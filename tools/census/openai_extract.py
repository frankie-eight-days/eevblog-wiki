"""OpenAI bake-off arms (gpt-5.6-luna, gpt-5.6-sol): concept-census extraction.

One request per (model, episode). Payload is census_prompt_v2.md verbatim with the
full transcript file appended after the prompt's trailing "--- TRANSCRIPT ---"
marker -- the same convention the opus/sonnet/kimi arms saw. Nothing else is
added: the prompt is the spec and the arms must stay comparable.

Responses API, streamed so a long reasoning+output turn cannot hit an idle
timeout. reasoning.effort is "low" for both arms (the production-relevant config).
"""
from __future__ import annotations

import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SCRATCH = os.path.dirname(os.path.abspath(__file__))
WIKI = "/Users/frankwalsh/Documents/vibecoding/eevblog_wiki"
TRANSCRIPTS = os.environ.get("EEV_TRANSCRIPTS", os.path.join(WIKI, "transcripts"))
PROMPT_PATH = os.path.join(WIKI, "research", "census_prompt_v2.md")
BAKEOFF = os.path.join(WIKI, "research", "bakeoff")

URL = "https://api.openai.com/v1/responses"
ARMS = {"luna": "gpt-5.6-luna", "sol": "gpt-5.6-sol"}
EFFORT = "low"
MAX_OUTPUT_TOKENS = 64000
TIMEOUT = 1800

STEMS = [
    "the-amp-hour-79-ludibrious-luxating-layout",
    "0212-an-interview-with-trey-german-launchpad-laden-lodesman",
    "0500-two-and-a-half-orders-of-magnitude",
    "0650-accessible-asics-with-andreas-olofsson",
    "0728-space-age-bluetooth-with-alex-haro",
]

_print_lock = threading.Lock()


def log(*a):
    with _print_lock:
        print(*a, flush=True)


def api_key():
    with open(os.path.join(SCRATCH, "openai_key"), encoding="utf-8") as fh:
        return fh.read().strip()


def build_content(stem, extra_note=None):
    with open(PROMPT_PATH, encoding="utf-8") as fh:
        prompt = fh.read()
    with open(os.path.join(TRANSCRIPTS, stem + ".md"), encoding="utf-8") as fh:
        transcript = fh.read()
    content = prompt + transcript
    if extra_note:
        content += "\n\n" + extra_note
    return content


def stream_request(key, model, content, max_tokens, effort=None):
    """-> (http_status, text, usage dict, status/stop string)

    `effort` defaults to the module-level EFFORT; pass it explicitly when
    several efforts are in flight at once (threads share the module global).
    """
    payload = {
        "model": model,
        "input": content,
        "reasoning": {"effort": effort or EFFORT},
        "max_output_tokens": max_tokens,
        "stream": True,
    }
    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "authorization": "Bearer %s" % key,
            "accept": "text/event-stream",
        },
        method="POST",
    )
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), {}, "http-error"
    except urllib.error.URLError as e:
        return 0, "urlerror: %s" % e, {}, "url-error"

    status = resp.status
    parts, usage, stop = [], {}, None
    try:
        for raw in resp:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            chunk = line[5:].strip()
            if not chunk or chunk == "[DONE]":
                continue
            try:
                ev = json.loads(chunk)
            except json.JSONDecodeError:
                continue
            t = ev.get("type")
            if t == "response.output_text.delta":
                parts.append(ev.get("delta") or "")
            elif t in ("response.completed", "response.incomplete", "response.failed"):
                r = ev.get("response") or {}
                usage.update(r.get("usage") or {})
                stop = r.get("status") or t
                if not parts:
                    # fall back to the assembled response object
                    for item in r.get("output") or []:
                        for c in item.get("content") or []:
                            if c.get("type") == "output_text":
                                parts.append(c.get("text") or "")
                inc = r.get("incomplete_details")
                if inc:
                    stop = "%s:%s" % (stop, inc.get("reason"))
            elif t == "error":
                return status, json.dumps(ev), usage, "stream-error"
    except Exception as e:  # noqa: BLE001 - a dropped socket mid-stream is a retryable failure
        return status, "".join(parts), usage, "stream-broken: %s" % e
    return status, "".join(parts), usage, stop


