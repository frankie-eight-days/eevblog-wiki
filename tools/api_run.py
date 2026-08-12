#!/usr/bin/env python3
"""Finish the corpus with the Whisper API.

Same skeleton as whisper_daemon.py -- resumable from disk, atomic writes,
throttled fetching, bot-check circuit breaker -- with the local whisper.cpp
call swapped for the API.

The bottleneck moves. Locally the GPU was the constraint and downloads were
free; here transcription is effectively instant and YOUTUBE DOWNLOADS ARE THE
ONLY LIMIT. There is therefore no point running more than one fetcher, and no
point putting a second machine on it: the block is per-IP, and both machines
sit behind one home connection. More concurrency would only spend the same
budget faster, which is what earned us an 85-minute block.

Output is written in the same shape whisper.cpp produces ({"transcription":
[{offsets, text}]}) so whisper_to_transcript.py needs no second code path and
the two halves of the corpus stay interchangeable.
"""
import csv, json, os, pathlib, queue, re, subprocess, sys, threading, time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "whisper_out"
WORK = ROOT / "scratch/api_work"
LOGS = ROOT / "logs"
QUEUE = ROOT / "meta/whisper_queue_pruned.tsv"
COOKIES = ROOT / "secrets/yt_cookies.txt"
KEY = (ROOT / "tools/census/openai_key").read_text().strip()

API = "https://api.openai.com/v1/audio/transcriptions"
MODEL = "whisper-1"
PRICE_PER_MIN = 0.006
MAX_BYTES = 25 * 1024 * 1024

N_API = 6                 # transcription is not the constraint; this is plenty
# It is a VOLUME quota, not a rate limit. Measured across four windows in this
# log: 99 videos at 63/h, 79 at 89/h, 87 at 37/h -- the block lands at ~85 videos
# whatever the pace. Slowing down therefore buys nothing; it stretches the same
# quota over three times the wall-clock.
#
#   15s gap: ~85 videos in ~50 min + 30 min cooldown  -> ~64/h
#   75s gap: ~87 videos in 141 min + 30 min cooldown  -> ~30/h
#
# So spend the quota fast and wait it out. (An earlier version of this comment
# claimed the opposite -- "the fast setting is the slow setting" -- from a run
# where cooldown escalation was mistaken for rate sensitivity.)
DOWNLOAD_GAP_S = 15
BOT_BLOCK = re.compile(r"not a bot|HTTP Error 429|Too Many Requests|"
                       r"Sign in to confirm you[’']?re", re.I)
# 45 minutes, not 30. Measured across every cycle in the log: a 30-minute wait was
# too short three times out of four -- the retry re-blocked instantly and the
# backoff doubled to 60 anyway, so the cycle cost 90 minutes of downtime instead
# of one clean wait. A 40-minute gap succeeded when it was tried. Waiting longer
# up front is strictly cheaper than spending an attempt to discover the quota has
# not reset yet.
COOLDOWN_S = 2700
COOLDOWN_MAX = 10800

STYLE_PROMPT = (
    "Hi, welcome to the EEVblog. I'm your host, Dave Jones. Today we're going "
    "to tear down some test gear and look at the PCB, the MOSFET, the LED "
    "driver and the oscilloscope. Now, that's a really interesting design "
    "decision, isn't it?")

_lock = threading.Lock()
_st = {"done": 0, "failed": 0, "mins": 0.0, "blocks": 0, "t0": time.time()}
_cool = {"s": COOLDOWN_S}
STOP = threading.Event()


def log(m):
    line = f"{time.strftime('%H:%M:%S')} {m}"
    with _lock:
        print(line, flush=True)
        LOGS.mkdir(exist_ok=True)
        with (LOGS / "api_run.log").open("a") as fh:
            fh.write(line + "\n")


