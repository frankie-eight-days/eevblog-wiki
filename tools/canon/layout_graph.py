#!/usr/bin/env python3
"""Pre-compute a force-directed layout for the concept graph.

The layout runs HERE, not in the browser. A 4k-node simulation in JS takes
seconds to settle, jitters while it does, and gives a different picture on every
load; solving it once means the page just draws coordinates, and the same graph
always looks the same -- which matters when you are trying to describe a region
of it to someone else.

Fruchterman-Reingold with a community-aware seed: nodes start near their
community's slot on a circle rather than at random, so the big clusters do not
have to fight their way past each other and the result is readable in ~250
iterations instead of thousands.
"""
import json, math, pathlib, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
ITERS = 260
SEED = 11


def main():
    g = json.loads((ROOT / "graph/graph.json").read_text())
    nodes = g["nodes"]
    idx = {n["id"]: i for i, n in enumerate(nodes)}
    N = len(nodes)

    edges = [(idx[e["source"]], idx[e["target"]], e["weight"])
             for e in g["edges"]
             if e["source"] in idx and e["target"] in idx and e["kind"] == "cooccur"]
    src = np.array([e[0] for e in edges])
    dst = np.array([e[1] for e in edges])
    w = np.array([e[2] for e in edges], dtype=np.float32)
    w = 1.0 + np.log1p(w)                      # damp the 90-weight hubs

    rng = np.random.default_rng(SEED)
    comms = sorted({n["community"] for n in nodes})
    size = {c: sum(1 for n in nodes if n["community"] == c) for c in comms}
    order = sorted(comms, key=lambda c: -size[c])
    slot = {c: i for i, c in enumerate(order)}
    R = math.sqrt(N) * 1.6

    pos = np.zeros((N, 2), dtype=np.float32)
    for i, n in enumerate(nodes):
        a = 2 * math.pi * slot[n["community"]] / len(comms)
        r = R * (0.35 + 0.65 * (slot[n["community"]] / len(comms)) ** 0.5)
        pos[i] = (r * math.cos(a) + rng.normal(0, R * 0.06),
                  r * math.sin(a) + rng.normal(0, R * 0.06))

    # LinLog attraction (log of distance) rather than Fruchterman-Reingold's d^2.
    # FR's quadratic attraction grows without bound, so with 14k edges -- many of
    # them weight-90 hub links -- every cluster is dragged into one blob; the first
    # attempt at this produced a single unreadable hairball. Under LinLog the pull
    # flattens with distance, so clusters settle apart and the community structure
    # is actually visible, which is the entire point of drawing this.
    #
    # Degree-scaled repulsion (ForceAtlas2's trick) does the rest: a hub with 200
    # edges pushes proportionally harder, so it claims space instead of being
    # buried under its own neighbours.
    deg = np.ones(N, dtype=np.float32)
    np.add.at(deg, src, 1.0)
    np.add.at(deg, dst, 1.0)
    k = 2.4
    temp = R * 0.10
    wn = w / w.mean()                            # weights around 1, not 5

    for it in range(ITERS):
        disp = np.zeros_like(pos)
        # all-pairs repulsion; 4k^2 is 16M float ops, ~0.15s/iteration in numpy,
        # cheaper than writing a quadtree for a one-off script
        d = pos[:, None, :] - pos[None, :, :]
        dist = np.sqrt((d ** 2).sum(-1)) + 0.01
        np.fill_diagonal(dist, np.inf)
        rep = (k * deg[:, None] * deg[None, :]) / dist
        disp += (d / dist[:, :, None] * rep[:, :, None]).sum(1)
        # LinLog attraction
        dv = pos[src] - pos[dst]
        dl = np.sqrt((dv ** 2).sum(-1)) + 1e-6
        f = (np.log1p(dl) * wn * 6.0)[:, None] * (dv / dl[:, None])
        np.add.at(disp, src, -f)
        np.add.at(disp, dst, f)
        # very weak centring, only enough to stop disconnected clusters drifting
        disp -= pos * 0.0015

        dl = np.sqrt((disp ** 2).sum(-1))[:, None] + 1e-9
        pos += (disp / dl) * np.minimum(dl, temp)
        temp *= 0.988
        if it % 60 == 0:
            print(f"  iter {it}/{ITERS}", file=sys.stderr)

    pos -= pos.mean(0)
    pos /= np.abs(pos).max()                    # normalise to [-1, 1]

    out = {
        "nodes": [{"i": n["id"], "x": round(float(pos[i, 0]), 4),
                   "y": round(float(pos[i, 1]), 4), "c": n["community"],
                   "t": n["type"], "e": n["episodes"], "m": n["mentions"]}
                  for i, n in enumerate(nodes)],
        "edges": [[int(a), int(b), int(ww)] for a, b, ww in edges],
        "communities": {str(c["id"]): c["members"][:6] for c in g["communities"]},
    }
    dest = ROOT / "graph/layout.json"
    dest.write_text(json.dumps(out, separators=(",", ":")))
    print(f"{N} nodes, {len(edges)} edges -> {dest} ({dest.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    sys.exit(main())
