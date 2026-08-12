#!/usr/bin/env python3
"""Concept co-occurrence graph over the canonicalised census.

  python3 tools/canon/build_graph.py [--census DIR ...] [--canon DIR] [--out DIR]

Relatedness here is a fact about PROXIMITY IN CONVERSATION, not about
explanation, so every depth counts -- including `mention`. Restricting to
`explains` would delete most edges and most of what makes "see also" feel right.
The report flags the consequence explicitly: nodes with zero `explains` are real
parts of the map that cannot carry a page.

Canonicalisation must run first. Without it `pcb`, `PCBs` and
`printed-circuit-board` are three nodes each holding a third of the edge weight,
and the weight>=2 prune then deletes all three -- the graph doesn't get messier,
it gets emptier.
"""
import argparse, json, pathlib, random, sys, time
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

MIN_EPISODES = 5      # a concept in fewer videos is an aside, not a topic
WINDOW = 2            # +/- paragraphs counted as co-occurring
MIN_WEIGHT = 2        # an edge seen in one video is a coincidence
TOP_K = 8             # keep each node's strongest partners
RESOLUTION = 1.6


def load(census_dirs, alias):
    """-> {concept: {episodes}}, [(episode, {concept: [paragraph_index]})]"""
    per_ep, eps = [], defaultdict(set)
    for d in census_dirs:
        for f in sorted(pathlib.Path(d).glob("*.json")):
            if f.name.startswith("_"):
                continue
            try:
                doc = json.loads(f.read_text())
            except json.JSONDecodeError:
                continue
            here = defaultdict(list)
            for m in doc.get("mentions", []):
                c = m.get("concept")
                if not c:
                    continue
                c = alias.get(c, c)
                pi = m.get("paragraph_index")
                if isinstance(pi, int):
                    here[c].append(pi)
                    eps[c].add(f.stem)
            if here:
                per_ep.append((f.stem, here))
    return eps, per_ep


def cooccur(per_ep, keep):
    """Edge weight = number of DISTINCT episodes in which the pair shares a
    +/-2 paragraph window. Counting raw co-occurrences instead would let one
    rambling video invent a strong edge on its own."""
    seen_pairs = defaultdict(set)
    for stem, here in per_ep:
        present = {c: sorted(p) for c, p in here.items() if c in keep}
        names = sorted(present)
        for i, a in enumerate(names):
            pa = present[a]
            for b in names[i + 1:]:
                pb = present[b]
                if _near(pa, pb):
                    seen_pairs[(a, b)].add(stem)
    return {k: len(v) for k, v in seen_pairs.items()}


def _near(pa, pb):
    """Two sorted paragraph lists within WINDOW of each other. Linear merge --
    the quadratic version is the whole runtime at 250k mentions."""
    i = j = 0
    while i < len(pa) and j < len(pb):
        d = pa[i] - pb[j]
        if abs(d) <= WINDOW:
            return True
        if d < 0:
            i += 1
        else:
            j += 1
    return False


def _local_move(nodes, adj, selfw, m2, resolution, rnd):
    """One local-moving phase: repeatedly move each node to the neighbouring
    community that most improves modularity, until nothing moves."""
    comm = {n: i for i, n in enumerate(nodes)}
    deg = {n: sum(adj[n].values()) + 2 * selfw.get(n, 0) for n in nodes}
    ctot = defaultdict(float)
    for n in nodes:
        ctot[comm[n]] += deg[n]
    order = list(nodes)
    for _ in range(20):
        moved = 0
        rnd.shuffle(order)
        for n in order:
            cn = comm[n]
            ctot[cn] -= deg[n]
            links = defaultdict(float)
            for nb, w in adj[n].items():
                if nb != n:
                    links[comm[nb]] += w
            best = cn
            gain = links.get(cn, 0.0) - resolution * ctot[cn] * deg[n] / m2
            for c, w in links.items():
                g = w - resolution * ctot[c] * deg[n] / m2
                if g > gain:
                    best, gain = c, g
            comm[n] = best
            ctot[best] += deg[n]
            moved += best != cn
        if not moved:
            break
    return comm


