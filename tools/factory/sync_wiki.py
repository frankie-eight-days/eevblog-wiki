#!/usr/bin/env python3
"""Sync written articles into the Quartz wiki: citations, wikilinks, infoboxes.

Three transforms, in order:

1. CITATIONS. `[844]` and `[fK2KBDo7ISY]` become superscript links into this
   site's own transcript page at the paragraph the claim came from, and every
   cited video gets a row in a Sources table with a YouTube deep link. The
   citation target is the transcript rather than YouTube because the point of
   hosting the transcripts is that a reader can check a claim without leaving.

2. WIKILINKS. A concept that has its own article becomes `[[link]]` on its first
   mention, using the canon alias table so "A to D converter" reaches
   `analog-to-digital-converter`. Only the first occurrence, and never inside a
   heading or an existing link -- a page where every third word is blue is worse
   than one with no links at all.

3. INFOBOX. Videos, mentions, explanatory mentions and span, injected as HTML.

  python3 tools/factory/sync_wiki.py
"""
import html
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
ARTS = ROOT / "articles/factory/articles"
BUNDLES = ROOT / "articles/factory/bundles"
OUT = ROOT / "wiki/content"
CITE = re.compile(r"\[([0-9]{1,4}|[A-Za-z0-9_-]{8,})\]")
# a heading line, or text already inside a link/wikilink
SKIP_LINE = re.compile(r"^\s*#")


def load_stats():
    d = json.loads((ROOT / "articles/candidates.json").read_text())
    return {c["concept"]: c for c in d["candidates"]}


def cite_targets(concept):
    """cite token -> {num, title, url, video_id, paragraph}"""
    p = BUNDLES / f"{concept}.json"
    if not p.exists():
        return {}
    out = {}
    for ps in json.loads(p.read_text())["passages"]:
        k = str(ps.get("cite") or ps.get("video_number"))
        if k not in out:
            out[k] = {"num": ps.get("video_number"), "title": ps["title"],
                      "url": ps.get("url", ""), "vid": ps["video_id"],
                      "para": ps["paragraph_index"]}
    return out


def apply_citations(text, targets):
    """Superscript links + a Sources table. Returns (text, used tokens)."""
    used = []

    def sub(m):
        tok = m.group(1)
        t = targets.get(tok)
        if not t:
            return m.group(0)
        if tok not in used:
            used.append(tok)
        n = used.index(tok) + 1
        label = t["num"] if t["num"] else "•"
        return (f'<sup class="cite"><a href="#src-{tok}" '
                f'title="{html.escape(t["title"])}">{label}</a></sup>')

    body = CITE.sub(sub, text)
    if not used:
        return body, used
    rows = ["", "## Sources", "",
            '<table class="srcs"><tbody>']
    for tok in used:
        t = targets[tok]
        num = f"#{t['num']}" if t["num"] else "&mdash;"
        # link to our own transcript page at the paragraph, plus the video
        rows.append(
            f'<tr id="src-{tok}">'
            f'<td class="n">{num}</td>'
            # cleanUrls strips .html; linking with the extension works only
            # via a 308 redirect, which costs a round trip on every citation
            f'<td><a href="/transcripts/t/{t["vid"]}#p{t["para"]}">'
            f'{html.escape(t["title"])}</a></td>'
            f'<td class="y"><a href="{html.escape(t["url"])}" target="_blank" '
            f'rel="noopener">watch</a></td></tr>')
    rows.append("</tbody></table>")
    return body + "\n" + "\n".join(rows) + "\n", used


def build_linker(concepts, alias):
    """surface phrase -> concept, longest first so multi-word names win."""
    surf = {}
    for c in concepts:
        surf[c.replace("-", " ")] = c
    for a, c in alias.items():
        if c in concepts and len(a) > 3:
            surf.setdefault(a.replace("-", " "), c)
    keys = sorted(surf, key=len, reverse=True)
    # a single alternation is far faster than 200+ passes over the text
    pat = re.compile(r"(?<![\w/\[])(" +
                     "|".join(re.escape(k) for k in keys) +
                     r")(?![\w\]])", re.I)
    return pat, surf


def apply_links(text, pat, surf, self_concept):
    linked, out_lines = set(), []
    for line in text.split("\n"):
        if SKIP_LINE.match(line) or line.startswith("<"):
            out_lines.append(line)
            continue

        def sub(m):
            phrase = m.group(1)
            c = surf.get(phrase.lower())
            if not c or c == self_concept or c in linked:
                return phrase
            linked.add(c)
            # Compare against the RAW concept name, not the de-hyphenated one:
            # `[[voltage-regulator]]` renders as "voltage-regulator", hyphen and
            # all, in the middle of a sentence. The alias is only redundant when
            # the surface text matches the slug exactly.
            if phrase == c:
                return f"[[{c}]]"
            return f"[[{c}|{phrase}]]"
        out_lines.append(pat.sub(sub, line))
    return "\n".join(out_lines)


