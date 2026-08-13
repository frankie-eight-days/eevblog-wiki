#!/usr/bin/env python3
"""Build site/explore.html -- the interactive concept-graph explorer.

Ported from the Amp Hour wiki's explorer, which is a canvas renderer over a flat
typed-array payload; the layout is precomputed by layout_graph.py, so the page
only draws. Template lives in tools/explore_template.html IN THIS REPO -- the
Amp Hour generator read its template out of a session scratchpad that has since
been cleaned, leaving a generator that cannot run.

Two fields the graph does not carry are computed here:

  expl  explains-depth mentions per canonical concept, from the census. Node
        cards show it because "mentioned in 200 videos" and "explained in 200
        videos" are very different claims, and only the second predicts an
        article worth writing.
  btw   betweenness, sampled. Sizes the bridge concepts -- the ones whose removal
        would disconnect clusters -- which are invisible to degree alone.

  python3 tools/build_explore.py
"""
import json
import pathlib
import random
import sys
from collections import Counter, deque

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools/explore_template.html"
OUT = ROOT / "site/explore.html"
CENSUS = [ROOT / "census/captions-v2", ROOT / "census/full-v2"]
BTW_SAMPLES = 300          # sources for sampled Brandes; 300/3961 is ~7.6%
SPAN = 10000.0             # the renderer's world square, matching its grid index


def explains_counts(alias):
    """explains-depth mentions per canonical name."""
    n = Counter()
    for d in CENSUS:
        for f in sorted(pathlib.Path(d).glob("*.json")):
            if f.name.startswith("_"):
                continue
            try:
                doc = json.loads(f.read_text())
            except json.JSONDecodeError:
                continue
            for m in doc.get("mentions", []):
                if m.get("depth") != "explains":
                    continue
                c = m.get("concept")
                if not c:
                    continue
                # census strings are raw; normalise the same way canon did, then
                # resolve through the alias table to the canonical node
                k = c.lower().strip().replace(" ", "-")
                n[alias.get(k, k)] += 1
    return n


def betweenness(N, adj, samples, seed=7):
    """Brandes, unweighted, from a random sample of sources.

    Sampling because exact is O(V*E) -- 55M operations in Python here. With 300
    sources the ranking of the top few hundred nodes is stable, which is all this
    is used for (node radius and the bridge filter), and it runs in seconds.
    """
    rnd = random.Random(seed)
    sources = rnd.sample(range(N), min(samples, N))
    bc = [0.0] * N
    for s in sources:
        stack, pred = [], [[] for _ in range(N)]
        sigma = [0.0] * N; sigma[s] = 1.0
        dist = [-1] * N; dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft(); stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = [0.0] * N
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                bc[w] += delta[w]
    scale = N / max(len(sources), 1) / ((N - 1) * (N - 2) / 2.0)
    return [b * scale for b in bc]


def main():
    layout = json.loads((ROOT / "graph/layout.json").read_text())
    graph = json.loads((ROOT / "graph/graph.json").read_text())
    alias = json.loads((ROOT / "canon/alias_table.json").read_text())

    nodes = layout["nodes"]
    N = len(nodes)
    idx = {n["i"]: k for k, n in enumerate(nodes)}

    # edge kind: layout.json drops it, graph.json has it
    kind = {}
    for e in graph["edges"]:
        a, b = idx.get(e["source"]), idx.get(e["target"])
        if a is not None and b is not None:
            kind[(min(a, b), max(a, b))] = 0 if e.get("kind") == "cooccur" else 1

    es, et, ew, ek = [], [], [], []
    adj = [[] for _ in range(N)]
    for a, b, w in layout["edges"]:
        es.append(a); et.append(b); ew.append(w)
        ek.append(kind.get((min(a, b), max(a, b)), 0))
        adj[a].append(b); adj[b].append(a)

    types = sorted({n["t"] for n in nodes})
    tix = {t: i for i, t in enumerate(types)}

    print(f"{N} nodes, {len(es)} edges; explains counts from census...",
          file=sys.stderr)
    expl = explains_counts(alias)
    print("betweenness...", file=sys.stderr)
    btw = betweenness(N, adj, BTW_SAMPLES)

    # layout is normalised to [-1,1]; the renderer indexes a 0..SPAN grid
    def sx(v):
        return round((v + 1.0) * SPAN / 2.0, 1)

    comm_members = layout.get("communities", {})
    sizes = Counter(n["c"] for n in nodes)
    comms = [{"id": int(c),
              "label3": ", ".join(m.replace("-", " ") for m in members[:3]),
              "size": sizes[int(c)]}
             for c, members in sorted(comm_members.items(),
                                      key=lambda kv: -sizes[int(kv[0])])]

    D = {
        "lbl":  [n["i"].replace("-", " ") for n in nodes],
        "type": [tix[n["t"]] for n in nodes],
        "types": types,
        "com":  [n["c"] for n in nodes],
        "ep":   [n["e"] for n in nodes],
        "men":  [n["m"] for n in nodes],
        "expl": [expl.get(n["i"], 0) for n in nodes],
        "deg":  [len(adj[i]) for i in range(N)],
        "btw":  [round(b, 6) for b in btw],
        "x":    [sx(n["x"]) for n in nodes],
        "y":    [sx(n["y"]) for n in nodes],
        "es": es, "et": et, "ew": ew, "ek": ek,
        "comms": comms,
    }

    html = TEMPLATE.read_text()
    html = html.replace("__DATA__", json.dumps(D, separators=(",", ":")))
    # no articles published for EEVblog yet, so no "read the article" links
    html = html.replace("__PUB__", "[]")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    print(f"{N} nodes, {len(es)} edges, {len(comms)} communities "
          f"-> {OUT} ({OUT.stat().st_size/1e6:.1f} MB)")
    top = sorted(range(N), key=lambda i: -D["btw"][i])[:8]
    print("top bridges: " + ", ".join(D["lbl"][i] for i in top))
    return 0


if __name__ == "__main__":
    sys.exit(main())
