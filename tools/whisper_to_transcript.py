#!/usr/bin/env python3
"""Convert whisper.cpp JSON output into census-ready transcript markdown.

Two things differ from the json3 caption path:

GRANULARITY. whisper.cpp emits ~30-second segments containing several
sentences each, where json3 emits short caption lines. Paragraph breaks
therefore come from sentence boundaries (the text IS punctuated, that is what
we paid for) accumulated toward the Amp Hour's 45 words/paragraph, rather than
from timing gaps. Paragraph size is load-bearing: the census under-emits on
oversized paragraphs, so a mismatch here silently depresses claim yield.

TIMESTAMPS. Each segment carries millisecond offsets, so every paragraph can
record the second it was spoken. The Amp Hour could never do this -- its
citations point at an episode. Here a claim can deep-link to
youtube.com/watch?v=<id>&t=<seconds>, which is the single biggest upgrade this
corpus allows. The offsets are written into the frontmatter as a paragraph
index -> seconds map so downstream stages can build those links without
re-parsing the whisper output.
"""
import json, pathlib, re, csv, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGET_WORDS = 45          # match the Amp Hour's measured 45 words/paragraph
MAX_WORDS = 70
SENT = re.compile(r"(?<=[.!?])\s+")


def segments(path):
    d = json.loads(path.read_text())
    for s in d.get("transcription") or []:
        text = (s.get("text") or "").strip()
        if text:
            yield int((s.get("offsets") or {}).get("from", 0)), text


def paragraphs(path):
    """-> [(start_seconds, text)] at roughly TARGET_WORDS each."""
    out, cur, words, start = [], [], 0, None
    for off_ms, text in segments(path):
        for sent in SENT.split(text):
            sent = sent.strip()
            if not sent:
                continue
            if start is None:
                start = off_ms // 1000
            cur.append(sent)
            words += len(sent.split())
            if words >= TARGET_WORDS:
                out.append((start, " ".join(cur)))
                cur, words, start = [], 0, None
    if cur:
        out.append((start or 0, " ".join(cur)))
    # a paragraph that blew past MAX_WORDS means a sentence-less run; leave it
    # rather than cutting mid-sentence, but make it visible
    for st, p in out:
        if len(p.split()) > MAX_WORDS * 2:
            print(f"  WARN oversized paragraph ({len(p.split())} words) at {st}s",
                  file=sys.stderr)
    return out


def convert(vid, title, url, src, outdir):
    paras = paragraphs(src)
    if not paras:
        return None
    stamps = {i: st for i, (st, _) in enumerate(paras)}
    fm = ["---", f"video_id: {vid}", f"title: {title}", f"url: {url}",
          "source: whisper-large-v3-q5_0",
          f"timestamps: {json.dumps(stamps)}", "---"]
    # census_lib.parse_transcript consumes exactly ONE newline after the closing
    # '---' and then requires the body to begin '\n**Speaker:**'. So the file
    # needs a BLANK LINE between the delimiter and the first paragraph: the
    # first newline terminates '---', the second becomes the body's leading
    # newline that every char_start offset is measured from. Emitting only one
    # newline here makes every spec-correct census validate as 100% invalid --
    # census_lib documents this as a real, load-bearing bug, and this converter
    # hit it on the first run.
    body = "\n".join(f"**Dave Jones:** {p}\n" for _, p in paras)
    dest = outdir / f"{vid}.md"
    dest.write_text("\n".join(fm) + "\n\n" + body)
    return dest, len(paras), sum(len(p.split()) for _, p in paras)


def main():
    src_dir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "whisper_out"
    outdir = ROOT / "transcripts_whisper"
    outdir.mkdir(exist_ok=True)
    meta = {}
    for f in ("meta/ledger.tsv", "meta/ledger2.tsv"):
        p = ROOT / f
        if p.exists():
            for r in csv.DictReader(open(p), delimiter="\t"):
                meta[r["id"]] = r
    n = tw = tp = 0
    for src in sorted(src_dir.glob("*.json")):
        vid = src.stem
        r = meta.get(vid, {})
        res = convert(vid, r.get("title", vid),
                      f"https://www.youtube.com/watch?v={vid}", src, outdir)
        if res:
            _, np_, w = res
            n += 1; tp += np_; tw += w
    print(f"{n} transcripts, {tw:,} words, {tp:,} paragraphs, "
          f"{tw/max(tp,1):.0f} words/paragraph (Amp Hour 45)")


if __name__ == "__main__":
    sys.exit(main())
