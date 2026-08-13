#!/usr/bin/env python3
"""Write one wiki article straight from a bundle, on any backend. Measured.

No extraction packet: the model reads the raw gathered passages and does both
jobs -- deciding what is knowledge and writing it. That is deliberate for the
model comparison, since a shared extraction pass would pre-make the hardest
judgment and leave only prose polish to compare.

Every run writes a sidecar <out>.run.json with tokens, wall-clock and cost, so
the comparison rests on measurements rather than impressions.

  python3 write_article.py --bundle .../asic.json --model k3 --out .../asic.k3.md
  python3 write_article.py --bundle ... --model terra --out ...
  python3 write_article.py --bundle ... --model k3 --dry-run   # print prompt size

Backends are chosen by model name:
  k3, k3-256k          Kimi coding plan (subscription quota, not per-token)
  terra, luna          OpenAI responses API
Sonnet/Opus run through the agent harness instead; see run_bakeoff.md.
"""
import argparse
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

KIMI_URL = "https://api.kimi.com/coding/v1/messages"
OPENAI_URL = "https://api.openai.com/v1/responses"

# USD per 1M tokens, for backends that actually meter. The Kimi coding plan is a
# flat subscription with a request quota, so its dollar cost per article is not
# defined -- recorded as null rather than guessed at the platform's rates, which
# this key cannot even use.
PRICES = {
    "terra": (1.25, 10.00),
    "luna": (0.20, 1.20),
}

SPEC = """You are writing an encyclopedia article for a technical reference wiki about the EEVblog YouTube channel's body of knowledge.

The subject is: {title}

SOURCE
You are given every passage from the corpus that touches this subject: {n} passages drawn from {v} videos. Each passage carries the video number, its title, a deep link, the speaker, and the surrounding context. Nothing has been pre-selected or summarised for you -- deciding what is worth saying is part of your job.

REGISTER AND VOICE
- Encyclopedic, neutral, third person. State claims as knowledge, not as things someone said on a video.
- Every factual sentence carries a bracketed video citation, e.g. "A linear regulator needs headroom between input and output to regulate at all.[844]" Stack them when several passages support one statement: "...[844][1112]".
- ZERO meta commentary. Never mention YouTube, a video, a channel, a teardown as-a-video, a viewer, this article, or the reader. The bracketed numbers are the only trace of provenance.
- Use named attribution ONLY where whose practice it is is itself the content -- a specific bench habit, a personal rule of thumb. Ordinary technical facts are never attributed to whoever happened to say them.
- Never write a Reception section, and never write reception or adoption material: nothing about how a product was received, what users felt, or how popular a thing became.

QUOTATION -- THIS IS CHECKED MECHANICALLY
- Direct quotation is rare; quote only when the exact phrasing is itself the artifact.
- Any string you place in quotation marks MUST appear character-for-character inside the `text` field of one of the supplied passages. It is byte-compared after you finish. A hyphen added, a filler word dropped, or a contraction expanded is a FAILURE.
- If you cannot reproduce it exactly, paraphrase instead. Paraphrase is always safe; an approximate quote is not.

CITATIONS -- ALSO CHECKED
- Cite only video numbers that appear in the supplied passages. Do not infer, guess, or invent a number.

SUBSTANCE
- Lead with what the thing IS and why it matters, in two or three sentences, before any detail.
- Prefer the specific over the general: a number, a threshold, a failure mode, a named part, a concrete consequence. Discard passages that carry no knowledge -- a passing name-drop is not material.
- Where the corpus contains a strong practical opinion held consistently, it may be stated as engineering judgment, not as sentiment.
- Organise under `##` headings that suit the subject. Do not use a fixed template.
- Length: whatever the evidence supports. Do not pad. If the evidence is thin, write a short article and stop.

OUTPUT
Markdown only. Start with `# {title}`. No preamble, no closing remarks, no notes about your process."""


