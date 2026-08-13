#!/usr/bin/env python3
"""Check a written article against the bundle it was written from.

Two mechanical checks, both of which a model can fail silently and neither of
which a human reviewer reliably catches by reading:

  QUOTES     every quoted string must appear character-for-character inside some
             passage. This is the fabrication check. A model that tidies up a
             quote -- expanding a contraction, dropping a filler word, adding a
             hyphen -- fails, and should: the whole premise of the wiki is that
             quoted words were actually said.
  CITATIONS  every [123] must be a video number present in the bundle. A model
             that invents a plausible-looking number produces an article that
             cannot be traced, which is worse than one with no citations at all.

  python3 verify_article.py articles/factory/bakeoff/asic.k3.md
  python3 verify_article.py --json articles/factory/bakeoff/*.md
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
BUNDLES = ROOT / "articles/factory/bundles"
CITE = re.compile(r"\[(\d{1,4})\]")
# straight and curly doubles; markdown blockquotes are checked separately
QUOTED = re.compile(r"[\"“]([^\"“”]{12,600})[\"”]")
MIN_WORDS = 4          # below this a "quote" is a term in scare quotes, not a quote


def norm(s):
    """Whitespace-only normalisation. Deliberately NOT case- or punctuation-
    insensitive: the point is to catch tidying, and tidying is exactly what a
    looser comparison would forgive."""
    return re.sub(r"\s+", " ", s).strip()


def verify(path):
    art = pathlib.Path(path)
    stem = art.name.split(".")[0]
    bpath = BUNDLES / f"{stem}.json"
    if not bpath.exists():
        return {"file": art.name, "error": f"no bundle {bpath.name}"}
    bundle = json.loads(bpath.read_text())
    text = art.read_text()

    # Check against the FULL transcript of every video in the bundle, not the
    # bundle's own passage text. Two of five flagged quotes turned out to be
    # real: a quotation that runs across the join between a passage and its
    # truncated context matches neither fragment, and the 240-passage cap means
    # a video can be in the bundle while the quoted paragraph is not. Both
    # produced false fabrication alarms. The transcript is the ground truth the
    # claim is really being made about, so compare against that.
    seen_v, hay = set(), []
    for p in bundle["passages"]:
        v = p["video_id"]
        if v in seen_v:
            continue
        seen_v.add(v)
        for d in (ROOT / "transcripts", ROOT / "transcripts_whisper"):
            f = d / f"{v}.md"
            if f.exists():
                hay.append(norm(f.read_text()))
                break
    haystack = "\n".join(hay)
    vids = {p["video_number"] for p in bundle["passages"] if p["video_number"]}
    ids = {p.get("cite") for p in bundle["passages"] if p.get("cite")}
    ids |= {p["video_id"] for p in bundle["passages"]}

    # Pair quote marks by ALTERNATION, not by regex. A pattern like
    # ["“]([^"“”]+)["”] happily matches from the closing quote of one span to
    # the opening quote of the NEXT, capturing the ordinary prose in between and
    # reporting it as an unverified quotation. That raised two false fabrication
    # alarms on an article whose quotations were all genuine -- the worst kind of
    # check failure, because a verifier that cries wolf discredits its real hits.
    segs = re.split(r'["“”]', text)
    quotes = [q for q in segs[1::2] if len(q.split()) >= MIN_WORDS]
    bad_q = [q for q in quotes if norm(q) not in haystack]

    cites = [int(c) for c in CITE.findall(text)]
    bad_c = sorted({c for c in cites if c not in vids})
    # A citation that is not a number at all -- [None], [n/a], [?] -- slipped
    # straight through the numeric regex and was counted as neither valid nor
    # invalid, so a run with six of them still reported a clean sweep. Anything
    # bracketed that is not a valid number is now a failure.
    junk = [t for t in re.findall(r"\[([^\]\n]{1,24})\]", text)
            if not t.isdigit() and t not in ids
            and not t.startswith(("^", "http"))]

    body = re.sub(r"^#.*$", "", text, flags=re.M)
    return {
        "file": art.name, "model": art.name.split(".")[-2],
        "concept": stem,
        "words": len(body.split()),
        "quotes": len(quotes), "quotes_bad": len(bad_q),
        "citations": len(cites), "citations_distinct": len(set(cites)),
        "citations_bad": len(bad_c) + len(junk),
        "citations_junk": len(junk),
        "junk_tokens": sorted(set(junk))[:6],
        "bad_citation_numbers": bad_c[:8],
        "bad_quotes": [q[:110] for q in bad_q[:5]],
        "sections": len(re.findall(r"^##\s", text, flags=re.M)),
        # a sentence with no citation anywhere near it is an unsourced claim
        "uncited_paragraphs": sum(
            1 for p in body.split("\n\n")
            if len(p.split()) > 25 and not CITE.search(p)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows = [verify(f) for f in args.files]
    if args.json:
        print(json.dumps(rows, indent=1))
        return 0
    print(f"{'article':34} {'words':>6} {'quo':>4} {'bad':>4} "
          f"{'cite':>5} {'uniq':>5} {'bad':>4} {'sec':>4} {'uncited':>8}")
    for r in rows:
        if "error" in r:
            print(f"{r['file']:34} {r['error']}")
            continue
        print(f"{r['file']:34} {r['words']:6,} {r['quotes']:4} {r['quotes_bad']:4} "
              f"{r['citations']:5} {r['citations_distinct']:5} {r['citations_bad']:4} "
              f"{r['sections']:4} {r['uncited_paragraphs']:8}")
    for r in rows:
        for q in r.get("bad_quotes", []):
            print(f"  UNVERIFIED QUOTE  {r['file']}: \"{q}\"")
        if r.get("junk_tokens"):
            print(f"  NON-NUMERIC CITE  {r['file']}: "
                  f"{r['junk_tokens']} x{r['citations_junk']}")
        if r.get("bad_citation_numbers"):
            print(f"  INVALID CITES     {r['file']}: {r['bad_citation_numbers']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
