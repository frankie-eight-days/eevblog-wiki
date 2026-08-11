#!/usr/bin/env python3
"""Score every fetched caption track and write the ingest ledger.

Two generations of YouTube ASR are mixed across this channel: the modern one
punctuates, the old one emits a lowercase unbroken stream. A track with no
sentence boundaries has no span to slice a verbatim quote from, so every claim
drawn from it would be uncitable — those videos have to be re-transcribed.

Discriminator is words-per-sentence (see FINDINGS.md); the sampled good tracks
sit near 12, the failures run into the thousands.
"""
import json, pathlib, re, csv, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# usage: score_captions.py [channel]   ("" = main EEVblog, "2" = EEVblog2)
CH = sys.argv[1] if len(sys.argv) > 1 else ""
CAPS = ROOT / f"captions{CH}"
SRC = ROOT / "meta" / (f"EEVblog2_flat.tsv" if CH == "2" else "channel_flat.tsv")
OUT = ROOT / "meta" / f"ledger{CH}.tsv"

WPS_LIMIT = 40          # above this, treat the track as unpunctuated
ENDER = re.compile(r"[.!?]")


def text_of(path):
    """Flatten a json3 track to plain text (json3 has no rolling-caption
    duplication, unlike vtt -- yt-dlp #1734)."""
    try:
        doc = json.loads(path.read_text())
    except Exception:
        return None
    out = []
    for ev in doc.get("events", []):
        for seg in ev.get("segs", []) or []:
            out.append(seg.get("utf8", ""))
    return "".join(out).replace("\n", " ")


def main():
    meta = {}
    for line in SRC.read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split("\\t")          # the flat dump wrote literal \t
        if len(parts) < 3:
            continue
        meta[parts[0]] = (parts[1], int(parts[2] or 0))

    rows, missing = [], []
    for pos, (vid, (title, dur)) in enumerate(meta.items()):
        p = CAPS / f"{vid}.en.json3"
        if not p.exists():
            missing.append(vid)
            rows.append(dict(pos=pos, id=vid, title=title, duration_s=dur,
                             words=0, sentences=0, wps=0,
                             verdict="no-captions", provenance="whisper-large-v3"))
            continue
        txt = text_of(p)
        if txt is None:
            rows.append(dict(pos=pos, id=vid, title=title, duration_s=dur,
                             words=0, sentences=0, wps=0,
                             verdict="unreadable", provenance="whisper-large-v3"))
            continue
        words = len(txt.split())
        sents = len(ENDER.findall(txt))
        wps = round(words / sents, 1) if sents else float(words)
        bad = sents == 0 or wps > WPS_LIMIT
        rows.append(dict(pos=pos, id=vid, title=title, duration_s=dur,
                         words=words, sentences=sents, wps=wps,
                         verdict="needs-whisper" if bad else "good",
                         provenance="whisper-large-v3" if bad else "youtube-asr"))

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t",
                           quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    # --- summary: share by AUDIO HOURS, which is what the Whisper bill tracks.
    # Counting by video would understate it -- the broken ones run longer.
    tot_h = sum(r["duration_s"] for r in rows) / 3600
    def hrs(v): return sum(r["duration_s"] for r in rows if r["verdict"] == v) / 3600
    good_h, bad_h = hrs("good"), tot_h - hrs("good")
    n_bad = sum(1 for r in rows if r["verdict"] != "good")

    print(f"ledger: {OUT}  ({len(rows)} videos, {tot_h:.0f} h)")
    for v in ("good", "needs-whisper", "no-captions", "unreadable"):
        n = sum(1 for r in rows if r["verdict"] == v)
        if n:
            print(f"  {v:>14}: {n:5d} videos  {hrs(v):6.1f} h  "
                  f"{hrs(v)/tot_h*100:4.1f}% of audio")
    if missing:
        # verified with --list-subs: YouTube has no track at all for these,
        # auto or manual. They are Whisper work, not a fetch failure to retry.
        print(f"  ({len(missing)} have no YouTube track of any kind)")
    print(f"\nre-transcription needed: {n_bad} videos / {bad_h:.0f} h")
    print(f"  Whisper API @ $0.006/min : ${bad_h*60*0.006:,.0f}")
    print(f"  whole corpus for comparison: ${tot_h*60*0.006:,.0f}")
    print(f"  local whisper.cpp large-v3 @ ~5x realtime: {bad_h/5/24:.1f} days")
    med = sorted(r["wps"] for r in rows if r["verdict"] == "good")
    if med:
        print(f"\nmedian words/sentence on good tracks: {med[len(med)//2]}")


if __name__ == "__main__":
    sys.exit(main())