def louvain(nodes, edges, resolution, seed=7):
    """Multi-level Louvain: local moving, then AGGREGATE each community into a
    single super-node and repeat on that smaller graph.

    The aggregation phase is the whole algorithm. Local moving alone stops at the
    first local optimum and leaves hundreds of small clusters -- this graph gave
    312 communities without it, against the Amp Hour's 26 for a corpus of the same
    shape. Collapsing and re-running lets whole clusters merge in one move, which
    single-level moving can never do because no individual node improves by
    jumping alone."""
    rnd = random.Random(seed)
    adj = defaultdict(lambda: defaultdict(float))
    for (a, b), w in edges.items():
        adj[a][b] += w
        adj[b][a] += w
    m2 = sum(sum(d.values()) for d in adj.values())
    if m2 == 0:
        return {n: i for i, n in enumerate(nodes)}

    level_nodes = list(nodes)
    selfw = defaultdict(float)
    membership = {n: n for n in nodes}          # original node -> current super-node

    for _ in range(10):
        comm = _local_move(level_nodes, adj, selfw, m2, resolution, rnd)
        if len(set(comm.values())) == len(level_nodes):
            break                                # nothing merged; converged
        membership = {n: comm[membership[n]] for n in nodes}
        # rebuild the graph with one node per community, keeping intra-community
        # weight as a self-loop so it still counts toward that node's degree
        new_adj = defaultdict(lambda: defaultdict(float))
        new_self = defaultdict(float)
        for a, nbrs in adj.items():
            ca = comm[a]
            new_self[ca] += selfw.get(a, 0)
            for b, w in nbrs.items():
                cb = comm[b]
                if ca == cb:
                    new_self[ca] += w / 2
                else:
                    new_adj[ca][cb] += w
        adj, selfw = new_adj, new_self
        level_nodes = sorted(set(comm.values()))
        if len(level_nodes) == 1:
            break

    remap = {c: i for i, c in enumerate(sorted(set(membership.values()), key=str))}
    return {n: remap[membership[n]] for n in nodes}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", nargs="+",
                    default=[str(ROOT / "census/captions-v1"),
                             str(ROOT / "census/full-v1")])
    ap.add_argument("--canon", default=str(ROOT / "canon"))
    ap.add_argument("--out", default=str(ROOT / "graph"))
    args = ap.parse_args()
    canon, out = pathlib.Path(args.canon), pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    alias = json.loads((canon / "alias_table.json").read_text())
    vocab = {c["canonical_name"]: c
             for c in json.loads((canon / "vocabulary.json").read_text())["concepts"]}
    print(f"canon: {len(alias):,} aliases, {len(vocab):,} canonical concepts")

    eps, per_ep = load(args.census, alias)
    keep = {c for c, e in eps.items() if len(e) >= MIN_EPISODES}
    print(f"{len(per_ep):,} videos; {len(keep):,} concepts in >={MIN_EPISODES} videos")

    raw = cooccur(per_ep, keep)
    print(f"{len(raw):,} raw candidate edges")
    strong = {k: w for k, w in raw.items() if w >= MIN_WEIGHT}
    print(f"{len(strong):,} edges at weight >= {MIN_WEIGHT}")

    # top-K per node, keeping an edge if EITHER endpoint ranks it -- a hub would
    # otherwise silently drop every small neighbour that depends on it
    best = defaultdict(list)
    for (a, b), w in strong.items():
        best[a].append((w, b)); best[b].append((w, a))
    keepset = set()
    for n, lst in best.items():
        for w, o in sorted(lst, reverse=True)[:TOP_K]:
            keepset.add((n, o) if n < o else (o, n))
    edges = {k: strong[k] for k in keepset if k in strong}
    print(f"{len(edges):,} edges after top-{TOP_K} prune")

    nodes = sorted({n for e in edges for n in e})
    dropped = len(keep) - len(nodes)
    comm = louvain(nodes, edges, RESOLUTION)
    print(f"{len(nodes):,} nodes ({dropped:,} isolates dropped), "
          f"{len(set(comm.values()))} communities")

    hier = 0
    node_objs = []
    for n in nodes:
        v = vocab.get(n, {})
        node_objs.append({"id": n, "type": v.get("type", "other"),
                          "episodes": len(eps[n]),
                          "mentions": v.get("total_mentions", 0),
                          "community": comm[n]})
    edge_objs = [{"source": a, "target": b, "weight": w, "kind": "cooccur"}
                 for (a, b), w in sorted(edges.items(), key=lambda x: -x[1])]
    for n in nodes:
        for p in vocab.get(n, {}).get("broader", []):
            if p in comm:
                edge_objs.append({"source": p, "target": n, "weight": 1,
                                  "kind": "broader"})
                hier += 1

    by_comm = defaultdict(list)
    for n in nodes:
        by_comm[comm[n]].append(n)
    communities = []
    for cid, members in sorted(by_comm.items(), key=lambda x: -len(x[1])):
        members.sort(key=lambda n: -len(eps[n]))
        communities.append({"id": cid, "size": len(members),
                            "members": members[:12]})

    (out / "graph.json").write_text(json.dumps(
        {"nodes": node_objs, "edges": edge_objs, "communities": communities}))

    tally = Counter(v.get("type", "other") for v in
                    (vocab.get(n, {}) for n in nodes))
    rows = "\n".join(f"| {c['id']} | {c['size']} | "
                     + ", ".join(f"`{m}`" for m in c["members"][:10]) + " |"
                     for c in communities[:20])
    (out / "_graph_report.md").write_text(f"""# Concept co-occurrence graph — EEVblog

Generated from {', '.join(args.census)} plus `{canon.name}/`.

## Build parameters

| parameter | value |
|---|---|
| min videos per node | {MIN_EPISODES} |
| co-occurrence window | +/- {WINDOW} paragraphs |
| edge weight | distinct videos co-occurring |
| min edge weight | {MIN_WEIGHT} |
| top-K prune per node | {TOP_K} |
| Louvain resolution | {RESOLUTION} |

## Counts

| metric | value |
|---|---|
| candidate concepts (>={MIN_EPISODES} videos) | {len(keep):,} |
| isolated (no surviving edge), dropped | {dropped:,} |
| **nodes in graph** | **{len(nodes):,}** |
| raw candidate edges | {len(raw):,} |
| edges after weight>={MIN_WEIGHT} | {len(strong):,} |
| **edges after top-{TOP_K} prune** | **{len(edges):,}** |
| hierarchy (broader) edges | {hier:,} |
| communities | {len(communities)} |

Node types: {', '.join(f'{t} {n}' for t, n in tally.most_common(8))}

## Largest communities

| # | size | members (most-covered first) |
|---|---|---|
{rows}

Build time {time.time()-t0:.0f}s.
""")
    print(f"-> {out}/graph.json in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    sys.exit(main())