def infobox(concept, st, n_src):
    if not st:
        return ""
    span = ""
    if st.get("first_video_num") and st.get("last_video_num"):
        span = (f'<tr><td>Span</td><td>#{st["first_video_num"]}'
                f'&ndash;#{st["last_video_num"]}</td></tr>')
    return (
        '<aside class="ib">'
        f'<div class="ib-h">{html.escape(concept.replace("-", " "))}</div>'
        '<table><tbody>'
        f'<tr><td>Videos</td><td>{st["video_count"]:,}</td></tr>'
        f'<tr><td>Mentions</td><td>{st["mention_count"]:,}</td></tr>'
        f'<tr><td>Explained in</td><td>{st["explains_count"]:,}</td></tr>'
        f'<tr><td>Sources cited</td><td>{n_src}</td></tr>'
        f'{span}'
        f'<tr><td>Type</td><td>{html.escape(st["type"])}</td></tr>'
        '</tbody></table></aside>')


def main():
    stats = load_stats()
    alias = json.loads((ROOT / "canon/alias_table.json").read_text())
    files = sorted(ARTS.glob("*.md"))
    concepts = sorted({f.name.split(".")[0] for f in files})
    pat, surf = build_linker(set(concepts), alias)
    surf = {k.lower(): v for k, v in surf.items()}
    OUT.mkdir(parents=True, exist_ok=True)

    written = []
    for f in files:
        concept = f.name.split(".")[0]
        model = f.name.split(".")[-2]
        raw = f.read_text()
        title = re.match(r"#\s+(.+)", raw)
        title = title.group(1).strip() if title else concept.replace("-", " ")
        body = re.sub(r"^#\s+.+\n", "", raw, count=1)

        body = apply_links(body, pat, surf, concept)
        body, used = apply_citations(body, cite_targets(concept))
        st = stats.get(concept)
        fm = (f"---\ntitle: {title}\n"
              f"tags:\n  - {st['type'] if st else 'concept'}\n"
              f"writer: {model}\n---\n\n")
        (OUT / f"{concept}.md").write_text(
            fm + infobox(concept, st, len(used)) + "\n\n" + body)
        written.append((concept, title, st, len(used)))

    # index page
    rows = ["---", "title: All articles", "---", "",
            f"{len(written)} articles, generated from 2,886 transcribed videos.",
            "", "| Article | Videos | Explained in | Sources |", "|---|---:|---:|---:|"]
    for c, t, st, n in sorted(written, key=lambda r: -(r[2]["explains_count"] if r[2] else 0)):
        rows.append(f"| [[{c}\\|{t}]] | {st['video_count'] if st else '—'} | "
                    f"{st['explains_count'] if st else '—'} | {n} |")
    (OUT / "all.md").write_text("\n".join(rows) + "\n")

    # Home page. Without a content/index.md Quartz emits no root index.html at
    # all, and a static host then serves the next best directory index it can
    # find -- which was index.xml, so the site's front door returned the raw RSS
    # feed as XML. Every deep link worked, which is exactly why it went unnoticed.
    top = sorted(written, key=lambda r: -(r[2]["explains_count"] if r[2] else 0))
    total_w = sum(len(( OUT / f"{c}.md").read_text().split()) for c, _, _, _ in written)
    home = ["---", "title: EEVblog Wiki", "---", "",
            f"An encyclopedia of the electronics knowledge in **{len(written)} articles**, "
            f"built from **2,886 transcribed EEVblog videos** (10.6 million words).",
            "",
            "Every factual sentence carries a citation to the video and the exact "
            "moment it came from. Nothing here was written from outside knowledge: "
            "if it is not in the transcripts, it is not on the page.",
            "", "## Start here", "",
            "- [[all|All articles]] — the full index, ranked by how often each "
            "subject is explained",
            "- [Transcripts](/transcripts) — all 2,886 videos, searchable",
            "- [Concept graph](/explore) — 5,042 concepts by what gets discussed together",
            "", "## Most explained", ""]
    for c, t, st, n in top[:24]:
        home.append(f"- [[{c}|{t}]] — explained in {st['explains_count']} of "
                    f"{st['video_count']} videos" if st else f"- [[{c}|{t}]]")
    home += ["", "## How it works", "",
             "A census pass read every transcript and recorded each concept "
             "mentioned, grading whether it was merely named, explained, or "
             "opined on. Those surface forms were folded into canonical concepts, "
             "linked by co-occurrence, and ranked. Articles were then written from "
             "the gathered passages alone, and every quotation was byte-compared "
             "against the transcript before publication."]
    (OUT / "index.md").write_text("\n".join(home) + "\n")

    print(f"{len(written)} articles -> {OUT}")
    print("  index.md (home) + all.md (full list)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