def prompt_for(bundle):
    title = bundle["concept"].replace("-", " ")
    lines = []
    for p in bundle["passages"]:
        head = f"[{p['video_number']}] {p['title']} — {p['speaker'] or 'unknown'} ({p['depth']})"
        lines.append(f"{head}\n"
                     f"context before: {p['context_before']}\n"
                     f"TEXT: {p['text']}\n"
                     f"context after: {p['context_after']}\n")
    spec = SPEC.format(title=title, n=bundle["passage_count"],
                       v=bundle["video_count"])
    return spec + "\n\n=== PASSAGES ===\n\n" + "\n".join(lines)


def post(url, payload, key, extra=None):
    body = json.dumps(payload).encode()
    hdr = {"Content-Type": "application/json"}
    hdr.update(extra or {})
    hdr.setdefault("Authorization", f"Bearer {key}")
    req = urllib.request.Request(url, body, hdr)
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read())


def call_kimi(model, prompt, max_tokens):
    key = (ROOT / "tools/kimi_key").read_text().strip()
    d = post(KIMI_URL, {"model": model, "max_tokens": max_tokens,
                        "messages": [{"role": "user", "content": prompt}]},
             key, {"anthropic-version": "2023-06-01", "x-api-key": key})
    text = "".join(c.get("text", "") for c in d.get("content", []))
    u = d.get("usage") or {}
    return text, u.get("input_tokens", 0), u.get("output_tokens", 0)


def call_openai(model, prompt, max_tokens):
    key = (ROOT / "tools/census/openai_key").read_text().strip()
    d = post(OPENAI_URL, {"model": f"gpt-5.6-{model}", "input": prompt,
                          "reasoning": {"effort": "medium"},
                          "max_output_tokens": max_tokens}, key)
    text = ""
    for item in d.get("output", []):
        for c in item.get("content", []) or []:
            if c.get("type") == "output_text":
                text = c["text"]
    u = d.get("usage") or {}
    return text, u.get("input_tokens", 0), u.get("output_tokens", 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--dry-run", action="store_true")
    # Sonnet and Opus have no API key here and run through the agent harness
    # instead. They must receive the SAME bytes as the API models or the
    # comparison measures prompt differences rather than model differences.
    ap.add_argument("--dump-prompt", metavar="PATH")
    args = ap.parse_args()

    bundle = json.loads(pathlib.Path(args.bundle).read_text())
    prompt = prompt_for(bundle)
    if args.dump_prompt:
        p = pathlib.Path(args.dump_prompt)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(prompt)
        print(f"{p} ({len(prompt):,} chars)")
        return 0
    if args.dry_run:
        print(f"{bundle['concept']}: {len(prompt):,} chars "
              f"(~{len(prompt)//4:,} tokens), {bundle['passage_count']} passages")
        return 0

    t0 = time.time()
    if args.model.startswith("k3") or args.model.startswith("kimi"):
        text, tin, tout = call_kimi(args.model, prompt, args.max_tokens)
    else:
        text, tin, tout = call_openai(args.model, prompt, args.max_tokens)
    dt = time.time() - t0

    if not text.strip():
        print(f"EMPTY RESPONSE from {args.model}", file=sys.stderr)
        return 1

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    rate = PRICES.get(args.model)
    cost = (tin * rate[0] + tout * rate[1]) / 1e6 if rate else None
    run = {"concept": bundle["concept"], "model": args.model,
           "seconds": round(dt, 1), "input_tokens": tin, "output_tokens": tout,
           "cost_usd": round(cost, 4) if cost is not None else None,
           "billing": "per-token" if rate else "subscription-quota",
           "words": len(text.split()), "chars": len(text)}
    out.with_suffix(out.suffix + ".run.json").write_text(json.dumps(run, indent=1))
    print(f"{args.model:8} {bundle['concept']:18} {dt:6.1f}s  "
          f"in {tin:6,} out {tout:6,}  {len(text.split()):5,} words  "
          f"{('$%.3f' % cost) if cost is not None else 'quota'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