def fetch(vid):
    ogg = WORK / f"{vid}.ogg"
    if ogg.exists():
        return ogg
    # Build flags as a list and append -- never splice into the middle of the
    # command. A cmd[5:5] insert landed between '-f' and 'bestaudio', so yt-dlp
    # read '--cookies' as the format, tried to fetch every format at once, and
    # died with "Fixed output name but more than one file to download".
    cmd = ["nice", "-n", "10", "yt-dlp", "-f", "bestaudio", "--no-progress",
           "--retries", "3"]
    if COOKIES.exists():
        cmd += ["--cookies", str(COOKIES)]
    # %(ext)s keeps yt-dlp free to pick the container; a fixed name is also what
    # trips the multi-file error when a format selector resolves to more than one.
    cmd += ["-o", str(WORK / f"{vid}.%(ext)s"),
            f"https://www.youtube.com/watch?v={vid}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    got = [p for p in WORK.glob(f"{vid}.*") if p.suffix != ".ogg"]
    if not got:
        # Keep the WHOLE stderr. yt-dlp puts "Sign in to confirm you're not a bot"
        # at the START of a long error that ends with a wiki URL, so the old
        # [-200:] tail cut the marker off, BOT_BLOCK never matched, and instead of
        # pausing 30 minutes the run would have burned through all 748 videos
        # marking them failed. Truncate at the log line, never before the match.
        raise RuntimeError(f"download failed: {r.stderr.strip()}")
    src = got[0]
    # 16 kHz mono opus: exactly what Whisper resamples to internally, and ~7x
    # smaller than source, which is what makes the upload tractable.
    r = subprocess.run(["nice", "-n", "10", "ffmpeg", "-y", "-loglevel", "error",
                        "-threads", "2", "-i", str(src), "-ac", "1",
                        "-ar", "16000", "-c:a", "libopus", "-b:a", "16k",
                        str(ogg)], capture_output=True, text=True)
    src.unlink(missing_ok=True)
    if not ogg.exists():
        raise RuntimeError(f"transcode failed: {r.stderr.strip()[-200:]}")
    return ogg


def transcribe(path):
    b = "----eevapi7f2c1"
    body = bytearray()

    def field(n, v):
        body.extend(f"--{b}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{n}"\r\n\r\n'.encode())
        body.extend(f"{v}\r\n".encode())

    field("model", MODEL)
    field("response_format", "verbose_json")
    field("prompt", STYLE_PROMPT)
    body.extend(f"--{b}\r\n".encode())
    body.extend(f'Content-Disposition: form-data; name="file"; '
                f'filename="{path.name}"\r\n'.encode())
    body.extend(b"Content-Type: audio/ogg\r\n\r\n")
    body.extend(path.read_bytes())
    body.extend(f"\r\n--{b}--\r\n".encode())
    req = urllib.request.Request(API, data=bytes(body), method="POST")
    req.add_header("Authorization", f"Bearer {KEY}")
    req.add_header("Content-Type", f"multipart/form-data; boundary={b}")
    # NOT 1800. A 40-minute video is ~5 MB of 16 kHz opus and answers in under a
    # minute; anything past a few minutes is a hung socket, not slow work. At 1800
    # a bad patch on OpenAI's side (504s, broken pipes) parked all six workers for
    # half an hour each, the 8-slot ready queue filled, and the single downloader
    # blocked forever in put() -- the whole run deadlocked with an empty work dir.
    with urllib.request.urlopen(req, timeout=240) as resp:
        return json.loads(resp.read())


def to_whispercpp_shape(doc):
    """Match whisper.cpp's on-disk shape so the 286 local transcripts and these
    are indistinguishable downstream."""
    segs = []
    for s in doc.get("segments") or []:
        segs.append({"offsets": {"from": int(float(s.get("start", 0)) * 1000),
                                 "to": int(float(s.get("end", 0)) * 1000)},
                     "text": s.get("text", "")})
    if not segs and doc.get("text"):
        segs = [{"offsets": {"from": 0, "to": 0}, "text": doc["text"]}]
    return {"transcription": segs, "source": "whisper-1-api"}


def downloader(work_q, ready_q, total):
    while not STOP.is_set():
        try:
            row = work_q.get(timeout=3)
        except queue.Empty:
            return
        vid = row["id"]
        try:
            ogg = fetch(vid)
            if ogg.stat().st_size > MAX_BYTES:
                log(f"TOO BIG {vid} ({ogg.stat().st_size/1e6:.0f} MB) - needs chunking, skipped")
                ogg.unlink(missing_ok=True)
                with _lock: _st["failed"] += 1
            else:
                ready_q.put((row, ogg))
            _cool["s"] = COOLDOWN_S
            time.sleep(DOWNLOAD_GAP_S)
        except Exception as e:                                  # noqa: BLE001
            msg = str(e)
            if BOT_BLOCK.search(msg):
                work_q.put(row)
                wait = _cool["s"]
                with _lock: _st["blocks"] += 1
                log(f"BOT-CHECK - pausing fetches {wait//60} min (queue intact)")
                slept = 0
                while slept < wait and not STOP.is_set():
                    time.sleep(10); slept += 10
                _cool["s"] = min(wait * 2, COOLDOWN_MAX)
            else:
                tries = row.get("_t", 0) + 1
                row["_t"] = tries
                if tries <= 2:
                    time.sleep(30 * tries); work_q.put(row)
                else:
                    log(f"FETCH FAIL {vid}: {msg[-120:]}")
                    with _lock: _st["failed"] += 1
        finally:
            work_q.task_done()


def worker(ready_q, total, work_q):
    while not STOP.is_set():
        try:
            row, ogg = ready_q.get(timeout=10)
        except queue.Empty:
            if STOP.is_set(): return
            continue
        vid = row["id"]
        try:
            doc = transcribe(ogg)
            tmp = OUT / f"{vid}.json.part"
            tmp.write_text(json.dumps(to_whispercpp_shape(doc)))
            tmp.rename(OUT / f"{vid}.json")          # atomic
            mins = float(doc.get("duration") or int(row["duration_s"])) / 60
            with _lock:
                _st["done"] += 1; _st["mins"] += mins; n = _st["done"]
            el = (time.time() - _st["t0"]) / 3600
            log(f"[{n}/{total}] {vid} {mins:5.1f}min  ${_st['mins']*PRICE_PER_MIN:6.2f} "
                f"spent  {n/max(el,.01):4.0f}/h  {row['title'][:44]}")
        except Exception as e:                                  # noqa: BLE001
            # A transcription failure used to drop the video on the floor -- the
            # audio was deleted and nothing ever re-queued it, so a transient 504
            # cost a video permanently. Put it back and let the downloader refetch.
            tries = row.get("_a", 0) + 1
            row["_a"] = tries
            if tries <= 2:
                log(f"API RETRY {vid} ({tries}/2): {type(e).__name__} {str(e)[-90:]}")
                work_q.put(row)
            else:
                log(f"API FAIL {vid}: {type(e).__name__} {str(e)[-120:]}")
                with _lock: _st["failed"] += 1
        finally:
            ogg.unlink(missing_ok=True)
            ready_q.task_done()


def main():
    OUT.mkdir(exist_ok=True); WORK.mkdir(parents=True, exist_ok=True); LOGS.mkdir(exist_ok=True)
    have = {p.stem for p in OUT.glob("*.json")}
    rows = [r for r in csv.DictReader(open(QUEUE), delimiter="\t")
            if r["id"] not in have and int(r["duration_s"]) <= 240 * 60]
    total = len(rows)
    hrs = sum(int(r["duration_s"]) for r in rows) / 3600
    log(f"START: {total} videos, {hrs:.0f} h, est ${hrs*60*PRICE_PER_MIN:.0f}, "
        f"cookies={'yes' if COOKIES.exists() else 'NO'}")
    if not total:
        return 0
    work_q, ready_q = queue.Queue(), queue.Queue(maxsize=8)
    for r in rows:
        work_q.put(r)
    threads = [threading.Thread(target=downloader, args=(work_q, ready_q, total), daemon=True)]
    threads += [threading.Thread(target=worker, args=(ready_q, total, work_q),
                                 daemon=True)
                for _ in range(N_API)]
    for t in threads: t.start()
    try:
        while any(t.is_alive() for t in threads):
            if work_q.empty() and ready_q.empty():
                time.sleep(30)
                if work_q.empty() and ready_q.empty(): break
            time.sleep(15)
    except KeyboardInterrupt:
        log("interrupted")
    STOP.set()
    el = (time.time() - _st["t0"]) / 3600
    log(f"DONE: {_st['done']} transcribed, {_st['failed']} failed, "
        f"{_st['blocks']} bot-blocks, ${_st['mins']*PRICE_PER_MIN:.2f} spent, {el:.1f} h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
