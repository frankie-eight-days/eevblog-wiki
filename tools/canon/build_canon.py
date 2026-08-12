#!/usr/bin/env python3
"""Run the eight-stage canonicalisation over the EEVblog census.

  python3 tools/canon/build_canon.py [--census DIR ...] [--out DIR] [--no-llm]

Writes canon/alias_table.json, canon/vocabulary.json, canon/_canon_report.md.
Additive: nothing under census/ is touched.

Cost shape, from the Amp Hour run: embeddings ~$0.01, adjudication ~$0.86. The
expense is entirely in stage 8, which is why stages 5-7 exist -- every pair a
rule decides is a pair the model never sees.
"""
import argparse, json, math, pathlib, sys, time, urllib.request
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from canon_lib import (Corpus, Union, acronym_pairs, digits, rule_verdict,
                       stem_key, variant_pairs)

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
KEY = (ROOT / "tools/census/openai_key").read_text().strip()

EMBED_URL = "https://api.openai.com/v1/embeddings"
EMBED_MODEL = "text-embedding-3-small"
EMBED_BATCH = 1000
CHAT_URL = "https://api.openai.com/v1/responses"
JUDGE_MODEL = "gpt-5.6-luna"
PAIRS_PER_REQUEST = 60
COS_FLOOR = 0.80          # stage 4 recall threshold
TOP_K = 25                # neighbours kept per concept; beyond this is noise

JUDGE_PROMPT = """You are canonicalising a concept vocabulary extracted from the \
EEVblog electronics video channel. For each numbered pair, decide the relation \
between the two concept names AS AN ELECTRONICS ENGINEER WOULD USE THEM.

SAME     - the same concept under different words (pcb / printed-circuit-board;
           heatsink / heat-sink; dfm / design-for-manufacturing)
BROADER  - the FIRST is a parent category of the SECOND, or vice versa. Say which.
           (dc-dc-converter is BROADER than buck-converter)
DISTINCT - related but not interchangeable, and neither contains the other
           (analog-to-digital-converter vs digital-to-analog-converter;
            oscilloscope vs spectrum-analyzer)

Be conservative. A wrong SAME silently destroys a distinction for every reader; a
wrong DISTINCT only leaves two thin pages. When genuinely unsure, answer DISTINCT.

Different part numbers, model numbers or process nodes are ALWAYS DISTINCT.

Return ONLY a JSON array, one object per pair, no prose and no markdown fence:
[{"n":1,"v":"SAME"},{"n":2,"v":"BROADER","parent":"dc-dc-converter"},{"n":3,"v":"DISTINCT"}]
"""


