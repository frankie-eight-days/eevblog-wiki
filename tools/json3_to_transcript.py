#!/usr/bin/env python3
"""Convert a YouTube json3 caption track into the transcript markdown the
census pipeline expects (frontmatter + '**Speaker:** ...' paragraphs).

The Amp Hour transcripts get their paragraph breaks free, from speaker turns.
EEVblog is one man talking continuously, so breaks have to be manufactured --
and they matter, because the census records paragraph_index + char_start and
an article's quotes are sliced out of those paragraphs. Too coarse and a quote
drags in unrelated material; too fine and it can't reach a full thought.

Break on a real pause (a gap between caption events) at a sentence boundary,
which follows how Dave actually speaks rather than an arbitrary word count.
"""
import json, pathlib, re, sys, csv

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Paragraph SIZE is not cosmetic: the census emits mentions per paragraph and
# under-emits badly when they are oversized. A first pass at ~217 words/paragraph
# scored 2.16 mentions/paragraph against the Amp Hour's 1.11 -- only 2x the rate
# from 4.8x the text, which reads as "EEVblog is 4x less informative" when it is
# really just coarser chunking. Match the Amp Hour's 45 words/paragraph so the
# two corpora are measured with the same instrument.
GAP_MS = 400           # pause that justifies a paragraph break
MIN_WORDS = 15         # ...but only once the paragraph has some substance
MAX_WORDS = 40         # hard break, so no paragraph is too big to quote from


def events(path):
    """Yield (start_ms, dur_ms, text) per caption event.

    Segments WITHIN an event carry their own spacing and concatenate directly,
    but consecutive events do not -- joining them raw welds the last word of one
    line to the first of the next ("about is" + "the basic" -> "isthe basic").
    Every quote downstream is sliced byte-exact out of this text, so that has to
    be right here; there is no later stage that could repair it.
    """
    doc = json.loads(path.read_text())
    for ev in doc.get("events", []):
        segs = ev.get("segs") or []
        text = "".join(s.get("utf8", "") for s in segs).replace("\n", " ")
        if text.strip():
            yield ev.get("tStartMs", 0), ev.get("dDurationMs", 0), text.strip() + " "


def paragraphs(path):
    out, cur, words, prev_end = [], [], 0, None
    for start, dur, text in events(path):
        gap = start - prev_end if prev_end is not None else 0
        ends_sentence = bool(cur) and re.search(r"[.!?]\s*$", "".join(cur).strip())
        if cur and ((gap >= GAP_MS and words >= MIN_WORDS and ends_sentence)
                    or words >= MAX_WORDS):
            out.append("".join(cur).strip())
            cur, words = [], 0
        cur.append(text)
        words += len(text.split())
        prev_end = start + dur
    if cur:
        out.append("".join(cur).strip())
    return [re.sub(r"\s+", " ", p) for p in out if p.strip()]


def convert(vid, title, url, outdir, capdir):
    src = capdir / f"{vid}.en.json3"
    if not src.exists():
        return None
    paras = paragraphs(src)
    if not paras:
        return None
    fm = (f"---\nvideo_id: {vid}\ntitle: {title}\nurl: {url}\n"
          f"source: youtube-asr\n---\n")
    # NOTE: census_lib.parse_transcript requires the body to begin with exactly
    # one newline then '**' -- do not tidy this join.
    body = "\n" + "\n\n".join(f"**Dave Jones:** {p}" for p in paras) + "\n"
    dest = outdir / f"{vid}.md"
    dest.write_text(fm + body)
    return dest, len(paras), sum(len(p.split()) for p in paras)


def main():
    ch = sys.argv[1] if len(sys.argv) > 1 else ""
    ids = sys.argv[2:]
    ledger = {r["id"]: r for r in
              csv.DictReader(open(ROOT / f"meta/ledger{ch}.tsv"), delimiter="\t")}
    capdir = ROOT / f"captions{ch}"
    outdir = ROOT / "transcripts"
    outdir.mkdir(exist_ok=True)
    for vid in ids:
        r = ledger.get(vid)
        if not r:
            print(f"  {vid}: not in ledger"); continue
        res = convert(vid, r["title"], f"https://www.youtube.com/watch?v={vid}",
                      outdir, capdir)
        if res:
            dest, n, w = res
            print(f"  {dest.name}: {n} paragraphs, {w:,} words "
                  f"({w/(int(r['duration_s'])/60):.0f} wpm)")
        else:
            print(f"  {vid}: no caption track")


if __name__ == "__main__":
    main()
