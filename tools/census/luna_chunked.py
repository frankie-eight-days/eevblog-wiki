"""Luna chunked-extraction arm (v3) + one whole-episode medium-effort control.

Chunked arm: one Responses API request per chunk (census_prompt_v3_chunk.md +
the chunk text from chunker.py), reasoning effort "low", 16k output cap. The
per-chunk JSON objects are merged per episode:

  * chunk 0 supplies the header block; later chunks supply mentions only.
  * a (concept, paragraph_index) pair re-emitted by the next chunk for a
    paragraph the two chunks SHARE is dropped as an overlap duplicate. Duplicates
    inside one chunk are left alone -- they are a real quality signal and the
    scorer counts them.
  * char_start is computed here, not asked of the model: the snippet must occur
    verbatim inside the span of the paragraph it names. A mention whose snippet
    is not found there is rejected and counted (-> luna_chunked_rejected.json).

Control: whole-episode 0212 with the ORIGINAL census_prompt_v2.md at reasoning
effort "medium". This isolates "did chunking help" from "did more thinking
help" for luna's earlier whole-episode failure. It does NOT go in the bake-off
directories.

The HTTP plumbing (streaming, fence-tolerant JSON parse) is openai_extract.py's,
imported rather than copied so the two arms cannot drift.
"""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = os.path.dirname(os.path.abspath(__file__))
WIKI = "/Users/frankwalsh/Documents/vibecoding/eevblog_wiki"
RESEARCH = os.path.join(WIKI, "research")
TRANSCRIPTS = os.environ.get("EEV_TRANSCRIPTS", os.path.join(WIKI, "transcripts"))
BAKEOFF = os.path.join(RESEARCH, "bakeoff")
OUTDIR = os.path.join(BAKEOFF, "luna-chunked")
CHUNKS = os.path.join(SCRATCH, "chunks")

sys.path.insert(0, SCRATCH)
sys.path.insert(0, RESEARCH)
import census_lib as cl  # noqa: E402
import openai_extract as oe  # noqa: E402
from chunker import CHUNK_SIZE, OVERLAP, STEMS, chunk_ranges  # noqa: E402

MODEL = "gpt-5.6-luna"
CHUNK_PROMPT = os.path.join(RESEARCH, "census_prompt_v3_chunk.md")
V2_PROMPT = os.path.join(RESEARCH, "census_prompt_v2.md")
CHUNK_MAX_TOKENS = 16000
HEADER_KEYS = ("episode", "title", "url", "file", "main_topics",
               "guest_name", "guest_affiliation", "notes")

log = oe.log


def request(key, content, max_tokens, effort):
    """oe.stream_request with a per-call reasoning effort (thread-safe)."""
    return oe.stream_request(key, MODEL, content, max_tokens, effort=effort)


# ------------------------------------------------------------------ chunk run


def run_chunk(key, stem, ci, prompt):
    path = os.path.join(CHUNKS, stem, "%02d.txt" % ci)
    with open(path, encoding="utf-8") as fh:
        chunk = fh.read()
    content = prompt + chunk
    t0 = time.time()
    rec = {"stem": stem, "chunk": ci}
    for attempt in (1, 2):
        body = content if attempt == 1 else content + "\n\n" + oe.RETRY_NOTE
        http, text, usage, stop = request(key, body, CHUNK_MAX_TOKENS, "low")
        obj, pstatus = oe.parse_json(text) if http == 200 else (None, "http %s" % http)
        det = usage.get("output_tokens_details") or {}
        rec.update({
            "attempt": attempt, "http": http, "status": stop, "parse": pstatus,
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "reasoning_tokens": det.get("reasoning_tokens"),
            "seconds": round(time.time() - t0, 1),
            "mentions": len(obj.get("mentions") or []) if isinstance(obj, dict) else 0,
        })
        log("[%s c%02d] att%d HTTP %s out=%s (reason=%s) status=%s parse=%s mentions=%d (%.0fs)"
            % (stem[:26], ci, attempt, http, rec["output_tokens"], rec["reasoning_tokens"],
               stop, pstatus, rec["mentions"], rec["seconds"]))
        if http != 200:
            log("[%s c%02d]   error: %s" % (stem[:26], ci, (text or "")[:300]))
        if obj is not None:
            rec["ok"] = True
            return rec, obj
        with open(os.path.join(SCRATCH, "luna_chunk_raw_%s_%02d.txt" % (stem, ci)), "w",
                  encoding="utf-8") as fh:
            fh.write(text or "")
    rec["ok"] = False
    return rec, None


# --------------------------------------------------------------------- merge


