#!/usr/bin/env python3
"""Fold one canonical concept into another in an already-built canon.

The mirror of split_aliases.py, and needed for the same reason: re-running the
whole canon to correct a handful of groups costs ~2.6 h and re-rolls every other
verdict. Used for acronym pairs the fixed `acronyms_of` now catches but the
built canon missed, e.g. `adc` -> `analog-to-digital-converter`.

Aggregates are recomputed from the census rather than added together, because
the two groups may share episodes and summing would double-count them.

  python3 merge_aliases.py adc=analog-to-digital-converter dac=digital-to-analog-converter
  python3 merge_aliases.py --dry-run adc=analog-to-digital-converter
"""
import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from canon_lib import Corpus                                # noqa: E402
from split_aliases import emit                              # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", metavar="FROM=INTO")
    ap.add_argument("--census", nargs="+",
                    default=[str(ROOT / "census/captions-v2"),
                             str(ROOT / "census/full-v2")])
    ap.add_argument("--canon", default=str(ROOT / "canon"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    canon_dir = pathlib.Path(args.canon)

    alias = json.loads((canon_dir / "alias_table.json").read_text())
    voc = json.loads((canon_dir / "vocabulary.json").read_text())
    byname = {c["canonical_name"]: c for c in voc["concepts"]}

    merges = []
    for p in args.pairs:
        src, dst = p.split("=", 1)
        if src not in byname or dst not in byname:
            print(f"skip {p}: {'src' if src not in byname else 'dst'} not canonical")
            continue
        merges.append((src, dst))
    if not merges:
        return 1

    members = {}
    for canon in {c for pair in merges for c in pair}:
        members[canon] = {canon} | {a for a, c in alias.items() if c == canon}

    corpus = Corpus(args.census)
    new_alias = dict(alias)
    changed = []
    for src, dst in merges:
        group = members[src] | members[dst]
        new_canon, entry = emit(group, corpus)
        # broader relations from both sides survive the fold
        entry["broader"] = sorted(set(byname[src]["broader"]) |
                                  set(byname[dst]["broader"]) - {new_canon})
        print(f"{src} + {dst} -> {new_canon}: "
              f"{entry['episode_count']} videos, {entry['total_mentions']} mentions, "
              f"{len(entry['aliases'])} aliases")
        changed.append((src, dst, new_canon, entry, group))

    if args.dry_run:
        print("\n--dry-run: nothing written")
        return 0

    drop = set()
    add = []
    for src, dst, new_canon, entry, group in changed:
        drop |= {src, dst}
        for n in group:
            new_alias.pop(n, None)
            if n != new_canon:
                new_alias[n] = new_canon
        add.append(entry)

    concepts = [c for c in voc["concepts"] if c["canonical_name"] not in drop]
    concepts += add
    live = {c["canonical_name"] for c in concepts}
    # a merged-away name may still be someone's parent; repoint it
    remap = {src: nc for src, _, nc, _, _ in changed}
    remap.update({dst: nc for _, dst, nc, _, _ in changed})
    for c in concepts:
        c["broader"] = sorted({remap.get(p, p) for p in c["broader"]}
                              & live - {c["canonical_name"]})
    concepts.sort(key=lambda c: (-c["episode_count"], -c["total_mentions"]))

    voc["concepts"] = concepts
    voc["canonical_count"] = len(concepts)
    (canon_dir / "alias_table.json").write_text(
        json.dumps(new_alias, indent=0, sort_keys=True))
    (canon_dir / "vocabulary.json").write_text(json.dumps(voc, indent=1))
    print(f"\ncanonical_count {len(byname)} -> {len(concepts)}")
    print("rebuild affected bundles before writing their articles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
