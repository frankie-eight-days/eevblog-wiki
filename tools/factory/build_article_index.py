#!/usr/bin/env python3
"""Build site/articles.html -- a browsable index of every written article.

Self-contained: all article text is inlined, so the page works from a file://
path or a static host with no backend. Citations link into the video at the
moment the claim came from, the same as the bakeoff page.

  python3 tools/factory/build_article_index.py [out.html]
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
ARTS = ROOT / "articles/factory/articles"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_review_page import md, video_links               # noqa: E402
from verify_article import verify                           # noqa: E402


def main():
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site/articles.html"
    links = video_links()
    rows = []
    for p in sorted(ARTS.glob("*.md")):
        parts = p.name.split(".")
        if len(parts) < 3:
            continue
        concept, model = parts[0], parts[-2]
        text = p.read_text()
        v = verify(p)
        # first sentence of the body, as a card blurb
        body = re.sub(r"^#.*$", "", text, flags=re.M).strip()
        first = re.sub(r"\[\d+\]|\[[A-Za-z0-9_-]{6,}\]", "", body.split("\n")[0])
        rows.append({
            "c": concept, "m": model,
            "t": concept.replace("-", " "),
            "w": v["words"], "ci": v["citations"], "u": v["citations_distinct"],
            "s": v["sections"], "q": v["quotes"],
            "bad": v["quotes_bad"] + v["citations_bad"],
            "blurb": first[:240],
            "html": md(text, links),
        })
    rows.sort(key=lambda r: -r["w"])
    page = TEMPLATE.replace("__D__", json.dumps(rows, separators=(",", ":")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print(f"{len(rows)} articles, {sum(r['w'] for r in rows):,} words -> {out} "
          f"({out.stat().st_size/1e6:.2f} MB)")
    return 0


TEMPLATE = r"""<title>EEVblog Wiki — articles</title>
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
.wrap{max-width:1150px;margin:0 auto;padding:0 22px}
header{border-bottom:3px solid var(--accent);background:var(--panel);
  position:sticky;top:0;z-index:20}
header .wrap{display:flex;align-items:center;gap:14px;padding:12px 22px;
  flex-wrap:wrap}
h1.t{font-size:17px;margin:0;cursor:pointer}
h1.t b{color:var(--accent-ink)}
.grow{flex:1}
.sub{font-family:var(--mono);font-size:11px;color:var(--ink-soft);
  text-transform:uppercase;letter-spacing:.08em}
input,select{font-family:var(--sans);font-size:14px;padding:7px 10px;
  border:1px solid var(--rule);border-radius:2px;background:var(--ground);
  color:var(--ink)}
input:focus,select:focus{outline:none;border-color:var(--accent)}
#q{width:230px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
  gap:14px;margin:22px 0 60px}
.card{border:1px solid var(--rule);border-radius:3px;padding:14px 16px;
  background:var(--ground);cursor:pointer;display:flex;flex-direction:column;
  gap:7px}
.card:hover{border-color:var(--accent);background:var(--panel)}
.ct{font-size:16px;font-weight:600;letter-spacing:.01em}
.cm{font-family:var(--mono);font-size:10px;text-transform:uppercase;
  letter-spacing:.07em;color:var(--ink-faint);display:flex;gap:9px;
  flex-wrap:wrap;font-variant-numeric:tabular-nums}
.cm .model{color:var(--accent-ink);font-weight:700}
.cb{font-size:13px;color:var(--ink-soft);line-height:1.45;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;
  overflow:hidden}
.flag{color:var(--bad);font-weight:700}
/* article view */
#view{display:none;padding-bottom:70px}
.back{font-family:var(--mono);font-size:11.5px;text-transform:uppercase;
  letter-spacing:.07em;color:var(--accent-ink);cursor:pointer;
  display:inline-block;margin:20px 0 4px}
