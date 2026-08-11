#!/usr/bin/env python3
"""Re-transcribe videos whose YouTube captions are unpunctuated.

Pipeline per video: download bestaudio -> transcode to 16 kHz mono opus (what
Whisper consumes internally, ~7x smaller than the source, which is what makes
the upload tractable) -> POST to the transcription API -> write transcript ->
delete the audio. Peak disk stays a few tens of MB no matter how many videos run.

Reports measured cost and wall clock so the full-corpus estimate comes from
observation rather than the price sheet.
"""
import json, os, pathlib, subprocess, sys, time, csv, mimetypes
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY = (ROOT / "tools/census/openai_key").read_text().strip()
MODEL = os.environ.get("WHISPER_MODEL", "whisper-1")
PRICE_PER_MIN = 0.006
API = "https://api.openai.com/v1/audio/transcriptions"
WORK = ROOT / "scratch/audio"
OUT = ROOT / "whisper"
MAX_BYTES = 25 * 1024 * 1024      # API hard limit

# Whisper conditions on `prompt` as though it were the transcript of immediately
# preceding audio, so a well-punctuated sample biases the decoder toward emitting
# punctuation. Without it, roughly 2 in 5 of the old (2009-2010) low-fidelity
# videos come back accurate but nearly unpunctuated -- one 4-minute video scored
# 580 words per sentence -- which leaves no span to slice a verbatim quote from,
# the exact failure we are paying to escape. With it: 580 -> 12.6 w/sent.
#
# This is NOT the punctuation restoration ruled out in FINDINGS.md. Restoration
# has a model rewrite a corrupted transcript it cannot hear, inventing text that
# then becomes the citable source. This conditions a primary transcription of the
# real audio; every word still comes from what Dave actually said.
STYLE_PROMPT = (
    "Hi, welcome to the EEVblog. I'm your host, Dave Jones. Today we're going "
    "to take a look at some test gear. Let's tear it down and see what's inside. "
    "Now, that's a really interesting design decision, isn't it?"
)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def fetch_audio(vid):
    WORK.mkdir(parents=True, exist_ok=True)
    raw = WORK / f"{vid}.src"
    ogg = WORK / f"{vid}.ogg"
    if not ogg.exists():
        r = run(["yt-dlp", "-f", "bestaudio", "--no-progress", "-o", str(raw),
                 f"https://www.youtube.com/watch?v={vid}"])
        if not raw.exists():
            return None, f"download failed: {r.stderr.strip()[:120]}"
        # 16 kHz mono is exactly what Whisper resamples to; sending more is
        # wasted upload, and upload is the binding constraint on this job.
        r = run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
                 "-ac", "1", "-ar", "16000", "-c:a", "libopus", "-b:a", "16k",
                 str(ogg)])
        raw.unlink(missing_ok=True)
        if not ogg.exists():
            return None, f"transcode failed: {r.stderr.strip()[:120]}"
    return ogg, None


def transcribe(path):
    boundary = "----ampwhisper7be1f2"
    body = bytearray()

    def field(name, value):
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        body.extend(f"{value}\r\n".encode())

    field("model", MODEL)
    field("response_format", "verbose_json")   # carries segment timings
    field("prompt", STYLE_PROMPT)
    body.extend(f"--{boundary}\r\n".encode())
    body.extend(f'Content-Disposition: form-data; name="file"; '
                f'filename="{path.name}"\r\n'.encode())
    body.extend(b"Content-Type: audio/ogg\r\n\r\n")
    body.extend(path.read_bytes())
    body.extend(f"\r\n--{boundary}--\r\n".encode())

    req = urllib.request.Request(API, data=bytes(body), method="POST")
    req.add_header("Authorization", f"Bearer {KEY}")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=1800) as resp:
        return json.loads(resp.read())


def main():
    ids = sys.argv[1:]
    led = {r["id"]: r for r in
           csv.DictReader(open(ROOT / "meta/ledger.tsv"), delimiter="\t")}
    OUT.mkdir(exist_ok=True)
    t0 = time.time()
    mins = 0.0
    for vid in ids:
        r = led.get(vid, {})
        t = time.time()
        ogg, err = fetch_audio(vid)
        if err:
            print(f"  {vid}: {err}")
            continue
        mb = ogg.stat().st_size / 1e6
        if ogg.stat().st_size > MAX_BYTES:
            print(f"  {vid}: {mb:.1f} MB exceeds the 25 MB limit - needs chunking")
            continue
        t_dl = time.time() - t
        t = time.time()
        try:
            doc = transcribe(ogg)
        except Exception as e:
            print(f"  {vid}: API error {type(e).__name__}: {str(e)[:140]}")
            continue
        t_api = time.time() - t
        dur = float(doc.get("duration") or int(r.get("duration_s", 0)))
        mins += dur / 60
        (OUT / f"{vid}.json").write_text(json.dumps(doc))
        txt = doc.get("text", "")
        sents = sum(txt.count(c) for c in ".!?")
        print(f"  {vid}  {dur/60:5.1f} min  {mb:5.1f} MB  "
              f"prep {t_dl:5.1f}s  api {t_api:6.1f}s  "
              f"{len(txt.split()):6,} words  {len(txt.split())/max(sents,1):4.1f} w/sent")
        ogg.unlink(missing_ok=True)

    wall = time.time() - t0
    print(f"\n{len(ids)} videos, {mins:.1f} min of audio in {wall:.0f}s wall")
    print(f"measured cost: ${mins*PRICE_PER_MIN:.2f}  "
          f"(${mins*PRICE_PER_MIN/max(mins/60,1e-9):.2f}/audio-hour)")
    print(f"throughput: {mins/(wall/60):.1f} audio-minutes per wall-minute, serial")


if __name__ == "__main__":
    main()
