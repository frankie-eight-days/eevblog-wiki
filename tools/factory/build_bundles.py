#!/usr/bin/env python3
"""Gather every passage in the corpus that touches a concept. No model involved.

This is the deterministic half of the Amp Hour factory: census mentions carry a
`paragraph_index`, so collecting the evidence for a concept is an index lookup,
not a judgment. The LLM extraction pass that turned bundles into claim packets is
NOT ported -- writers read the bundle directly, so nothing pre-selects what is
worth saying on their behalf.

Each passage carries the paragraph plus its neighbours, because a quote that
starts mid-thought needs the turn before it to be intelligible, and EEVblog is
mostly one man talking continuously.

  python3 tools/factory/build_bundles.py dropout-voltage service-manual asic
  python3 tools/factory/build_bundles.py --cap 400 asic
"""
import argparse
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
CENSUS = [ROOT / "census/captions-v2", ROOT / "census/full-v2"]
TRANSCRIPTS = [ROOT / "transcripts", ROOT / "transcripts_whisper"]
OUTDIR = ROOT / "articles/factory/bundles"
CTX = 420                       # chars of neighbouring paragraph kept as context
CAP = 300                       # passages per bundle
DEPTH_RANK = {"explains": 0, "opinion": 1, "mention": 2}
EPNUM = re.compile(r"EEVblog\s*#?\s*(\d+)", re.I)

_tcache = {}


def load_transcript(stem):
    """-> (frontmatter dict, [{speaker, text}, ...]). Cached; bundles revisit the
    same episode many times."""
    if stem in _tcache:
        return _tcache[stem]
    path = None
    for d in TRANSCRIPTS:
        p = d / f"{stem}.md"
        if p.exists():
            path = p
            break
    if path is None:
        _tcache[stem] = ({}, [])
        return _tcache[stem]
    raw = path.read_text()
    fm = {}
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        for line in raw[3:end].strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        raw = raw[end + 4:]
    paras = []
    for block in raw.strip().split("\n\n"):
        block = block.strip()
        if not block:
            continue
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)", block, re.S)
        if m:
            paras.append({"speaker": m.group(1), "text": m.group(2).strip()})
        else:
            paras.append({"speaker": None, "text": block})
    _tcache[stem] = (fm, paras)
    return _tcache[stem]


def stamps(fm):
    try:
        return {int(k): v for k, v in json.loads(fm.get("timestamps", "{}")).items()}
    except (json.JSONDecodeError, ValueError):
        return {}


def build_index(alias):
    """canonical concept -> [(stem, mention), ...] across every census dir."""
    idx = defaultdict(list)
    for d in CENSUS:
        for f in sorted(pathlib.Path(d).glob("*.json")):
            if f.name.startswith("_"):
                continue
            try:
                doc = json.loads(f.read_text())
            except json.JSONDecodeError:
                continue
            for m in doc.get("mentions", []):
                c = m.get("concept")
                if not c or m.get("paragraph_index") is None:
                    continue
                k = c.lower().strip().replace(" ", "-")
                idx[alias.get(k, k)].append((f.stem, m))
    return idx


def collect(concept, idx, cap):
    seen, depths, skipped = {}, Counter(), {}
    # skipped is retained for reporting only; nothing is dropped now
    for stem, m in idx.get(concept, ()):
        pi = m["paragraph_index"]
        fm, paras = load_transcript(stem)
        if not (0 <= pi < len(paras)):
            continue
        title = fm.get("title", "")
        num = EPNUM.search(title)
        # Videos whose titles carry no EEVblog number still need a citation
        # token. Rendering the missing number as "None" put literal "[None]"
        # into finished articles; DROPPING those passages instead was far worse
        # -- 32% of transcripts have no number in the title, and `sextant` lost
        # the single video holding 114 of its 116 paragraphs, leaving a top-50
        # concept with four passages. So numberless videos cite by video id:
        # uglier in the text, but every claim stays traceable and no evidence is
        # discarded for a naming accident.
        cite = num.group(1) if num else stem
        key = (stem, pi)
        depth = m.get("depth") or "mention"
        if key in seen:
            # a paragraph can be indexed by several surface forms; keep the
            # strongest depth rather than whichever arrived first
            if DEPTH_RANK[depth] < DEPTH_RANK[seen[key]["depth"]]:
                seen[key]["depth"] = depth
            continue
        depths[depth] += 1
        secs = stamps(fm).get(pi)
        url = fm.get("url", "")
        before = paras[pi - 1]["text"] if pi > 0 else ""
        after = paras[pi + 1]["text"] if pi + 1 < len(paras) else ""
        seen[key] = {
            "video_id": stem,
            "video_number": int(num.group(1)) if num else None,
            "cite": cite,
            "title": title,
            "url": f"{url}&t={secs}s" if url and secs is not None else url,
            "paragraph_index": pi,
            "depth": depth,
            "speaker": paras[pi]["speaker"] or m.get("speaker"),
            # `text` is what any quote must be verified against, byte for byte
            "text": paras[pi]["text"],
            "context_before": before[-CTX:],
            "context_after": after[:CTX],
        }
    out = sorted(seen.values(),
                 key=lambda p: (DEPTH_RANK[p["depth"]], -len(p["text"])))
    return out[:cap], depths, len(out), skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("concepts", nargs="+")
    ap.add_argument("--cap", type=int, default=CAP)
    args = ap.parse_args()

    alias = json.loads((ROOT / "canon/alias_table.json").read_text())
    print("indexing census...", file=sys.stderr)
    idx = build_index(alias)
    OUTDIR.mkdir(parents=True, exist_ok=True)

    for c in args.concepts:
        passages, depths, total, skipped = collect(c, idx, args.cap)
        if not passages:
            print(f"{c}: NO PASSAGES (not a canonical name?)")
            continue
        vids = {p["video_id"] for p in passages}
        words = sum(len(p["text"].split()) for p in passages)
        doc = {"concept": c, "passage_count": len(passages),
               "passages_available": total, "video_count": len(vids),
               "depths": dict(depths),
               "uncitable_videos_skipped": len(skipped),
               "passages": passages}
        dest = OUTDIR / f"{c}.json"
        dest.write_text(json.dumps(doc, indent=1))
        print(f"{c:22} {len(passages):4}/{total:4} passages  {len(vids):4} videos  "
              f"{words:6,} words  {dict(depths)}"
              + (f"  [{len(skipped)} uncitable videos skipped]" if skipped else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
