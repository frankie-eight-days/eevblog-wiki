#!/usr/bin/env python3
"""Render the bakeoff articles as one reviewable HTML page.

Every [123] becomes a link to that video at the timestamp of the passage the
claim came from, so a reviewer can check any sentence against the source in one
click rather than taking the citation on trust.

  python3 tools/factory/build_review_page.py [out.html]
"""
import html
import json
import pathlib
import re
import sys
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
BAKEOFF = ROOT / "articles/factory/bakeoff"
BUNDLES = ROOT / "articles/factory/bundles"
MODELS = ["opus", "k3", "sonnet", "terra"]
CITE = re.compile(r"\[(\d{1,4})\]")


def video_links():
    """video number -> (url, title). First passage wins; they all point at the
    same video, and the timestamp of the first is as good an entry point as any."""
    out = {}
    for b in sorted(BUNDLES.glob("*.json")):
        for p in json.loads(b.read_text())["passages"]:
            n = p.get("video_number")
            if n and n not in out:
                out[n] = (p.get("url") or "", p.get("title") or "")
    return out


def md(text, links):
    """Just enough markdown for what these articles use."""
    out, para = [], []

    def flush():
        if para:
            out.append("<p>" + " ".join(para) + "</p>")
            para.clear()

    for line in text.split("\n"):
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith("### "):
            flush(); out.append(f"<h3>{inline(s[4:], links)}</h3>")
        elif s.startswith("## "):
            flush(); out.append(f"<h2>{inline(s[3:], links)}</h2>")
        elif s.startswith("# "):
            flush(); out.append(f"<h1>{inline(s[2:], links)}</h1>")
        elif s.startswith(("- ", "* ")):
            flush(); out.append(f"<li>{inline(s[2:], links)}</li>")
        else:
            para.append(inline(s, links))
    flush()
    # wrap consecutive <li> in <ul>
    joined = "\n".join(out)
    joined = re.sub(r"(?:<li>.*?</li>\n?)+",
                    lambda m: "<ul>" + m.group(0) + "</ul>", joined, flags=re.S)
    return joined


def inline(s, links):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)

    def cite(m):
        n = int(m.group(1))
        url, title = links.get(n, ("", ""))
        if not url:
            return f'<sup class="c c-bad" title="not in bundle">[{n}]</sup>'
        return (f'<sup class="c"><a href="{html.escape(url)}" target="_blank" '
                f'rel="noopener" title="{html.escape(title)}">{n}</a></sup>')
    return CITE.sub(cite, s)


