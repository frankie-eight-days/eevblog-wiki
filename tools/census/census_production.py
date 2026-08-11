"""Full-corpus concept census: gpt-5.6-luna, chunked v3 pipeline.

Runs the bake-off-winning arm over every Amp Hour transcript. One Responses API
request per 40-paragraph chunk (census_prompt_v3_chunk.md), reasoning effort
"low", 16k output cap, merged per episode with the bake-off's merge() so the
production censuses are schema-identical to the bake-off outputs.

  -> census/luna-v3/<stem>.json          one census per episode
  -> census/luna-v3/_manifest.json       per-episode + run-level stats

Resume: an episode whose output file already exists and parses is skipped, so
the script can be re-run after an interruption without re-spending.

Retries per chunk: up to 2 after the first attempt. Transient failures (non-200,
socket drops) back off; parse failures re-ask for compact JSON. A chunk that
returns zero mentions while covering more than 10 paragraphs gets one extra
attempt on top of that; if it is still empty it is recorded as suspect-sparse
rather than retried forever.
"""
from __future__ import annotations

import json
import os
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = os.path.dirname(os.path.abspath(__file__))
WIKI = "/Users/frankwalsh/Documents/vibecoding/eevblog_wiki"
RESEARCH = SCRATCH
TRANSCRIPTS = os.environ.get("EEV_TRANSCRIPTS", os.path.join(WIKI, "transcripts"))
OUTDIR = os.environ.get("EEV_OUTDIR", os.path.join(WIKI, "census", "sample"))
MANIFEST = os.path.join(OUTDIR, "_manifest.json")

sys.path.insert(0, SCRATCH)
sys.path.insert(0, RESEARCH)
import census_lib as cl  # noqa: E402
import openai_extract as oe  # noqa: E402
from chunker import CHUNK_SIZE, OVERLAP, chunk_ranges, render  # noqa: E402
from luna_chunked import HEADER_KEYS, merge  # noqa: E402

MODEL = "gpt-5.6-luna"
EFFORT = "low"
# A 16k-token chunk call answers in ~11s. openai_extract's 1800s default lets a
# silently stalled stream park a worker for half an hour; cap it far lower so a
# dead connection becomes a fast retry instead of a stall.
oe.TIMEOUT = 240
CHUNK_MAX_TOKENS = 16000
CHUNK_PROMPT = os.path.join(RESEARCH, "census_prompt_v3_chunk.md")
CONCURRENCY = 100
MAX_ATTEMPTS = 3          # first try + 2 retries
SPARSE_MIN_PARAS = 10     # a chunk bigger than this must not come back empty
PRICE_IN = 0.20 / 1e6
PRICE_OUT = 1.20 / 1e6

# research/speaker_label_audit.md section 5: byte-identical re-air duplicates.
SKIP_FILES = {
    "theamphour-117-undulating-utensil-utility.md",
    "0241-an-interview-with-chuck-peddle-re-air.md",
}

_logfile = open(os.path.join(SCRATCH, "census_production.log"), "a", encoding="utf-8")


def log(*a):
    line = " ".join(str(x) for x in a)
    with _stats_lock_print:
        print(line, flush=True)
        _logfile.write(line + "\n")
        _logfile.flush()


_stats_lock_print = threading.Lock()

_stats_lock = threading.Lock()
TOTALS = {"requests": 0, "retries": 0, "input_tokens": 0, "output_tokens": 0,
          "reasoning_tokens": 0, "http_errors": 0, "parse_failures": 0,
          "sparse_retries": 0, "chunks_done": 0}
ABORT = threading.Event()
ABORT_REASON = []
_fail_streak = [0]


def bump(**kw):
    with _stats_lock:
        for k, v in kw.items():
            TOTALS[k] = TOTALS.get(k, 0) + v


def abort(reason):
    if not ABORT.is_set():
        ABORT_REASON.append(reason)
        ABORT.set()
        log("!!! ABORTING RUN: %s" % reason)


# ----------------------------------------------------------------- chunk call


