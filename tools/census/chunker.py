"""Split a transcript into overlapping paragraph chunks for the v3-chunk prompt.

Chunks are CHUNK_SIZE paragraphs with OVERLAP paragraphs of carry-over, so
consecutive chunks share their boundary paragraph (chunk k ends on the paragraph
chunk k+1 starts on). Each paragraph is rendered with its GLOBAL index as a
"[pN] " prefix in front of the "**Speaker:**" label; the prompt tells the model
to copy that number into paragraph_index.

Paragraph indices and text come from census_lib.parse_transcript, so the
leading-newline body convention is the one the validators use -- p.text is the
paragraph verbatim, with no leading newline of its own.

-> <scratch>/chunks/<stem>/<nn>.txt
"""
from __future__ import annotations

import os
import sys

SCRATCH = os.path.dirname(os.path.abspath(__file__))
WIKI = "/Users/frankwalsh/Documents/vibecoding/eevblog_wiki"
TRANSCRIPTS = os.environ.get("EEV_TRANSCRIPTS", os.path.join(WIKI, "transcripts"))
CHUNKS = os.path.join(SCRATCH, "chunks")

sys.path.insert(0, SCRATCH)
import census_lib as cl  # noqa: E402

CHUNK_SIZE = 40
OVERLAP = 1

STEMS = [
    "the-amp-hour-79-ludibrious-luxating-layout",
    "0212-an-interview-with-trey-german-launchpad-laden-lodesman",
]


def chunk_ranges(n_paras, size=CHUNK_SIZE, overlap=OVERLAP):
    """[(start, end)) covering [0, n_paras) with `overlap` paragraphs of carry-over."""
    step = size - overlap
    assert step > 0
    out = []
    start = 0
    while start < n_paras:
        end = min(start + size, n_paras)
        out.append((start, end))
        if end == n_paras:
            break
        start += step
    return out


def render(tr, stem, ci, n_chunks, lo, hi):
    head = (
        "CHUNK %d of %d (paragraphs %d-%d of %d)\n"
        "episode: %s | title: %s | url: %s | file: %s\n"
        % (ci, n_chunks, lo, hi - 1, len(tr.paragraphs),
           tr.episode if tr.episode is not None else "(none in frontmatter)",
           tr.title, tr.url, stem + ".md")
    )
    paras = ["[p%d] %s" % (p.index, p.text) for p in tr.paragraphs[lo:hi]]
    return head + "\n" + "\n\n".join(paras) + "\n"


def build(stem):
    tr = cl.parse_transcript(os.path.join(TRANSCRIPTS, stem + ".md"))
    for p in tr.paragraphs:
        assert tr.body[p.start:p.end] == p.text, (stem, p.index)
    rngs = chunk_ranges(len(tr.paragraphs))
    outdir = os.path.join(CHUNKS, stem)
    os.makedirs(outdir, exist_ok=True)
    for ci, (lo, hi) in enumerate(rngs):
        text = render(tr, stem, ci, len(rngs), lo, hi)
        with open(os.path.join(outdir, "%02d.txt" % ci), "w", encoding="utf-8") as fh:
            fh.write(text)
    # every paragraph must appear in at least one chunk
    seen = set()
    for lo, hi in rngs:
        seen.update(range(lo, hi))
    assert seen == set(range(len(tr.paragraphs))), "chunk coverage gap in %s" % stem
    return tr, rngs


def main():
    for stem in STEMS:
        tr, rngs = build(stem)
        print("%-60s paragraphs=%4d words=%6d chunks=%2d"
              % (stem[:60], len(tr.paragraphs), len(tr.body.split()), len(rngs)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