def merge(stem, objs, rngs):
    """-> (census, stats, rejected). objs[ci] may be None for a failed chunk."""
    tr = cl.parse_transcript(os.path.join(TRANSCRIPTS, stem + ".md"))
    npara = len(tr.paragraphs)

    census = {}
    if objs and isinstance(objs[0], dict):
        for k in HEADER_KEYS:
            if k in objs[0]:
                census[k] = objs[0][k]
    census.setdefault("file", stem + ".md")

    mentions, rejected = [], []
    stats = {"raw": 0, "overlap_dupes_dropped": 0, "snippet_not_found": 0,
             "bad_paragraph_index": 0, "malformed": 0, "kept": 0,
             "header_on_later_chunk": 0, "failed_chunks": []}
    prev_pairs = set()   # (concept, pidx) emitted by the previous chunk
    prev_hi = -1         # exclusive end of the previous chunk's paragraph range

    for ci, obj in enumerate(objs):
        lo, hi = rngs[ci]
        if obj is None:
            stats["failed_chunks"].append(ci)
            prev_pairs, prev_hi = set(), hi
            continue
        if ci > 0 and any(k in obj for k in ("main_topics", "guest_name", "notes")):
            stats["header_on_later_chunk"] += 1
        this_pairs = set()
        ms = obj.get("mentions")
        for m in (ms if isinstance(ms, list) else []):
            if not isinstance(m, dict):
                stats["malformed"] += 1
                continue
            stats["raw"] += 1
            m = dict(m)
            m["_chunk"] = ci
            pidx, snip = m.get("paragraph_index"), m.get("context_snippet")
            concept = m.get("concept")
            if (not isinstance(pidx, int) or isinstance(pidx, bool)
                    or not 0 <= pidx < npara):
                stats["bad_paragraph_index"] += 1
                m["_reject"] = "bad-paragraph-index"
                rejected.append(m)
                continue
            key = (concept, pidx)
            # overlap duplicate: same pair, in a paragraph both chunks saw
            if key in prev_pairs and lo <= pidx < prev_hi:
                stats["overlap_dupes_dropped"] += 1
                continue
            this_pairs.add(key)
            if not isinstance(snip, str) or not snip:
                stats["snippet_not_found"] += 1
                m["_reject"] = "no-snippet"
                rejected.append(m)
                continue
            p = tr.paragraphs[pidx]
            pos = cl._find_in_span(tr.body, snip, p.start, p.end)
            if pos == -1:
                stats["snippet_not_found"] += 1
                m["_reject"] = "snippet-not-in-stated-paragraph"
                rejected.append(m)
                continue
            out = {"concept": concept, "type": m.get("type"), "speaker": m.get("speaker"),
                   "paragraph_index": pidx, "char_start": pos, "depth": m.get("depth"),
                   "context_snippet": snip}
            if m.get("asr_suspect") is not None:
                out["asr_suspect"] = m.get("asr_suspect")
            mentions.append(out)
        prev_pairs, prev_hi = this_pairs, hi

    mentions.sort(key=lambda m: (m["paragraph_index"], m["char_start"]))
    stats["kept"] = len(mentions)
    census["mentions"] = mentions
    # header defaults so the schema matches the other arms
    for k in HEADER_KEYS:
        census.setdefault(k, None)
    census = {**{k: census[k] for k in HEADER_KEYS}, "mentions": mentions}
    return census, stats, rejected


# ------------------------------------------------------------------- control


def run_control(key):
    stem = "0212-an-interview-with-trey-german-launchpad-laden-lodesman"
    with open(V2_PROMPT, encoding="utf-8") as fh:
        prompt = fh.read()
    with open(os.path.join(TRANSCRIPTS, stem + ".md"), encoding="utf-8") as fh:
        prompt += fh.read()
    t0 = time.time()
    http, text, usage, stop = request(key, prompt, 64000, "medium")
    obj, pstatus = oe.parse_json(text) if http == 200 else (None, "http %s" % http)
    det = usage.get("output_tokens_details") or {}
    n = len(obj.get("mentions") or []) if isinstance(obj, dict) else 0
    rec = {"control": "luna whole-episode 0212, v2 prompt, effort=medium",
           "http": http, "status": stop, "parse": pstatus,
           "input_tokens": usage.get("input_tokens"),
           "output_tokens": usage.get("output_tokens"),
           "reasoning_tokens": det.get("reasoning_tokens"),
           "mentions": n, "seconds": round(time.time() - t0, 1)}
    log("[CONTROL] %s" % json.dumps(rec))
    path = os.path.join(SCRATCH, "luna_medium_control_0212.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj if obj is not None else {"error": text[:4000], "_meta": rec},
                  fh, indent=1, ensure_ascii=False)
    return rec


# ---------------------------------------------------------------------- main


def main():
    key = oe.api_key()
    with open(CHUNK_PROMPT, encoding="utf-8") as fh:
        prompt = fh.read()

    plans = {}
    for stem in STEMS:
        tr = cl.parse_transcript(os.path.join(TRANSCRIPTS, stem + ".md"))
        plans[stem] = chunk_ranges(len(tr.paragraphs), CHUNK_SIZE, OVERLAP)

    jobs = [(stem, ci) for stem in STEMS for ci in range(len(plans[stem]))]
    log("chunk jobs: %d  (%s)" % (len(jobs), {s: len(r) for s, r in plans.items()}))

    with ThreadPoolExecutor(max_workers=6) as ex:
        fut_control = ex.submit(run_control, key)
        results = list(ex.map(lambda j: run_chunk(key, j[0], j[1], prompt), jobs))
        control = fut_control.result()

    by_stem = {s: [None] * len(plans[s]) for s in STEMS}
    recs = []
    for (stem, ci), (rec, obj) in zip(jobs, results):
        by_stem[stem][ci] = obj
        recs.append(rec)

    os.makedirs(OUTDIR, exist_ok=True)
    summary = {"control": control, "chunks": recs, "episodes": {}}
    for stem in STEMS:
        census, stats, rejected = merge(stem, by_stem[stem], plans[stem])
        with open(os.path.join(OUTDIR, stem + ".json"), "w", encoding="utf-8") as fh:
            json.dump(census, fh, indent=1, ensure_ascii=False)
        with open(os.path.join(SCRATCH, "luna_chunked_rejected_%s.json" % stem), "w",
                  encoding="utf-8") as fh:
            json.dump(rejected, fh, indent=1, ensure_ascii=False)
        summary["episodes"][stem] = stats
        log("\n%s: %s" % (stem, json.dumps(stats)))

    with open(os.path.join(SCRATCH, "luna_chunked_run_log.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