def safe_request(key, content):
    """oe.stream_request that cannot raise.

    stream_request only catches urllib's HTTPError/URLError. http.client
    exceptions such as RemoteDisconnected are neither, so they escape the worker
    thread and resurface from Future.result() in the main thread -- which is
    what killed the first production run. Anything unexpected becomes a
    retryable pseudo-status here instead.
    """
    try:
        return oe.stream_request(key, MODEL, content, CHUNK_MAX_TOKENS, effort=EFFORT)
    except Exception as e:  # noqa: BLE001 - any transport failure is retryable
        return 0, "%s: %s" % (type(e).__name__, e), {}, "exception"


def run_chunk(key, stem, ci, chunk_text, prompt, n_paras):
    """-> (rec, obj|None). Never raises; a dead chunk comes back with obj None."""
    base = prompt + chunk_text
    rec = {"stem": stem, "chunk": ci, "attempts": 0, "retries": 0,
           "input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0,
           "sparse_retry": False, "ok": False}
    t0 = time.time()
    obj = None
    attempt = 0
    budget = MAX_ATTEMPTS
    sparse_used = False

    while attempt < budget:
        if ABORT.is_set():
            rec["error"] = "aborted before attempt %d" % (attempt + 1)
            break
        attempt += 1
        rec["attempts"] = attempt
        if attempt > 1:
            rec["retries"] += 1
            bump(retries=1)
        content = base if attempt == 1 else base + "\n\n" + oe.RETRY_NOTE
        bump(requests=1)
        http, text, usage, stop = safe_request(key, content)
        det = usage.get("output_tokens_details") or {}
        it = usage.get("input_tokens") or 0
        ot = usage.get("output_tokens") or 0
        rt = det.get("reasoning_tokens") or 0
        rec["input_tokens"] += it
        rec["output_tokens"] += ot
        rec["reasoning_tokens"] += rt
        bump(input_tokens=it, output_tokens=ot, reasoning_tokens=rt)
        rec["http"], rec["status"] = http, stop

        if http in (401, 403):
            abort("HTTP %s from the API (auth); body: %s" % (http, (text or "")[:200]))
            rec["error"] = "auth"
            break
        if http != 200:
            bump(http_errors=1)
            rec["parse"] = "http %s" % http
            log("[%s c%02d] att%d HTTP %s: %s"
                % (stem[:34], ci, attempt, http, (text or "")[:160]))
            if attempt < budget:
                time.sleep(min(30, 3 * 2 ** (attempt - 1)) + random.random() * 3)
            continue

        obj, pstatus = oe.parse_json(text)
        rec["parse"] = pstatus
        if obj is None or not isinstance(obj, dict):
            obj = None
            bump(parse_failures=1)
            log("[%s c%02d] att%d parse=%s status=%s out=%d"
                % (stem[:34], ci, attempt, pstatus, stop, ot))
            continue

        n = len(obj.get("mentions") or [])
        rec["mentions"] = n
        # yield check: a substantial chunk must not come back empty
        if n == 0 and n_paras > SPARSE_MIN_PARAS and not sparse_used:
            sparse_used = True
            rec["sparse_retry"] = True
            budget += 1
            bump(sparse_retries=1)
            log("[%s c%02d] empty chunk over %d paragraphs; one extra attempt"
                % (stem[:34], ci, n_paras))
            obj = None
            continue
        rec["ok"] = True
        break

    rec["seconds"] = round(time.time() - t0, 1)
    if rec["ok"]:
        rec["suspect_sparse"] = bool(sparse_used and not rec.get("mentions"))
        with _stats_lock:
            _fail_streak[0] = 0
    else:
        rec["suspect_sparse"] = False
        with _stats_lock:
            _fail_streak[0] += 1
            streak = _fail_streak[0]
        if streak >= 40:
            abort("%d chunks in a row exhausted their retries" % streak)
    with _stats_lock:
        TOTALS["chunks_done"] += 1
        done = TOTALS["chunks_done"]
    if done % 250 == 0:
        log("--- progress: %d chunks done, in=%dk out=%dk, $%.2f so far ---"
            % (done, TOTALS["input_tokens"] // 1000, TOTALS["output_tokens"] // 1000,
               TOTALS["input_tokens"] * PRICE_IN + TOTALS["output_tokens"] * PRICE_OUT))
    return rec, obj