def post(url, payload, timeout=300):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": f"Bearer {KEY}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def embed(names, log):
    """Stage 4a. ~$0.01 for 66k strings, so there is no reason to be clever here."""
    vecs, t0 = [], time.time()
    for i in range(0, len(names), EMBED_BATCH):
        chunk = [n.replace("-", " ") for n in names[i:i + EMBED_BATCH]]
        for attempt in range(4):
            try:
                d = post(EMBED_URL, {"model": EMBED_MODEL, "input": chunk})
                vecs.extend(e["embedding"] for e in d["data"])
                break
            except Exception as exc:                            # noqa: BLE001
                if attempt == 3:
                    raise
                log(f"  embed retry {attempt+1}: {str(exc)[-80:]}")
                time.sleep(3 * (attempt + 1))
        if (i // EMBED_BATCH) % 10 == 0:
            log(f"  embedded {min(i+EMBED_BATCH, len(names)):,}/{len(names):,}")
    a = np.asarray(vecs, dtype=np.float32)
    a /= np.linalg.norm(a, axis=1, keepdims=True) + 1e-9
    log(f"  {a.shape[0]:,} vectors in {time.time()-t0:.0f}s")
    return a


def neighbours(mat, names, log, block=1024):
    """Stage 4b: all-pairs cosine, blocked so the full N x N never exists.

    At 40k concepts the dense matrix would be 6 GB; in 1024-row strips it is
    160 MB and the whole sweep takes a couple of minutes."""
    pairs, n = {}, len(names)
    # numpy 2.0 on macOS Accelerate raises divide-by-zero/overflow/invalid on every
    # large float32 matmul, including on random well-formed input. Verified
    # spurious: the outputs are finite and in [-1, 1]. Suppressed so a real NaN
    # would still be visible in the candidate counts rather than buried in noise.
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        return _sweep(mat, names, log, block, pairs, n)


def _sweep(mat, names, log, block, pairs, n):
    for start in range(0, n, block):
        sims = mat[start:start + block] @ mat.T
        if not np.isfinite(sims).all():
            raise RuntimeError(f"non-finite similarity block at row {start}")
        for r in range(sims.shape[0]):
            i = start + r
            row = sims[r]
            row[i] = -1.0                              # never pair with self
            idx = np.argpartition(row, -TOP_K)[-TOP_K:]
            for j in idx:
                if row[j] >= COS_FLOOR:
                    a, b = (i, int(j)) if i < j else (int(j), i)
                    if a != b:
                        pairs[(names[a], names[b])] = float(row[j])
        if (start // block) % 8 == 0:
            log(f"  cosine {min(start+block, n):,}/{n:,} -> {len(pairs):,} candidates")
    return pairs


def adjudicate(pairs, corpus, log):
    """Stage 8. 60 pairs per request; the model only sees what rules could not
    decide."""
    out, batches = {}, [pairs[i:i + PAIRS_PER_REQUEST]
                        for i in range(0, len(pairs), PAIRS_PER_REQUEST)]
    tin = tout = 0
    for bi, batch in enumerate(batches):
        lines = []
        for n, (a, b) in enumerate(batch, 1):
            lines.append(f"{n}. {a} [{corpus.type_of(a)}, {corpus.mentions(a)}] "
                         f"<-> {b} [{corpus.type_of(b)}, {corpus.mentions(b)}]")
        payload = {"model": JUDGE_MODEL,
                   "input": JUDGE_PROMPT + "\n\n" + "\n".join(lines),
                   "reasoning": {"effort": "low"}, "max_output_tokens": 8000}
        text = None
        for attempt in range(3):
            try:
                d = post(CHAT_URL, payload)
                u = d.get("usage") or {}
                tin += u.get("input_tokens", 0); tout += u.get("output_tokens", 0)
                for item in d.get("output", []):
                    for c in item.get("content", []) or []:
                        if c.get("type") == "output_text":
                            text = c["text"]
                if text:
                    break
            except Exception as exc:                            # noqa: BLE001
                log(f"  judge retry {attempt+1}: {str(exc)[-80:]}")
                time.sleep(4 * (attempt + 1))
        if not text:
            continue
        s = text.strip()
        s = s[s.find("["):s.rfind("]") + 1] if "[" in s else s
        try:
            verdicts = json.loads(s)
        except json.JSONDecodeError:
            log(f"  batch {bi}: unparseable verdict block, skipped")
            continue
        for v in verdicts:
            try:
                a, b = batch[int(v["n"]) - 1]
            except (KeyError, ValueError, IndexError):
                continue
            out[(a, b)] = (v.get("v"), v.get("parent"))
        if bi % 25 == 0:
            log(f"  adjudicated {min((bi+1)*PAIRS_PER_REQUEST, len(pairs)):,}/{len(pairs):,}")
    cost = tin * 0.20 / 1e6 + tout * 1.20 / 1e6
    log(f"  judge tokens in {tin:,} out {tout:,} -> ${cost:.2f}")
    return out, cost


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", nargs="+",
                    default=[str(ROOT / "census/captions-v2"),
                             str(ROOT / "census/full-v1")])
    ap.add_argument("--out", default=str(ROOT / "canon"))
    ap.add_argument("--no-llm", action="store_true",
                    help="rules + embeddings only; skip stage 8")
    args = ap.parse_args()
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    logf = open(out / "_canon_run.log", "a")

    def log(*a):
        line = " ".join(str(x) for x in a)
        print(line, flush=True); logf.write(line + "\n"); logf.flush()

    t0 = time.time()
    log(f"\n=== canon run {time.strftime('%Y-%m-%d %H:%M')} ===")
    log("stage 1-2: load + hygiene + normalise")
    corpus = Corpus(args.census)
    names = sorted(corpus.names())
    total_mentions = sum(corpus.mentions(n) for n in names)
    log(f"  {corpus.episodes:,} episodes, {total_mentions:,} mentions, "
        f"{len(names):,} raw distinct concepts, {len(corpus.fixes)} hygiene fixes")

    log("stage 3: plural / hyphen / spacing variants")
    var = variant_pairs(names)
    log(f"  {len(var):,} deterministic variant pairs")

    log("stage 7: acronym recall")
    acro, acro_rejected = acronym_pairs(corpus)
    log(f"  {len(acro):,} acronym pairs, {len(acro_rejected)} homonym expansions rejected")

    log("stage 4: embeddings")
    mat = embed(names, log)
    cand = neighbours(mat, names, log)
    log(f"  {len(cand):,} candidate pairs at cosine >= {COS_FLOOR}")

    log("stage 5-6: rules")
    decided, undecided = {}, []
    for (a, b) in var:
        decided[(a, b)] = "SAME"
    # Acronym pairs are CANDIDATES, not merges. Auto-merging them collapsed `hp`
    # into `hackaday-prize` because that outscored `hewlett-packard` in a sample;
    # initials matching is good recall and bad evidence, so it feeds stage 8.
    for pair in acro:
        if pair not in decided:
            undecided.append(pair)
    auto = rejected = 0
    for (a, b), cos in cand.items():
        if (a, b) in decided or (a, b) in acro:
            continue
        v = rule_verdict(a, b, corpus, cos)
        if v == "SAME":
            decided[(a, b)] = "SAME"; auto += 1
        elif v == "DISTINCT":
            rejected += 1
        else:
            undecided.append((a, b))
    log(f"  {auto:,} rule auto-merge, {rejected:,} rule reject, "
        f"{len(undecided):,} to adjudicate")

    broader, cost = [], 0.0
    if undecided and not args.no_llm:
        log("stage 8: adjudication")
        verdicts, cost = adjudicate(undecided, corpus, log)
        tally = Counter(v for v, _ in verdicts.values())
        log(f"  {dict(tally)}")
        for (a, b), (v, parent) in verdicts.items():
            if v == "SAME":
                decided[(a, b)] = "SAME"
            elif v == "BROADER":
                child = b if parent == a else a
                broader.append({"parent": parent or a, "child": child})
    elif args.no_llm:
        log("stage 8: SKIPPED (--no-llm)")

    log("merge + emit")
    uf = Union(names)
    for (a, b), v in decided.items():
        if v == "SAME":
            uf.union(a, b)

    alias, vocab = {}, []
    for group in uf.groups().values():
        # canonical = most-mentioned; ties break on the shorter, then alphabetical,
        # so `pcb` never wins over `printed-circuit-board` on a coin flip
        canon = sorted(group, key=lambda n: (-corpus.mentions(n), len(n), n))[0]
        e = {"mentions": 0, "episodes": set(), "types": Counter(),
             "snippets": [], "asr": 0}
        for n in group:
            d = corpus.by_name[n]
            e["mentions"] += d["mentions"]; e["episodes"] |= d["episodes"]
            e["types"] += d["types"]; e["asr"] += d["asr_suspect"]
            e["snippets"] += d["snippets"]
            if n != canon:
                alias[n] = canon
        vocab.append({
            "canonical_name": canon,
            "aliases": sorted(n for n in group if n != canon),
            "type": e["types"].most_common(1)[0][0],
            "type_votes": dict(e["types"]),
            "total_mentions": e["mentions"],
            "episode_count": len(e["episodes"]),
            "sample_snippets": e["snippets"][:3],
            "broader": [],
            "asr_suspect_mentions": e["asr"],
            "low_confidence": e["mentions"] <= 2,
        })
    vocab.sort(key=lambda c: (-c["episode_count"], -c["total_mentions"]))
    byname = {c["canonical_name"]: c for c in vocab}
    for rel in broader:
        p = alias.get(rel["parent"], rel["parent"])
        c = alias.get(rel["child"], rel["child"])
        if p != c and c in byname and p in byname:
            byname[c]["broader"].append(p)
    for c in vocab:
        c["broader"] = sorted(set(c["broader"]))

    (out / "alias_table.json").write_text(json.dumps(alias, indent=0, sort_keys=True))
    (out / "vocabulary.json").write_text(json.dumps({
        "generated_from": args.census, "raw_distinct": len(names),
        "canonical_count": len(vocab), "total_mentions": total_mentions,
        "concepts": vocab}, indent=1))
    (out / "_hygiene_fixes.json").write_text(json.dumps(corpus.fixes, indent=1))
    (out / "_acronym_rejects.json").write_text(json.dumps(acro_rejected, indent=1))

    big = [c for c in vocab if len(c["aliases"]) >= 3][:40]
    rows = "\n".join(
        f"| `{c['canonical_name']}` | {c['type']} | {c['episode_count']} | "
        f"{c['total_mentions']} | {len(c['aliases'])} | "
        + ", ".join(f"`{a}`" for a in c["aliases"][:6]) + " |" for c in big)
    (out / "_canon_report.md").write_text(f"""# Canonicalisation report — EEVblog concept census

Source: {', '.join(args.census)} ({corpus.episodes:,} videos, {total_mentions:,} mentions).
Additive layer; no census file was modified.

## Headline

| metric | value |
|---|---|
| raw distinct concept strings | {len(names):,} |
| canonical concepts | {len(vocab):,} |
| compression | {(1-len(vocab)/max(len(names),1))*100:.1f}% fewer entries |
| total mentions (unchanged) | {total_mentions:,} |
| concepts in >=10 videos | {sum(1 for c in vocab if c['episode_count']>=10):,} |
| singletons (1 mention, no alias) | {sum(1 for c in vocab if c['total_mentions']==1 and not c['aliases']):,} |
| `broader` relations recorded | {sum(len(c['broader']) for c in vocab):,} |

## Stages

| stage | method | result |
|---|---|---|
| 1 hygiene | junk `type` remapped to the canonical 16; leaked `depth` reset | {len(corpus.fixes)} fixes |
| 2 normalise | case / unicode / punctuation / whitespace fold | folded into stage 3 |
| 3 variants | plural + hyphen + spacing, only when both forms observed | {len(var):,} pairs |
| 4 embeddings | `{EMBED_MODEL}`, cosine >= {COS_FLOOR}, top-{TOP_K} neighbours | {len(cand):,} candidates |
| 5 rule merge | identical stemmed token sequence + compatible type | {auto:,} pairs |
| 6 rule reject | differing digit signature, or both-singleton below 0.86 | {rejected:,} pairs |
| 7 acronym | deterministic initials match (embeddings are blind to these) | {len(acro):,} pairs |
| 8 adjudication | `{JUDGE_MODEL}`, effort low, {PAIRS_PER_REQUEST}/request | {len(undecided):,} pairs, ${cost:.2f} |

An acronym gets exactly one expansion: the highest-mention one, plus spelling
variants of it. {len(acro_rejected)} homonym expansions were rejected this way
(full list in `_acronym_rejects.json`).

## Biggest merge clusters

| canonical | type | videos | mentions | aliases | sample |
|---|---|---|---|---|---|
{rows}

Run time {time.time()-t0:.0f}s.
""")
    log(f"DONE: {len(names):,} -> {len(vocab):,} canonical "
        f"({(1-len(vocab)/max(len(names),1))*100:.1f}% compression), "
        f"${cost:.2f}, {time.time()-t0:.0f}s")


if __name__ == "__main__":
    sys.exit(main())
