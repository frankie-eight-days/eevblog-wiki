#!/usr/bin/env python3
"""Unattended Whisper transcription daemon for the Mac Mini.

Design constraints, and why each one is here:

RESUMABILITY. A completed video is one with a .json in OUT/. Nothing else is
state. Kill this process at any moment and the only work lost is whatever was
mid-flight -- at worst two videos. Restarting re-derives the queue from what is
already on disk, so there is no index to corrupt and no checkpoint to go stale.

ATOMIC WRITES. Output is written to a .part and renamed. A crash mid-write can
therefore never leave a truncated .json that a later run would mistake for done.

GPU UTILISATION. Whisper alternates a GPU-heavy encoder with an autoregressive
decoder that leaves the GPU mostly idle -- measured: 21-34s of CPU against 300s
of wall. Two transcribers fill each other's gaps (5.3x -> 8.5x realtime). A
separate pool of downloaders keeps decoded audio waiting so the GPU never
blocks on the network.

DISK. Audio is deleted the moment its transcript lands. Peak usage is the
bounded ready-queue, a few hundred MB, regardless of corpus size.

PAUSE. Touch the PAUSE file and workers stop picking up new videos, finishing
what is in flight first. Remove it to resume. No signals, no lost work.

PRIORITY. The queue is ordered: main channel first, then the second channel.
"""
import json, os, pathlib, queue, shutil, subprocess, sys, threading, time, csv

HOME = pathlib.Path.home()
BASE = HOME / "eevblog"
MODEL = BASE / "models/ggml-large-v3.bin"
WORK = BASE / "work"
OUT = BASE / "out"
LOGS = BASE / "logs"
QUEUE_FILE = BASE / "queue.tsv"
PAUSE = BASE / "PAUSE"
STATUS = BASE / "status.json"

N_TRANSCRIBE = 2          # measured sweet spot; 3 risks swapping on 16 GB
N_DOWNLOAD = 2
READY_MAX = 3             # bounded, so disk stays ~300 MB
WHISPER = "/opt/homebrew/bin/whisper-cli"

# Conditions the decoder toward punctuated output with the right vocabulary.
# Without it, old low-fidelity videos come back accurate but almost
# unpunctuated, which leaves no span to slice a verbatim quote from.
PROMPT = ("Hi, welcome to the EEVblog. I'm your host, Dave Jones. Today we're "
          "going to tear down some test gear and look at the PCB, the MOSFET, "
          "the LED driver and the oscilloscope. Now, that's a really "
          "interesting design decision, isn't it?")

_lock = threading.Lock()
_stats = {"done": 0, "failed": 0, "secs_audio": 0.0, "started": time.time()}
_inflight = {}
STOP = threading.Event()


def log(msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    with _lock:
        print(line, flush=True)
        with (LOGS / "daemon.log").open("a") as fh:
            fh.write(line + "\n")


def load_queue():
    """Ordered work list; presence of OUT/<id>.json means already done."""
    rows = []
    with QUEUE_FILE.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if not (OUT / f"{r['id']}.json").exists():
                rows.append(r)
    return rows


def fetch(vid):
    """Download bestaudio and decode to the 16 kHz mono WAV whisper.cpp wants."""
    src = WORK / f"{vid}.src"
    wav = WORK / f"{vid}.wav"
    if wav.exists():
        return wav
    r = subprocess.run(["yt-dlp", "-f", "bestaudio", "--no-progress",
                        "--retries", "5", "-o", str(src),
                        f"https://www.youtube.com/watch?v={vid}"],
                       capture_output=True, text=True)
    if not src.exists():
        raise RuntimeError(f"download failed: {r.stderr.strip()[-160:]}")
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                        "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
                        str(wav)], capture_output=True, text=True)
    src.unlink(missing_ok=True)
    if not wav.exists():
        raise RuntimeError(f"transcode failed: {r.stderr.strip()[-160:]}")
    return wav


def transcribe(vid, wav):
    stem = WORK / f"{vid}.out"
    r = subprocess.run([WHISPER, "-m", str(MODEL), "-f", str(wav), "-t", "4",
                        "-oj", "-of", str(stem), "--prompt", PROMPT,
                        "--no-prints"], capture_output=True, text=True)
    produced = stem.with_suffix(".out.json") if stem.with_suffix(".out.json").exists() \
        else pathlib.Path(str(stem) + ".json")
    if not produced.exists():
        raise RuntimeError(f"whisper produced nothing: {r.stderr.strip()[-160:]}")
    # atomic: a crash mid-write must not leave a half file that looks complete
    tmp = OUT / f"{vid}.json.part"
    shutil.move(str(produced), str(tmp))
    tmp.rename(OUT / f"{vid}.json")
    return OUT / f"{vid}.json"