FENCE = re.compile(r"^\s*```(?:json)?\s*(.*?)\s*```\s*$", re.S)


def parse_json(text):
    """-> (obj|None, status string)"""
    if not text or not text.strip():
        return None, "empty"
    s = text.strip()
    m = FENCE.match(s)
    if m:
        s = m.group(1).strip()
    else:
        i = s.find("{")
        if i > 0:
            s = s[i:]
    try:
        return json.loads(s), "ok"
    except json.JSONDecodeError as e:
        return None, "parse-error: %s" % e


RETRY_NOTE = (
    "Your previous response could not be parsed as JSON (it was truncated or "
    "malformed). Return the same JSON object again as compact JSON: no markdown "
    "fence, no prose, minimal whitespace."
)


def run_one(arm, stem, key):
    model = ARMS[arm]
    outdir = os.path.join(BAKEOFF, arm)
    t0 = time.time()
    attempts = []
    for attempt in (1, 2):
        content = build_content(stem, None if attempt == 1 else RETRY_NOTE)
        http, text, usage, stop = stream_request(key, model, content, MAX_OUTPUT_TOKENS)
        obj, pstatus = parse_json(text) if http == 200 else (None, "http %s" % http)
        det = usage.get("output_tokens_details") or {}
        rec = {
            "arm": arm, "attempt": attempt, "http": http,
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "reasoning_tokens": det.get("reasoning_tokens"),
            "total_tokens": usage.get("total_tokens"),
            "status": stop, "parse": pstatus,
            "mentions": len(obj.get("mentions") or []) if isinstance(obj, dict) else 0,
            "chars": len(text or ""), "seconds": round(time.time() - t0, 1),
        }
        attempts.append(rec)
        log("[%s/%s] att%d: HTTP %s in=%s out=%s (reason=%s) status=%s parse=%s "
            "mentions=%d (%.0fs)" % (arm, stem[:30], attempt, http, rec["input_tokens"],
                                     rec["output_tokens"], rec["reasoning_tokens"], stop,
                                     pstatus, rec["mentions"], rec["seconds"]))
        if http != 200:
            log("[%s/%s]   error body: %s" % (arm, stem[:30], (text or "")[:400]))
        if obj is not None:
            os.makedirs(outdir, exist_ok=True)
            with open(os.path.join(outdir, stem + ".json"), "w", encoding="utf-8") as fh:
                json.dump(obj, fh, indent=1, ensure_ascii=False)
            return {"arm": arm, "stem": stem, "ok": True, "attempts": attempts}
        if attempt == 1:
            with open(os.path.join(SCRATCH, "openai_raw_%s_%s.txt" % (arm, stem)), "w",
                      encoding="utf-8") as fh:
                fh.write(text or "")
    return {"arm": arm, "stem": stem, "ok": False, "attempts": attempts}


def main():
    key = api_key()
    args = sys.argv[1:]
    arms = [a for a in args if a in ARMS] or list(ARMS)
    stems = [s for s in args if s in STEMS] or STEMS
    jobs = [(a, s) for a in arms for s in stems]
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(lambda j: run_one(j[0], j[1], key), jobs))
    log("\n=== summary ===")
    for r in results:
        a = r["attempts"][-1]
        log("%-6s %-60s %s http=%s out_tok=%s mentions=%d parse=%s"
            % (r["arm"], r["stem"], "OK " if r["ok"] else "FAIL", a["http"],
               a["output_tokens"], a["mentions"], a["parse"]))
    for arm in arms:
        rs = [r for r in results if r["arm"] == arm]
        it = sum(a["input_tokens"] or 0 for r in rs for a in r["attempts"])
        ot = sum(a["output_tokens"] or 0 for r in rs for a in r["attempts"])
        rt = sum(a["reasoning_tokens"] or 0 for r in rs for a in r["attempts"])
        log("%s totals: input=%d output=%d (reasoning=%d)" % (arm, it, ot, rt))
    with open(os.path.join(SCRATCH, "openai_run_log.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    return 0 if all(r["ok"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