def main():
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site/bakeoff.html"
    links = video_links()

    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from verify_article import verify                      # noqa: E402

    concepts = OrderedDict()
    for b in sorted(BUNDLES.glob("*.json")):
        c = b.stem
        if not (BAKEOFF / f"{c}.{MODELS[0]}.md").exists():
            continue
        bundle = json.loads(b.read_text())
        concepts[c] = {"meta": {"passages": bundle["passage_count"],
                                "videos": bundle["video_count"],
                                "depths": bundle["depths"]}, "models": {}}
        for m in MODELS:
            p = BAKEOFF / f"{c}.{m}.md"
            if not p.exists():
                continue
            run = {}
            rp = p.with_suffix(p.suffix + ".run.json")
            if rp.exists():
                run = json.loads(rp.read_text())
            v = verify(p)
            concepts[c]["models"][m] = {
                "html": md(p.read_text(), links),
                "words": v["words"], "cites": v["citations"],
                "uniq": v["citations_distinct"], "bad_q": v["quotes_bad"],
                "bad_c": v["citations_bad"], "quotes": v["quotes"],
                "secs": run.get("seconds"), "cost": run.get("cost_usd"),
                "billing": run.get("billing", "agent"),
            }
    page = TEMPLATE.replace("__DATA__", json.dumps(concepts, separators=(",", ":")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print(f"{len(concepts)} concepts x {len(MODELS)} models -> {out} "
          f"({out.stat().st_size/1e6:.2f} MB)")
    return 0


TEMPLATE = r"""<title>EEVblog Wiki — article model bakeoff</title>
<style>
:root{
  --ground:#fffefb; --ink:#1b1a17; --ink-soft:#5d5a52; --ink-faint:#938f85;
  --panel:#f4f2ec; --rule:#ded9cf; --accent:#ff8500; --accent-ink:#a34e00;
  --ok:#2f6d40; --bad:#b3341f;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sans:system-ui,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#131210; --ink:#eceae4; --ink-soft:#a8a49a; --ink-faint:#767268;
  --panel:#1c1b18; --rule:#33312b; --accent:#ff9a2e; --accent-ink:#ffb055;
  --ok:#6fae7c; --bad:#e2705a;
}}
:root[data-theme="dark"]{
  --ground:#131210; --ink:#eceae4; --ink-soft:#a8a49a; --ink-faint:#767268;
  --panel:#1c1b18; --rule:#33312b; --accent:#ff9a2e; --accent-ink:#ffb055;
  --ok:#6fae7c; --bad:#e2705a;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.55}
.wrap{max-width:1240px;margin:0 auto;padding:0 22px}
header{border-bottom:3px solid var(--accent);background:var(--panel);
  position:sticky;top:0;z-index:20}
header .wrap{display:flex;justify-content:space-between;align-items:center;
  gap:14px;padding:13px 22px;flex-wrap:wrap}
h1.t{font-size:17px;margin:0}
h1.t b{color:var(--accent-ink)}
.tabs{display:flex;gap:7px;flex-wrap:wrap}
.tab{font-family:var(--mono);font-size:11.5px;text-transform:uppercase;
  letter-spacing:.07em;padding:7px 12px;border:1px solid var(--rule);
  border-radius:2px;background:var(--ground);color:var(--ink-soft);cursor:pointer}
.tab:hover{border-color:var(--accent)}
.tab[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);
  color:#1b1a17;font-weight:700}
.bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;
  padding:14px 0 4px;border-bottom:1px solid var(--rule);margin-bottom:20px}
.src{font-family:var(--mono);font-size:11.5px;color:var(--ink-faint);
  text-transform:uppercase;letter-spacing:.06em;margin-left:auto}
.cols{display:grid;gap:26px}
.cols.two{grid-template-columns:1fr 1fr}
.card{border:1px solid var(--rule);border-radius:3px;overflow:hidden;
  background:var(--ground)}
.card > .hd{background:var(--panel);border-bottom:1px solid var(--rule);
  padding:10px 16px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
.mname{font-family:var(--mono);font-size:13px;font-weight:700;
  text-transform:uppercase;letter-spacing:.08em;color:var(--accent-ink)}
.stat{font-family:var(--mono);font-size:11px;color:var(--ink-soft);
  font-variant-numeric:tabular-nums}
.stat b{color:var(--ink);font-weight:600}
.pill{font-family:var(--mono);font-size:10px;text-transform:uppercase;
  letter-spacing:.06em;padding:2px 7px;border-radius:2px;border:1px solid}
.pill.ok{color:var(--ok);border-color:var(--ok)}
.pill.bad{color:var(--bad);border-color:var(--bad)}
.body{padding:8px 26px 26px;font-family:var(--serif);font-size:16.5px;
  line-height:1.62;max-width:68ch}
.body h1{font-family:var(--sans);font-size:20px;margin:20px 0 6px;
  letter-spacing:.01em}
.body h2{font-family:var(--sans);font-size:15px;margin:26px 0 6px;
  text-transform:uppercase;letter-spacing:.07em;color:var(--accent-ink)}
.body h3{font-family:var(--sans);font-size:14.5px;margin:18px 0 4px}
.body p{margin:0 0 13px}
.body ul{margin:0 0 13px 18px;padding:0}
.body li{margin:0 0 5px}
sup.c{font-family:var(--mono);font-size:9.5px;vertical-align:2px;
  margin-left:1px;line-height:0}
sup.c a{color:var(--accent-ink);text-decoration:none;padding:0 1px}
sup.c a:hover{background:var(--accent);color:#1b1a17;border-radius:2px}
sup.c-bad{color:var(--bad)}
footer{margin:40px 0 60px;padding-top:16px;border-top:1px solid var(--rule);
  font-size:13px;color:var(--ink-faint);max-width:72ch}
@media(max-width:900px){.cols.two{grid-template-columns:1fr}}
</style>

<header><div class="wrap">
  <h1 class="t">Article <b>bakeoff</b></h1>
  <div class="tabs" id="ctabs"></div>
  <div class="tabs" id="mtabs"></div>
  <div class="tabs"><button class="tab" id="sxs" aria-pressed="false">side by side</button></div>
</div></header>

<div class="wrap">
  <div class="bar"><span class="src" id="src"></span></div>
  <div class="cols" id="cols"></div>
  <footer>All four models received byte-identical prompts: the full set of
  gathered passages, with nothing pre-selected or summarised. Every quotation was
  byte-compared against the transcript and every citation checked against the
  source bundle; a citation that failed that check would render in red. Click any
  citation to open the video at the moment the claim came from.</footer>
</div>

<script>
const D = __DATA__;
const CS = Object.keys(D), MS = ["opus","k3","sonnet","terra"];
let c = CS[0], m = "opus", sxs = false;

function tabs(el, items, cur, on){
  el.innerHTML = "";
  items.forEach(k=>{
    const b=document.createElement("button");
    b.className="tab"; b.textContent=k.replace(/-/g," ");
    b.setAttribute("aria-pressed", k===cur);
    b.onclick=()=>on(k); el.append(b);
  });
}
function card(model){
  const d = D[c].models[model];
  if(!d) return "";
  const clean = d.bad_q===0 && d.bad_c===0;
  const cost = d.cost!=null ? `$${d.cost.toFixed(3)}`
             : (d.billing==="subscription-quota" ? "quota" : "agent");
  return `<div class="card"><div class="hd">
    <span class="mname">${model}</span>
    <span class="stat"><b>${d.words.toLocaleString()}</b> words</span>
    <span class="stat"><b>${d.cites}</b> cites / <b>${d.uniq}</b> videos</span>
    <span class="stat"><b>${d.quotes}</b> quotes</span>
    <span class="stat">${d.secs!=null?`<b>${d.secs}</b>s`:""}</span>
    <span class="stat">${cost}</span>
    <span class="pill ${clean?"ok":"bad"}">${clean?"verified":(d.bad_q+" bad quotes / "+d.bad_c+" bad cites")}</span>
  </div><div class="body">${d.html}</div></div>`;
}
function render(){
  tabs(document.getElementById("ctabs"), CS, c, k=>{c=k;render();});
  tabs(document.getElementById("mtabs"), MS, m, k=>{m=k;render();});
  document.getElementById("sxs").setAttribute("aria-pressed", sxs);
  const meta = D[c].meta;
  document.getElementById("src").textContent =
    `source: ${meta.passages} passages · ${meta.videos} videos · ` +
    Object.entries(meta.depths).map(([k,v])=>`${v} ${k}`).join(" · ");
  const cols = document.getElementById("cols");
  cols.className = "cols" + (sxs ? " two" : "");
  cols.innerHTML = sxs ? MS.map(card).join("") : card(m);
  scrollTo({top:0,behavior:"smooth"});
}
document.getElementById("sxs").onclick=()=>{sxs=!sxs;render();};
render();
</script>
"""

if __name__ == "__main__":
    sys.exit(main())
