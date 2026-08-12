#!/usr/bin/env python3
"""Decide which canonical concepts become articles.

  python3 tools/canon/build_candidates.py [--census DIR ...] [--canon DIR]

Writes articles/candidates.json (full record for everything clearing the floor)
and articles/candidates_below_floor.json (compact rows, so the floor can be
relitigated without loading 50k objects into a UI).

TWO GATES, and they use different depths on purpose.

  Notability  -- does this concept RECUR? Counted over every depth, because a
                 thing named across 30 videos is part of the channel's furniture
                 whether or not any single mention teaches it.
  Substance   -- is there enough to WRITE? Counted over `explains` only, because
                 a paragraph that merely says the word "FPGA" contains no
                 information about FPGAs.

A concept needs both. That is why the score multiplies them rather than picking
one: taught-but-once scores low, named-constantly-but-never-taught scores ~zero.

DIFFERENCE FROM THE AMP HOUR. Its formula carried a `distinct_guests` term --
a concept three different guests independently explained was better evidenced
than one host's hobbyhorse. EEVblog is one man talking to camera, so that signal
does not exist and the term is dropped rather than faked. Video count carries the
recurrence signal alone here.

View counts are recorded but deliberately NOT scored. They measure what YouTube
promoted, not what the corpus explains; letting them into the ranking would build
a wiki about Dave's greatest hits instead of about electronics.
"""
import argparse, json, math, pathlib, re, sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

MIN_VIDEOS = 3            # notability floor
EXPLAINS_FOR_ARTICLE = 15  # provisional; set from the sweep this script prints
SWEEP = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 80, 100]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", nargs="+",
                    default=[str(ROOT / "census/captions-v1"),
                             str(ROOT / "census/full-v1")])
    ap.add_argument("--canon", default=str(ROOT / "canon"))
    ap.add_argument("--out", default=str(ROOT / "articles"))
    ap.add_argument("--threshold", type=int, default=EXPLAINS_FOR_ARTICLE)
    args = ap.parse_args()
    canon, out = pathlib.Path(args.canon), pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    alias = json.loads((canon / "alias_table.json").read_text())
    vocab = {c["canonical_name"]: c for c in
             json.loads((canon / "vocabulary.json").read_text())["concepts"]}

    meta = {}
    for f in ("meta/ledger.tsv", "meta/ledger2.tsv"):
        p = ROOT / f
        if p.exists():
            import csv
            for r in csv.DictReader(open(p), delimiter="\t"):
                meta[r["id"]] = r
    views = {}
    vp = ROOT / "meta/views.txt"
    if vp.exists():
        for line in vp.read_text().splitlines():
            vid, _, v = line.partition("|")
            if v.isdigit():
                views[vid] = int(v)

    stats = defaultdict(lambda: {
        "videos": set(), "mentions": 0, "explains": 0, "opinion": 0,
        "snips": [], "titles": [], "views": 0, "nums": []})
    n_videos = 0
    for d in args.census:
        for f in sorted(pathlib.Path(d).glob("*.json")):
            if f.name.startswith("_"):
                continue
            try:
                doc = json.loads(f.read_text())
            except json.JSONDecodeError:
                continue
            n_videos += 1
            vid = f.stem
            title = (meta.get(vid, {}) or {}).get("title", "")
            num = re.search(r"#?\s*(\d{2,4})\b", title)
            for m in doc.get("mentions", []):
                c = m.get("concept")
                if not c:
                    continue
                c = alias.get(c, c)
                s = stats[c]
                if vid not in s["videos"]:
                    s["videos"].add(vid)
                    s["views"] += views.get(vid, 0)
                    if title and len(s["titles"]) < 5:
                        s["titles"].append(title)
                    if num:
                        s["nums"].append(int(num.group(1)))
                s["mentions"] += 1
                d_ = m.get("depth")
                if d_ == "explains":
                    s["explains"] += 1
                elif d_ == "opinion":
                    s["opinion"] += 1
                if d_ == "explains" and len(s["snips"]) < 3 and m.get("context_snippet"):
                    s["snips"].append(m["context_snippet"])

    def score(s):
        return s["explains"] * math.log(1 + len(s["videos"]))

    above, below = [], []
    for c, s in stats.items():
        v = vocab.get(c, {})
        nv = len(s["videos"])
        row = {"concept": c, "type": v.get("type", "other"),
               "video_count": nv, "mention_count": s["mentions"],
               "explains_count": s["explains"], "opinion_count": s["opinion"],
               "score": round(score(s), 2)}
        if nv < MIN_VIDEOS:
            below.append(row)
            continue
        row.update({
            "aliases": v.get("aliases", []),
            "broader": v.get("broader", []),
            "total_views": s["views"],
            "first_video_num": min(s["nums"]) if s["nums"] else None,
            "last_video_num": max(s["nums"]) if s["nums"] else None,
            "sample_titles": s["titles"],
            "sample_snippets": s["snips"],
            "low_confidence": v.get("low_confidence", False),
            "asr_suspect_mentions": v.get("asr_suspect_mentions", 0),
        })
        above.append(row)

    sweep = {t: sum(1 for r in above if r["explains_count"] >= t) for t in SWEEP}
    for r in above:
        if r["explains_count"] >= args.threshold:
            r["suggested"] = {"status": "article", "parent": None}
        elif r["broader"]:
            r["suggested"] = {"status": "section-of", "parent": r["broader"][0]}
        else:
            r["suggested"] = {"status": "section-of", "parent": None}
    for r in below:
        r["suggested"] = {"status": "skip", "parent": None}
    above.sort(key=lambda r: -r["score"])

    counts = Counter(r["suggested"]["status"] for r in above + below)
    payload = {"_meta": {
        "generated_from": {"census": args.census, "canon": str(canon)},
        "videos_processed": n_videos,
        "concepts_total": len(stats),
        "notability_floor": {"video_count": MIN_VIDEOS},
        "explains_threshold_for_article": args.threshold,
        "explains_threshold_sweep": sweep,
        "passed_floor": len(above),
        "counts": dict(counts),
        "score_formula": "explains_count * log(1 + video_count)",
        "dropped_from_amp_hour": "distinct_guests term -- EEVblog is a solo "
                                 "channel, so the signal does not exist",
        "views_note": "total_views recorded but NOT scored; it measures YouTube "
                      "promotion, not corpus coverage",
    }, "candidates": above}
    (out / "candidates.json").write_text(json.dumps(payload, indent=1))
    (out / "candidates_below_floor.json").write_text(json.dumps(below, indent=0))

    print(f"{n_videos:,} videos, {len(stats):,} canonical concepts")
    print(f"{len(above):,} clear the floor (>={MIN_VIDEOS} videos), {len(below):,} below")
    print(f"\nexplains-threshold sweep (articles at each cut):")
    for t in SWEEP:
        bar = "#" * min(60, sweep[t] // 8)
        print(f"  >={t:3d}  {sweep[t]:5d}  {bar}")
    print(f"\nat threshold {args.threshold}: {dict(counts)}")
    print("\ntop 25 by score:")
    for r in above[:25]:
        print(f"  {r['score']:8.1f}  {r['video_count']:4d} vids  "
              f"{r['explains_count']:4d} expl  {r['type']:18s} {r['concept']}")


if __name__ == "__main__":
    sys.exit(main())