def downloader(work_q, ready_q):
    while not STOP.is_set():
        try:
            row = work_q.get(timeout=2)
        except queue.Empty:
            return
        while PAUSE.exists() and not STOP.is_set():
            time.sleep(5)
        if STOP.is_set():
            return
        try:
            wav = fetch(row["id"])
            ready_q.put((row, wav))
            row.pop("_tries", None)
        except Exception as e:                       # noqa: BLE001
            # YouTube hands out transient 403s, especially on the first requests
            # of a session. Without a retry these videos would be silently
            # skipped for the whole run and only picked up on the next restart.
            tries = row.get("_tries", 0) + 1
            row["_tries"] = tries
            if tries <= 3:
                log(f"fetch retry {tries}/3 {row['id']}: {str(e)[-90:]}")
                time.sleep(min(60 * tries, 180))
                work_q.put(row)
            else:
                log(f"FETCH FAIL {row['id']} after 3 tries: {e}")
                with _lock:
                    _stats["failed"] += 1
        finally:
            work_q.task_done()


def transcriber(ready_q, total):
    while not STOP.is_set():
        try:
            row, wav = ready_q.get(timeout=5)
        except queue.Empty:
            if STOP.is_set():
                return
            continue
        vid = row["id"]
        with _lock:
            _inflight[vid] = {"title": row["title"][:60], "t0": time.time()}
        t0 = time.time()
        try:
            transcribe(vid, wav)
            dt = time.time() - t0
            secs = float(row.get("duration_s") or 0)
            with _lock:
                _stats["done"] += 1
                _stats["secs_audio"] += secs
                n = _stats["done"]
            log(f"[{n}/{total}] {vid} {secs/60:5.1f}min in {dt:5.0f}s "
                f"({secs/max(dt,1):4.1f}x)  {row['title'][:52]}")
        except Exception as e:                       # noqa: BLE001
            log(f"TRANSCRIBE FAIL {vid}: {e}")
            with _lock:
                _stats["failed"] += 1
        finally:
            wav.unlink(missing_ok=True)
            for junk in WORK.glob(f"{vid}.*"):
                junk.unlink(missing_ok=True)
            with _lock:
                _inflight.pop(vid, None)
            ready_q.task_done()
            write_status(total)


def write_status(total):
    el = time.time() - _stats["started"]
    done = _stats["done"]
    rate = _stats["secs_audio"] / el if el else 0        # audio-secs per wall-sec
    st = {
        "updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "done": done, "remaining": total - done, "total": total,
        "failed": _stats["failed"],
        "audio_hours_done": round(_stats["secs_audio"] / 3600, 1),
        "realtime_factor": round(rate, 2),
        "elapsed_hours": round(el / 3600, 2),
        "paused": PAUSE.exists(),
        "in_flight": {k: v["title"] for k, v in _inflight.items()},
    }
    if rate > 0 and done:
        remaining_audio = (_stats["secs_audio"] / done) * (total - done)
        st["eta_hours"] = round(remaining_audio / rate / 3600, 1)
    tmp = STATUS.with_suffix(".json.part")
    tmp.write_text(json.dumps(st, indent=1))
    tmp.rename(STATUS)


def main():
    for d in (WORK, OUT, LOGS):
        d.mkdir(parents=True, exist_ok=True)
    rows = load_queue()
    total = len(rows)
    if not total:
        log("queue empty - everything is transcribed")
        write_status(0)
        return 0
    log(f"starting: {total} videos remaining, "
        f"{sum(float(r.get('duration_s') or 0) for r in rows)/3600:.0f} h of audio")

    work_q, ready_q = queue.Queue(), queue.Queue(maxsize=READY_MAX)
    for r in rows:
        work_q.put(r)

    threads = []
    for _ in range(N_DOWNLOAD):
        t = threading.Thread(target=downloader, args=(work_q, ready_q), daemon=True)
        t.start(); threads.append(t)
    for _ in range(N_TRANSCRIBE):
        t = threading.Thread(target=transcriber, args=(ready_q, total), daemon=True)
        t.start(); threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            if work_q.empty() and ready_q.empty() and not _inflight:
                break
            write_status(total)
            time.sleep(20)
    except KeyboardInterrupt:
        log("interrupted - finishing in-flight work")
    STOP.set()
    write_status(total)
    log(f"exiting: {_stats['done']} done, {_stats['failed']} failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