.meta{font-family:var(--mono);font-size:11px;color:var(--ink-faint);
  text-transform:uppercase;letter-spacing:.07em;margin-bottom:10px;
  padding-bottom:10px;border-bottom:1px solid var(--rule)}
.body{font-family:var(--serif);font-size:17px;line-height:1.64;max-width:68ch}
.body h1{font-family:var(--sans);font-size:24px;margin:14px 0 10px}
.body h2{font-family:var(--sans);font-size:15px;margin:28px 0 7px;
  text-transform:uppercase;letter-spacing:.07em;color:var(--accent-ink)}
.body h3{font-family:var(--sans);font-size:15px;margin:18px 0 4px}
.body p{margin:0 0 14px}
.body ul{margin:0 0 14px 18px;padding:0}
sup.c{font-family:var(--mono);font-size:9.5px;vertical-align:2px;line-height:0}
sup.c a{color:var(--accent-ink);text-decoration:none;padding:0 1px}
sup.c a:hover{background:var(--accent);color:#1b1a17;border-radius:2px}
sup.c-bad{color:var(--bad)}
</style>

<header><div class="wrap">
  <h1 class="t" id="home">EEVblog <b>Wiki</b></h1>
  <span class="sub" id="count"></span>
  <span class="grow"></span>
  <input id="q" placeholder="search articles…" autocomplete="off">
  <select id="mo"><option value="">both writers</option></select>
  <select id="so">
    <option value="w">longest</option>
    <option value="u">most videos cited</option>
    <option value="ci">most citations</option>
    <option value="t">A–Z</option>
  </select>
</div></header>

<div class="wrap">
  <div class="grid" id="grid"></div>
  <div id="view"></div>
</div>

<script>
const D = __D__;
const grid=document.getElementById("grid"), view=document.getElementById("view"),
      q=document.getElementById("q"), mo=document.getElementById("mo"),
      so=document.getElementById("so"), count=document.getElementById("count");
[...new Set(D.map(d=>d.m))].sort().forEach(m=>{
  const o=document.createElement("option");o.value=m;o.textContent=m;mo.append(o);});

function list(){
  view.style.display="none"; grid.style.display="";
  const t=q.value.trim().toLowerCase(), m=mo.value, k=so.value;
  const rows=D.filter(d=>(!m||d.m===m)&&(!t||d.t.includes(t)||d.blurb.toLowerCase().includes(t)))
    .sort((a,b)=> k==="t" ? a.t.localeCompare(b.t) : b[k]-a[k]);
  count.textContent=`${rows.length} of ${D.length} articles · ${D.reduce((s,d)=>s+d.w,0).toLocaleString()} words`;
  grid.innerHTML=rows.map(d=>`<div class="card" data-k="${d.c}.${d.m}">
      <div class="ct">${d.t}</div>
      <div class="cm"><span class="model">${d.m}</span>
        <span>${d.w.toLocaleString()} words</span>
        <span>${d.ci} cites / ${d.u} videos</span>
        <span>${d.s} sections</span>
        ${d.bad?`<span class="flag">${d.bad} unverified</span>`:""}</div>
      <div class="cb">${d.blurb}</div></div>`).join("");
}
grid.addEventListener("click",e=>{
  const c=e.target.closest(".card"); if(!c) return;
  const d=D.find(x=>`${x.c}.${x.m}`===c.dataset.k);
  grid.style.display="none"; view.style.display="block";
  view.innerHTML=`<span class="back" id="back">&larr; all articles</span>
    <div class="meta">${d.m} · ${d.w.toLocaleString()} words · ${d.ci} citations
      across ${d.u} videos · ${d.q} quotations${d.bad?` · <span class="flag">${d.bad} unverified</span>`:" · all verified"}</div>
    <div class="body">${d.html}</div>`;
  document.getElementById("back").onclick=list;
  scrollTo({top:0});
});
document.getElementById("home").onclick=list;
q.oninput=list; mo.onchange=list; so.onchange=list;
list();
</script>
"""

if __name__ == "__main__":
    sys.exit(main())
