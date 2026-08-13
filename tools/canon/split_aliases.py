#!/usr/bin/env python3
"""Re-split alias groups that a firewall says should never have merged.

Repairs an ALREADY-BUILT canon in place. The firewall in canon_lib now blocks
these merges at build time, but re-running the whole canon to apply it costs
~2.6 h and $1.65 of adjudication to change three groups -- and adjudication is
not resumable, so a re-run also re-rolls every other verdict. This applies the
same rule to the emitted artefacts instead.

Groups are recomputed from the census rather than patched, so the split halves
get correct mention/episode/type aggregates instead of a guess at how to divide
the merged totals -- which cannot be done from the merged numbers alone.

  python3 split_aliases.py --census census/captions-v2 census/full-v2
  python3 split_aliases.py --dry-run          # report, write nothing
"""
import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from canon_lib import Corpus, Union, firewalled          # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def emit(group, corpus):
    """One vocabulary entry for a set of raw names. Mirrors build_canon's emit
    block exactly -- if that changes, this must change with it."""
    canon = sorted(group, key=lambda n: (-corpus.mentions(n), len(n), n))[0]
    e = {"mentions": 0, "episodes": set(), "types": Counter(),
         "snippets": [], "asr": 0}
    for n in group:
        d = corpus.by_name[n]
        e["mentions"] += d["mentions"]; e["episodes"] |= d["episodes"]
        e["types"] += d["types"]; e["asr"] += d["asr_suspect"]
        e["snippets"] += d["snippets"]
    ranked = e["types"].most_common()
    top_t, top_n = ranked[0]
    second = ranked[1][1] if len(ranked) > 1 else 0
    share = top_n / max(sum(e["types"].values()), 1)
    return canon, {
        "canonical_name": canon,
        "aliases": sorted(n for n in group if n != canon),
        "type": top_t,
        "type_votes": dict(e["types"]),
        "type_share": round(share, 3),
        "type_contested": share < 0.5 or (top_n - second) <= 2,
        "total_mentions": e["mentions"],
        "episode_count": len(e["episodes"]),
        "sample_snippets": e["snippets"][:3],
        "broader": [],
        "asr_suspect_mentions": e["asr"],
        "low_confidence": e["mentions"] <= 2,
    }


def main():
    ap = argparse.ArgumentParser()
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

    # canonical -> every raw name that resolves to it, including itself
    groups = defaultdict(set)
    for a, c in alias.items():
        groups[c].add(a)
    for c in groups:
        groups[c].add(c)

    # Re-partition each group with a union-find over its own members, joining
    # only pairs the firewall permits. A group splits into as many parts as the
    # firewall carves out -- which is not always two, and is why this is a
    # union-find rather than a two-way test.
    splits = []
    for canon, members in groups.items():
        members = sorted(members)
        if len(members) < 2:
            continue
        uf = Union(members)
        hit = None
        for i, a in enumerate(members):
            for b in members[i + 1:]:
                fw = firewalled(a, b)
                if fw:
                    hit = fw
                else:
                    uf.union(a, b)
        if hit is None:
            continue
        parts = [sorted(p) for p in uf.groups().values()]
        if len(parts) > 1:
            splits.append((canon, hit, parts))

    if not splits:
        print("no firewalled groups found; nothing to do")
        return 0

    corpus = Corpus(args.census)
    new_alias = dict(alias)
    added, removed = [], []
    for canon, fw, parts in splits:
        print(f"\n{canon}  [{fw}]  ->  {len(parts)} concepts")
        for p in parts:
            for n in p:
                new_alias.pop(n, None)
            new_canon, entry = emit(set(p), corpus)
            removed.append(canon)
            added.append(entry)
            for n in p:
                if n != new_canon:
                    new_alias[n] = new_canon
            print(f"   {new_canon:32} {entry['episode_count']:4} videos "
                  f"{entry['total_mentions']:5} mentions  "
                  f"aliases: {', '.join(entry['aliases']) or '-'}")

    if args.dry_run:
        print("\n--dry-run: nothing written")
        return 0

    # Replace the old merged entries with the split ones. `broader` is carried
    # over from the old entry only for the part that kept its name: a parent
    # relation was asserted about that concept, and the other part never had one.
    keep = {a["canonical_name"] for a in added}
    concepts = [c for c in voc["concepts"] if c["canonical_name"] not in set(removed)]
    for entry in added:
        old = byname.get(entry["canonical_name"])
        if old:
            entry["broader"] = old["broader"]
        concepts.append(entry)
    concepts.sort(key=lambda c: (-c["episode_count"], -c["total_mentions"]))

    # A dangling parent would break the hierarchy edges the graph draws.
    live = {c["canonical_name"] for c in concepts}
    dangling = 0
    for c in concepts:
        before = len(c["broader"])
        c["broader"] = sorted(p for p in c["broader"] if p in live)
        dangling += before - len(c["broader"])

    voc["concepts"] = concepts
    voc["canonical_count"] = len(concepts)
    (canon_dir / "alias_table.json").write_text(
        json.dumps(new_alias, indent=0, sort_keys=True))
    (canon_dir / "vocabulary.json").write_text(json.dumps(voc, indent=1))
    print(f"\n{len(removed)} groups split into {len(added)} concepts; "
          f"canonical_count {len(byname)} -> {len(concepts)}; "
          f"{dangling} dangling broader refs dropped")
    print("re-run build_graph / layout_graph / build_candidates to pick this up")
    return 0


if __name__ == "__main__":
    sys.exit(main())