# ---------------------------------------------------------------------- main


def episode_files():
    files = sorted(f for f in os.listdir(TRANSCRIPTS)
                   if f.endswith(".md") and f not in SKIP_FILES)
    return [f[:-3] for f in files]


def already_done(stem):
    path = os.path.join(OUTDIR, stem + ".json")
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            obj = json.load(fh)
    except (ValueError, OSError):
        return None
    return obj if isinstance(obj, dict) and isinstance(obj.get("mentions"), list) else None


def main():
    t_start = time.time()
    os.makedirs(OUTDIR, exist_ok=True)
    key = oe.api_key()
    with open(CHUNK_PROMPT, encoding="utf-8") as fh:
        prompt = fh.read()

    stems = episode_files()
    log("corpus: %d episodes (2 duplicate re-airs skipped)" % len(stems))

    manifest = {"model": MODEL, "effort": EFFORT, "chunk_size": CHUNK_SIZE,
                "overlap": OVERLAP, "prompt": os.path.basename(CHUNK_PROMPT),
                "episodes": {}, "totals": {}}
    if os.path.exists(MANIFEST):
        try:
            with open(MANIFEST, encoding="utf-8") as fh:
                prev = json.load(fh)
            manifest["episodes"] = prev.get("episodes", {})
        except (ValueError, OSError):
            pass

    todo, skipped = [], []
    trs, plans = {}, {}
    for stem in stems:
        if already_done(stem) is not None and stem in manifest["episodes"]:
            skipped.append(stem)
            continue
        tr = cl.parse_transcript(os.path.join(TRANSCRIPTS, stem + ".md"))
        trs[stem] = tr
        plans[stem] = chunk_ranges(len(tr.paragraphs), CHUNK_SIZE, OVERLAP)
        todo.append(stem)
    log("resume: %d episodes already complete, %d to run" % (len(skipped), len(todo)))
    if not todo:
        log("nothing to do")
        return 0

    jobs = [(stem, ci) for stem in todo for ci in range(len(plans[stem]))]
    log("chunk jobs: %d  (concurrency %d)" % (len(jobs), CONCURRENCY))

    # An episode is merged and written by whichever worker finishes its last
    # chunk, so a straggler in one episode can never hold finished episodes in
    # memory behind it -- the first run lost ~6400 completed chunks that way.
    pending = {stem: len(plans[stem]) for stem in todo}
    parts = {stem: [None] * len(plans[stem]) for stem in todo}
    recs_by_stem = {stem: [None] * len(plans[stem]) for stem in todo}
    ep_lock = threading.Lock()
    written = [0]

    def finalize(stem):
        objs, recs = parts.pop(stem), recs_by_stem.pop(stem)
        census, stats, rejected = merge(stem, objs, plans[stem])
        ep_stats = {
            "chunks": len(objs),
            "raw_mentions": stats["raw"],
            "kept": stats["kept"],
            "rejected": stats["snippet_not_found"] + stats["bad_paragraph_index"]
                        + stats["malformed"],
            "snippet_not_found": stats["snippet_not_found"],
            "bad_paragraph_index": stats["bad_paragraph_index"],
            "malformed": stats["malformed"],
            "dup_dropped": stats["overlap_dupes_dropped"],
            "failed_chunks": stats["failed_chunks"],
            "suspect_sparse_chunks": [r["chunk"] for r in recs if r and r.get("suspect_sparse")],
            "retries": sum(r["retries"] for r in recs if r),
            "paragraphs": len(trs[stem].paragraphs),
            "words": len(trs[stem].body.split()),
            "input_tokens": sum(r["input_tokens"] for r in recs if r),
            "output_tokens": sum(r["output_tokens"] for r in recs if r),
            "reasoning_tokens": sum(r["reasoning_tokens"] for r in recs if r),
        }
        tmp = os.path.join(OUTDIR, stem + ".json.tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(census, fh, indent=1, ensure_ascii=False)
        os.replace(tmp, os.path.join(OUTDIR, stem + ".json"))
        if rejected:
            with open(os.path.join(SCRATCH, "prod_rejected_%s.json" % stem), "w",
                      encoding="utf-8") as fh:
                json.dump(rejected, fh, indent=1, ensure_ascii=False)
        trs.pop(stem, None)
        with ep_lock:
            manifest["episodes"][stem] = ep_stats
            written[0] += 1
            n = written[0]
            flush = (n % 10 == 0) or n == len(todo)
            if flush:
                write_manifest(manifest, t_start, partial=(n != len(todo)))
        log("[%3d/%3d] %-52s chunks=%2d kept=%4d rej=%3d dup=%2d fail=%s sparse=%s"
            % (n, len(todo), stem[:52], ep_stats["chunks"], ep_stats["kept"],
               ep_stats["rejected"], ep_stats["dup_dropped"],
               ep_stats["failed_chunks"] or "-",
               ep_stats["suspect_sparse_chunks"] or "-"))

    def work(job):
        stem, ci = job
        try:
            lo, hi = plans[stem][ci]
            text = render(trs[stem], stem, ci, len(plans[stem]), lo, hi)
            rec, obj = run_chunk(key, stem, ci, text, prompt, hi - lo)
        except Exception as e:  # noqa: BLE001 - never let a worker die silently
            log("[%s c%02d] WORKER ERROR %s: %s" % (stem[:34], ci, type(e).__name__, e))
            rec, obj = {"stem": stem, "chunk": ci, "ok": False, "retries": 0,
                        "input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0,
                        "error": "%s: %s" % (type(e).__name__, e)}, None
        try:
            with ep_lock:
                parts[stem][ci] = obj
                recs_by_stem[stem][ci] = rec
                pending[stem] -= 1
                ready = pending[stem] == 0
            if ready:
                finalize(stem)
        except Exception as e:  # noqa: BLE001 - a bad merge must not kill the run
            log("[%s] FINALIZE ERROR %s: %s" % (stem[:40], type(e).__name__, e))

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(work, jobs))

    write_manifest(manifest, t_start, partial=False)
    log("\ndone in %.1f min; %s" % ((time.time() - t_start) / 60,
                                    ABORT_REASON[0] if ABORT_REASON else "no systemic failure"))
    return 1 if ABORT.is_set() else 0


