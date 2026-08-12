#!/usr/bin/env python3
"""Convert every good-caption track on both channels into census transcripts.

json3_to_transcript.py takes ids on the command line, which overflows ARG_MAX at
1,763 of them (and silently mis-parses the channel arg when the list is empty).
This drives its convert() directly instead.
"""
import csv, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from json3_to_transcript import convert, ROOT

outdir = ROOT / "transcripts"
outdir.mkdir(exist_ok=True)
for ch in ("", "2"):
    capdir = ROOT / f"captions{ch}"
    rows = [r for r in csv.DictReader(open(ROOT / f"meta/ledger{ch}.tsv"), delimiter="\t")
            if r["verdict"] == "good"]
    n = w = p = miss = 0
    for r in rows:
        if (outdir / f"{r['id']}.md").exists():
            n += 1; continue
        res = convert(r["id"], r["title"],
                      f"https://www.youtube.com/watch?v={r['id']}", outdir, capdir)
        if res:
            _, np_, ww = res; n += 1; p += np_; w += ww
        else:
            miss += 1
    print(f"channel{ch or '1'}: {n}/{len(rows)} converted, {miss} missing caption file, "
          f"{w:,} new words, {w/max(p,1):.0f} words/paragraph")