def write_manifest(manifest, t_start, partial):
    eps = manifest["episodes"]
    it = sum(e["input_tokens"] for e in eps.values())
    ot = sum(e["output_tokens"] for e in eps.values())
    manifest["totals"] = {
        "episodes": len(eps),
        "chunks": sum(e["chunks"] for e in eps.values()),
        "raw_mentions": sum(e["raw_mentions"] for e in eps.values()),
        "kept": sum(e["kept"] for e in eps.values()),
        "rejected": sum(e["rejected"] for e in eps.values()),
        "dup_dropped": sum(e["dup_dropped"] for e in eps.values()),
        "failed_chunks": sum(len(e["failed_chunks"]) for e in eps.values()),
        "suspect_sparse_chunks": sum(len(e["suspect_sparse_chunks"]) for e in eps.values()),
        "retries": sum(e["retries"] for e in eps.values()),
        "input_tokens": it,
        "output_tokens": ot,
        "reasoning_tokens": sum(e["reasoning_tokens"] for e in eps.values()),
        "cost_usd": round(it * PRICE_IN + ot * PRICE_OUT, 2),
        "wall_minutes": round((time.time() - t_start) / 60, 1),
        "session_requests": TOTALS["requests"],
        "session_retries": TOTALS["retries"],
        "session_http_errors": TOTALS["http_errors"],
        "session_parse_failures": TOTALS["parse_failures"],
        "partial": partial,
        "aborted": ABORT_REASON[0] if ABORT_REASON else None,
    }
    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1)
    os.replace(tmp, MANIFEST)


if __name__ == "__main__":
    sys.exit(main())
