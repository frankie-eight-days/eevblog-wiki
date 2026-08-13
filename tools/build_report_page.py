#!/usr/bin/env python3
"""Build the shareable one-page report: concept graph + article candidates.

Distinct from build_explore.py, which ports the Amp Hour explorer as a
full-viewport app. This is a document you can send someone: the graph sits in a
fixed panel at the top, the ranked article list runs underneath it, and the two
are linked -- clicking a node filters the list, clicking a row locates the node.

Self-contained (data inlined, no external requests) so it can be published as-is.

  python3 tools/build_report_page.py [out.html]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE_MIN = 3        # visual prune only; the real graph keeps weight>=2
MIN_EXPLAINS = 15   # the article gate; the same cut the Amp Hour wiki used


def island_layout(nodes, edges, pad=0.055, iters=600):
    """Place each community as its own island. VISUAL ONLY, disclosed on the page.

    LinLog is a faithful global layout, but this corpus is one connected mass --
    everything on the channel touches electronics -- so it packs 5,042 nodes into
    a disc where all 57 community centroids sit near the origin. Nothing that
    merely nudges those centroids can separate them; measured, a 42% outward push
    moved the picture not at all.

    So the communities are laid out as a graph in their own right: centroids
    repel until their discs no longer overlap, and inter-community edge weight
    pulls related ones together. Each node then keeps its LinLog position
    RELATIVE to its own community, rescaled into that community's disc -- so
    internal structure and cluster adjacency both survive, and cross-cluster
    edges are still drawn from the real topology. A bad grouping shows up as a
    thick bundle of edges between two islands, not as something this hides.
    """
    import numpy as np

    comms = sorted({n["c"] for n in nodes})
    ci = {c: k for k, c in enumerate(comms)}
    C = len(comms)
    grp = np.array([ci[n["c"]] for n in nodes])
    P = np.array([[n["x"], n["y"]] for n in nodes], dtype=float)

    size = np.bincount(grp, minlength=C).astype(float)
    cen = np.zeros((C, 2))
    for k in range(C):
        cen[k] = P[grp == k].mean(0)
    # area proportional to membership, so a 500-node cluster is not drawn the
    # same size as a 6-node one
    rad = np.sqrt(size); rad /= rad.max(); rad *= 0.30

    # inter-community attraction, weighted by how many edges actually cross
    W = np.zeros((C, C))
    for a, b, w in edges:
        ga, gb = grp[a], grp[b]
        if ga != gb:
            W[ga, gb] += w; W[gb, ga] += w
    if W.max() > 0:
        W /= W.max()

    # seed on the LinLog centroids (keeps real adjacency), then relax
    cen = cen - cen.mean(0)
    cen *= 1.6
    for it in range(iters):
        d = cen[:, None, :] - cen[None, :, :]
        dist = np.sqrt((d ** 2).sum(-1)) + 1e-9
        need = rad[:, None] + rad[None, :] + pad
        # separation: push apart only where discs overlap
        over = np.maximum(need - dist, 0.0)
        np.fill_diagonal(over, 0.0)
        push = (d / dist[:, :, None]) * over[:, :, None] * 0.5
        # cohesion: pull linked communities together, but never inside contact
        slack = np.maximum(dist - need, 0.0)
        pull = -(d / dist[:, :, None]) * (W * slack * 0.035)[:, :, None]
        cen += (push + pull).sum(1)
        # gravity. Without it the ~8 communities that share no edge with anything
        # else feel only repulsion and drift off forever, and normalising to the
        # extent then shrinks the real graph to a speck in the middle.
        cen -= cen * 0.012
        cen -= cen.mean(0)

    out = np.zeros_like(P)
    for k in range(C):
        m = grp == k
        loc = P[m] - P[m].mean(0)
        # Whiten per axis. A community sitting on the rim of the LinLog disc is
        # stretched into a thin arc; dropped into a round island unchanged it
        # renders as a crescent and the internal structure is unreadable. Scaling
        # each axis by its own spread makes the island fill its disc while
        # keeping every node's position relative to its neighbours.
        sd = loc.std(0)
        sd[sd < 1e-9] = 1.0
        loc = loc / sd
        s = np.abs(loc).max()
        loc = loc / s * rad[k] * 0.92 if s > 1e-9 else loc
        out[m] = cen[k] + loc
    out -= out.mean(0)
    # Scale so the whole graph fits the panel on load. Earlier this used a 98th
    # percentile, which left the top island clipped off the canvas -- the extent
    # is the only thing that guarantees nothing is cut, and gravity has already
    # stopped any island running away far enough to shrink the rest.
    out /= np.abs(out).max() or 1.0
    return [(round(float(x), 4), round(float(y), 4)) for x, y in out]


def main():
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site/report.html"
    layout = json.loads((ROOT / "graph/layout.json").read_text())
    cand = json.loads((ROOT / "articles/candidates.json").read_text())["candidates"]

    nodes = layout["nodes"]
    idx = {n["i"]: k for k, n in enumerate(nodes)}
    sizes = {}
    for n in nodes:
        sizes[n["c"]] = sizes.get(n["c"], 0) + 1
    comms = sorted(layout.get("communities", {}).items(),
                   key=lambda kv: -sizes.get(int(kv[0]), 0))

    # explains per concept, for node colouring and the list
    expl = {c["concept"]: c["explains_count"] for c in cand}

    pos = island_layout(nodes, layout["edges"])

    G = {
        "n": [[n["i"], round(pos[k][0], 3), round(pos[k][1], 3), n["c"], n["e"],
               expl.get(n["i"], 0)] for k, n in enumerate(nodes)],
        "e": [[a, b] for a, b, w in layout["edges"] if w >= EDGE_MIN],
        "c": [{"id": int(c), "label": ", ".join(m[:3]), "size": sizes.get(int(c), 0)}
              for c, m in comms],
    }
    arts = [{"c": a["concept"], "t": a["type"], "v": a["video_count"],
             "x": a["explains_count"], "o": a["opinion_count"],
             "m": a["mention_count"], "s": a["score"],
             "i": idx.get(a["concept"], -1),
             "ti": a.get("sample_titles", [])[:3]}
            # filter FIRST, then take everything -- slicing by score before the
            # explains gate silently dropped 75 qualifying concepts, because a
            # high-explains/low-breadth concept ranks poorly on score
            for a in cand if a["explains_count"] >= MIN_EXPLAINS]

    html = TEMPLATE.replace("__G__", json.dumps(G, separators=(",", ":"))) \
                   .replace("__A__", json.dumps(arts, separators=(",", ":"))) \
                   .replace("__NV__", f"{len(nodes):,}") \
                   .replace("__NE__", f"{len(layout['edges']):,}") \
                   .replace("__NC__", str(len(comms))) \
                   .replace("__NA__", f"{len(arts):,}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(f"{len(nodes):,} nodes / {len(G['e']):,} drawn edges / {len(arts):,} "
          f"articles -> {out} ({out.stat().st_size/1e6:.2f} MB)")
    return 0


TEMPLATE = r"""<title>EEVblog Wiki — concept graph &amp; article candidates</title>
<style>
:root{
  --ground:#fffefb; --ink:#1b1a17; --ink-soft:#5d5a52; --ink-faint:#938f85;
  --panel:#f4f2ec; --rule:#ded9cf; --accent:#ff8500; --accent-ink:#a34e00;
  --screen:#141310; --screen-grid:#2a2722; --screen-ink:#e8e3d7;
  --good:#3f7d4e;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sans:system-ui,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#131210; --ink:#eceae4; --ink-soft:#a8a49a; --ink-faint:#767268;
  --panel:#1c1b18; --rule:#33312b; --accent:#ff9a2e; --accent-ink:#ffb055;
  --good:#6fae7c;
}}
:root[data-theme="dark"]{
  --ground:#131210; --ink:#eceae4; --ink-soft:#a8a49a; --ink-faint:#767268;
  --panel:#1c1b18; --rule:#33312b; --accent:#ff9a2e; --accent-ink:#ffb055;
  --good:#6fae7c;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}

header{border-bottom:3px solid var(--accent);background:var(--panel)}
header .wrap{display:flex;justify-content:space-between;align-items:baseline;
  gap:16px;padding-top:16px;padding-bottom:14px;flex-wrap:wrap}
h1{font-size:19px;margin:0;letter-spacing:.01em}
h1 b{color:var(--accent-ink)}
.sub{font-family:var(--mono);font-size:11.5px;color:var(--ink-soft);
  text-transform:uppercase;letter-spacing:.09em}

.lede{max-width:65ch;margin:26px 0 20px;color:var(--ink-soft);font-size:15.5px}
.lede strong{color:var(--ink)}

/* ---- scope screen ---- */
.screen{position:relative;background:var(--screen);border:1px solid var(--rule);
  border-radius:3px;overflow:hidden;margin:0 0 6px}
.screen canvas{display:block;width:100%;height:640px;cursor:grab}
.screen canvas.drag{cursor:grabbing}
.hud{position:absolute;top:10px;left:12px;right:12px;display:flex;gap:8px;
  align-items:center;flex-wrap:wrap;pointer-events:none}
.hud > *{pointer-events:auto}
.find{font-family:var(--mono);font-size:12.5px;padding:7px 10px;width:210px;
  background:#00000066;color:var(--screen-ink);border:1px solid #ffffff2e;
  border-radius:2px}
.find:focus{outline:none;border-color:var(--accent)}
.find::placeholder{color:#ffffff66}
.btn{font-family:var(--mono);font-size:11.5px;text-transform:uppercase;
  letter-spacing:.07em;padding:7px 11px;background:#00000066;color:var(--screen-ink);
  border:1px solid #ffffff2e;border-radius:2px;cursor:pointer}
.btn:hover{border-color:var(--accent);color:#fff}
.btn[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#1b1a17}
.tip{position:absolute;pointer-events:none;background:#000000d9;color:#fff;
  border:1px solid #ffffff33;border-radius:2px;padding:7px 9px;font-size:12.5px;
  max-width:260px;display:none;z-index:5}
.tip b{color:var(--accent)}
.tip .r{font-family:var(--mono);font-size:11px;color:#c9c4b8;display:block;margin-top:3px}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-family:var(--mono);
  font-size:11px;color:var(--ink-faint);margin:0 0 26px;
  text-transform:uppercase;letter-spacing:.06em}
.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;
  margin-right:5px;vertical-align:-1px}

/* ---- table ---- */
h2{font-size:16px;margin:34px 0 4px;letter-spacing:.01em}
h2 + p{margin:0 0 16px;color:var(--ink-soft);max-width:65ch}
.controls{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 12px}
.controls input,.controls select{font-family:var(--sans);font-size:14px;
  padding:8px 10px;border:1px solid var(--rule);border-radius:2px;
  background:var(--ground);color:var(--ink)}
.controls input:focus,.controls select:focus{outline:none;border-color:var(--accent)}
.count{font-family:var(--mono);font-size:11.5px;color:var(--ink-faint);
  text-transform:uppercase;letter-spacing:.07em}
.tbl{width:100%;border-collapse:collapse;font-size:14.5px}
.tbl th{text-align:left;font-family:var(--mono);font-size:10.5px;
  text-transform:uppercase;letter-spacing:.08em;color:var(--ink-faint);
  border-bottom:1px solid var(--rule);padding:0 10px 7px 0;cursor:pointer;
  white-space:nowrap;font-weight:600}
.tbl th:hover{color:var(--accent-ink)}
.tbl th[data-on]{color:var(--accent-ink)}
.tbl td{border-bottom:1px solid var(--rule);padding:9px 10px 9px 0;
  vertical-align:top}
.tbl tr:hover td{background:var(--panel)}
.num{font-family:var(--mono);font-variant-numeric:tabular-nums;text-align:right;
  white-space:nowrap}
.rank{color:var(--ink-faint);width:44px}
.name{font-weight:600}
.name button{all:unset;cursor:pointer;font-weight:600}
.name button:hover{color:var(--accent-ink);text-decoration:underline}
.chip{display:inline-block;font-family:var(--mono);font-size:10px;
  text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft);
  border:1px solid var(--rule);border-radius:2px;padding:1px 5px;margin-left:7px;
  vertical-align:1px}
.bar{position:relative;height:5px;background:var(--rule);border-radius:3px;
  width:110px;margin-top:6px;overflow:hidden}
.bar i{position:absolute;inset:0 auto 0 0;background:var(--accent);border-radius:3px}
.ti{font-size:12.5px;color:var(--ink-faint);margin-top:5px;display:none}
tr.open .ti{display:block}
footer{margin:44px 0 60px;padding-top:18px;border-top:1px solid var(--rule);
  font-size:13px;color:var(--ink-faint);max-width:70ch}
@media(max-width:720px){
  .screen canvas{height:380px}
  .hide-sm{display:none}
}
</style>

<header><div class="wrap">
  <h1>EEVblog <b>Wiki</b> — concept graph</h1>
  <div class="sub">__NV__ concepts · __NE__ links · __NC__ clusters · 2,846 videos</div>
</div></header>

<div class="wrap">
<p class="lede">Every concept the census found across the whole EEVblog corpus,
placed by what Dave talks about <strong>alongside</strong> what. Nothing here was
categorised by hand — the clusters fell out of co-occurrence, and they landed on
the bench: scopes in one, PCB layout in another, RF off on its own.
<strong>Brightness is teaching</strong>, not frequency: a bright node is one he
<em>explains</em> rather than merely names. Clusters are drawn pushed apart from
each other for legibility — positions within a cluster, and every link, are the
real ones.</p>

<div class="screen">
  <canvas id="cv"></canvas>
  <div class="hud">
    <input id="find" class="find" placeholder="find a concept…" autocomplete="off">
    <button class="btn" id="bExp" aria-pressed="true">colour: explains</button>
    <button class="btn" id="bReset">reset view</button>
    <span class="btn hide-sm" id="sel" style="cursor:default">drag to pan · scroll to zoom</span>
  </div>
  <div class="tip" id="tip"></div>
</div>
<div class="legend">
  <span><i style="background:#3a3630"></i>named only</span>
  <span><i style="background:#8a5a1e"></i>explained sometimes</span>
  <span><i style="background:#ff8500"></i>explained often</span>
  <span style="margin-left:auto">node size = videos it appears in</span>
</div>

<h2>Article candidates, ranked by explanations</h2>
<p>__NA__ concepts clear the bar of <strong>15+ explanatory mentions</strong> — the
same cut that produced 412 articles on the Amp Hour wiki. Sorted by explains, not
by how often a thing gets mentioned, because a part Dave name-drops in passing
makes a thin article and one he keeps teaching makes a good one.</p>

<div class="controls">
  <input id="q" placeholder="filter concepts…" autocomplete="off">
  <select id="ty"><option value="">all types</option></select>
  <span class="count" id="cnt"></span>
</div>
<table class="tbl">
  <thead><tr>
    <th class="rank">#</th>
    <th data-k="c">concept</th>
    <th class="num" data-k="x" data-on="1">explains</th>
    <th class="num" data-k="v">videos</th>
    <th class="num hide-sm" data-k="o">opinions</th>
    <th class="num hide-sm" data-k="m">mentions</th>
  </tr></thead>
  <tbody id="tb"></tbody>
</table>

<footer>Generated from 2,846 transcribed EEVblog videos. Concepts were extracted
per-paragraph, folded into canonical names, then linked by co-occurrence within
±2 paragraphs. “Explains” counts only mentions where the concept itself is being
taught — which is why teardown-style and travel material, carried by narrative
rather than by explanation, is deliberately absent from this ranking.</footer>
</div>

<script>
const G = __G__, A = __A__;
const NODES = G.n, EDGES = G.e;
const N = NODES.length;
const NAME=[],X=[],Y=[],COM=[],EP=[],EXP=[];
for (let i=0;i<N;i++){const n=NODES[i];NAME.push(n[0]);X.push(n[1]);Y.push(n[2]);
  COM.push(n[3]);EP.push(n[4]);EXP.push(n[5]);}
const byName = new Map(NAME.map((n,i)=>[n,i]));
const maxExp = Math.max(1,...EXP);

const cv=document.getElementById("cv"), ctx=cv.getContext("2d");
const tip=document.getElementById("tip");
let W=0,H=0,DPR=1;
let view={s:1,x:0,y:0}, base=1, hover=-1, pick=-1, colourExp=true;

// community hues, spread so adjacent ids are not adjacent colours
const CH={}; const CC=G.c.length;
G.c.forEach((c,k)=>{CH[c.id]=(k*360/CC*2.39)%360;});

function fit(){
  DPR=Math.min(2,window.devicePixelRatio||1);
  W=cv.clientWidth;H=cv.clientHeight;
  cv.width=W*DPR;cv.height=H*DPR;ctx.setTransform(DPR,0,0,DPR,0,0);
  // HUD_TOP is reserved in world space, not just painted over: the search row
  // sits on top of the canvas, and without this the highest island (scopes, the
  // biggest cluster in the corpus) renders underneath the buttons.
  base=Math.min(W,H-HUD_TOP-16)/2.15;
  draw();
}
const HUD_TOP=52;
const px=i=>X[i]*base*view.s+W/2+view.x;
const py=i=>Y[i]*base*view.s+(H+HUD_TOP)/2+view.y;
const rad=i=>Math.max(1.3,Math.sqrt(EP[i])*0.34*Math.max(1,Math.sqrt(view.s)));

function colour(i,dim){
  if(colourExp){
    const t=Math.min(1,Math.sqrt(EXP[i]/maxExp)*1.35);
    const l=(14+t*46)|0, s=(t*88)|0, h=26+t*8;
    return `hsl(${h} ${s}% ${l}% / ${dim?0.5:1})`;
  }
  return `hsl(${CH[COM[i]]|0} 58% ${dim?32:58}% / ${dim?0.55:1})`;
}

function draw(){
  ctx.fillStyle="#141310";ctx.fillRect(0,0,W,H);
  // graticule — a scope screen, not a whiteboard
  ctx.strokeStyle="#232019";ctx.lineWidth=1;ctx.beginPath();
  for(let g=0;g<=10;g++){const gx=W*g/10,gy=H*g/10;
    ctx.moveTo(gx,0);ctx.lineTo(gx,H);ctx.moveTo(0,gy);ctx.lineTo(W,gy);}
  ctx.stroke();

  const nb = pick>=0 ? NEI.get(pick) : null;
  // Edge alpha scales with zoom. At full extent 7,757 lines over 5,042 nodes is
  // a grey fog that hides every node under it; the structure only becomes
  // readable once you are close enough for individual links to mean something.
  ctx.lineWidth=Math.min(1.1,0.5*view.s);
  ctx.strokeStyle = view.s<1.4 ? "#ffffff07" : (view.s<3 ? "#ffffff10" : "#ffffff1c");
  ctx.beginPath();
  for(let e=0;e<EDGES.length;e++){
    const a=EDGES[e][0],b=EDGES[e][1];
    if(nb && !(a===pick||b===pick)) continue;
    const ax=px(a),ay=py(a);
    if(ax<-60||ax>W+60||ay<-60||ay>H+60){const bx=px(b),by=py(b);
      if(bx<-60||bx>W+60||by<-60||by>H+60) continue;}
    ctx.moveTo(ax,ay);ctx.lineTo(px(b),py(b));
  }
  if(nb){ctx.strokeStyle="#ff850099";ctx.lineWidth=1.2;}
  ctx.stroke();

  for(let i=0;i<N;i++){
    const x=px(i),y=py(i);
    if(x<-20||x>W+20||y<-20||y>H+20) continue;
    const dim = nb ? !(i===pick||nb.has(i)) : false;
    ctx.fillStyle=colour(i,dim);
    ctx.beginPath();ctx.arc(x,y,rad(i),0,6.2832);ctx.fill();
  }
  // labels for the biggest nodes on screen, with an occupancy grid so they
  // never stack — the failure mode of every force-directed graph render
  const cell=[],CW=124,CHh=21;
  const order=[...Array(N).keys()].sort((a,b)=>EP[b]-EP[a]);
  ctx.font="600 12px "+getComputedStyle(document.body).getPropertyValue("--sans");
  const cap = view.s<1.4 ? 30 : (view.s<3 ? 55 : 85);
  let drawn=0;
  for(const i of order){
    if(drawn>cap) break;
    const x=px(i),y=py(i);
    if(x<0||x>W||y<0||y>H) continue;
    if(nb && !(i===pick||nb.has(i))) continue;
    if(view.s<1.25 && EP[i]<40 && i!==pick) continue;
    // reserve the cell to the right as well: labels run rightward from the node,
    // so a one-cell claim lets the next label start inside this one's text
    const cxi=(x/CW)|0, cyi=(y/CHh)|0;
    if(cell[cxi+","+cyi]||cell[(cxi+1)+","+cyi]) continue;
    cell[cxi+","+cyi]=1; cell[(cxi+1)+","+cyi]=1;
    const t=NAME[i].replace(/-/g," ");
    ctx.fillStyle="#0b0a08";ctx.fillText(t,x+rad(i)+4,y+4.5);
    ctx.fillStyle= i===pick?"#ff9a2e":"#e8e3d7";
    ctx.fillText(t,x+rad(i)+3,y+3.5);
    drawn++;
  }
}

// adjacency, for click-to-isolate
const NEI=new Map();
{const m=new Map();
 for(const [a,b] of EDGES){
   if(!m.has(a))m.set(a,new Set()); if(!m.has(b))m.set(b,new Set());
   m.get(a).add(b);m.get(b).add(a);}
 for(const [k,v] of m) NEI.set(k,v);}

function nearest(mx,my){
  let best=-1,bd=18*18;
  for(let i=0;i<N;i++){
    const dx=px(i)-mx,dy=py(i)-my,d=dx*dx+dy*dy;
    const r=rad(i)+5;
    if(d<Math.max(bd,r*r)&&d<400){bd=d;best=i;}
  }
  return best;
}

let drag=null;
cv.addEventListener("mousedown",e=>{drag={x:e.offsetX,y:e.offsetY,vx:view.x,vy:view.y,moved:0};
  cv.classList.add("drag");});
addEventListener("mouseup",()=>{if(drag&&drag.moved<4){const i=nearest(drag.x,drag.y);
    pick = (i>=0&&i!==pick)?i:-1; sync(); }
  drag=null;cv.classList.remove("drag");});
cv.addEventListener("mousemove",e=>{
  const mx=e.offsetX,my=e.offsetY;
  if(drag){drag.moved+=Math.abs(e.movementX)+Math.abs(e.movementY);
    view.x=drag.vx+(mx-drag.x);view.y=drag.vy+(my-drag.y);draw();return;}
  const i=nearest(mx,my);
  if(i!==hover){hover=i;
    if(i<0){tip.style.display="none";}
    else{
      tip.innerHTML=`<b>${NAME[i].replace(/-/g," ")}</b>`+
        `<span class="r">${EP[i]} videos · ${EXP[i]} explains</span>`;
      tip.style.display="block";
      tip.style.left=Math.min(W-270,mx+14)+"px";
      tip.style.top=Math.max(4,my-10)+"px";
    }}
});
cv.addEventListener("mouseleave",()=>{tip.style.display="none";hover=-1;});
cv.addEventListener("wheel",e=>{
  e.preventDefault();
  const k=Math.exp(-e.deltaY*0.0016), ns=Math.min(14,Math.max(0.55,view.s*k));
  const mx=e.offsetX-W/2, my=e.offsetY-(H+HUD_TOP)/2;
  view.x=mx-(mx-view.x)*(ns/view.s); view.y=my-(my-view.y)*(ns/view.s);
  view.s=ns; draw();
},{passive:false});

function focusNode(i){
  pick=i; view.s=3.4;
  view.x=-X[i]*base*view.s; view.y=-Y[i]*base*view.s;
  sync(); cv.scrollIntoView({behavior:"smooth",block:"center"});
}
function sync(){
  document.getElementById("sel").textContent =
    pick>=0 ? NAME[pick].replace(/-/g," ")+" — "+(NEI.get(pick)?.size||0)+" links (click again to clear)"
            : "drag to pan · scroll to zoom";
  draw();
}
document.getElementById("bExp").onclick=e=>{
  colourExp=!colourExp; e.target.setAttribute("aria-pressed",colourExp);
  e.target.textContent="colour: "+(colourExp?"explains":"cluster"); draw();};
document.getElementById("bReset").onclick=()=>{view={s:1,x:0,y:0};pick=-1;sync();};
document.getElementById("find").addEventListener("input",e=>{
  const v=e.target.value.trim().toLowerCase().replace(/ /g,"-");
  if(!v) return;
  let i = byName.get(v);
  if(i===undefined){for(let k=0;k<N;k++) if(NAME[k].startsWith(v)){i=k;break;}}
  if(i!==undefined) focusNode(i);
});

// ---- article table ----
const tb=document.getElementById("tb"), q=document.getElementById("q"),
      ty=document.getElementById("ty"), cnt=document.getElementById("cnt");
[...new Set(A.map(a=>a.t))].sort().forEach(t=>{
  const o=document.createElement("option");o.value=t;o.textContent=t;ty.append(o);});
let sortK="x", desc=true;
const maxX=Math.max(...A.map(a=>a.x));

function render(){
  const term=q.value.trim().toLowerCase(), t=ty.value;
  const rows=A.filter(a=>(!t||a.t===t)&&(!term||a.c.includes(term)))
    .sort((p,r)=>{const d=typeof p[sortK]==="string"
      ? p[sortK].localeCompare(r[sortK]) : p[sortK]-r[sortK]; return desc?-d:d;});
  cnt.textContent=rows.length+" of "+A.length+" concepts";
  tb.innerHTML=rows.map((a,k)=>`<tr>
    <td class="num rank">${k+1}</td>
    <td class="name">${a.i>=0?`<button data-i="${a.i}">${a.c.replace(/-/g," ")}</button>`
        :a.c.replace(/-/g," ")}<span class="chip">${a.t}</span>
      <div class="bar"><i style="width:${(a.x/maxX*100).toFixed(1)}%"></i></div>
      <div class="ti">${a.ti.map(s=>s.replace(/&/g,"&amp;").replace(/</g,"&lt;")).join(" · ")}</div></td>
    <td class="num">${a.x}</td><td class="num">${a.v}</td>
    <td class="num hide-sm">${a.o}</td><td class="num hide-sm">${a.m}</td></tr>`).join("");
}
document.querySelectorAll(".tbl th[data-k]").forEach(th=>{
  th.onclick=()=>{const k=th.dataset.k;
    if(k===sortK) desc=!desc; else {sortK=k;desc=k!=="c";}
    document.querySelectorAll(".tbl th").forEach(o=>o.removeAttribute("data-on"));
    th.setAttribute("data-on","1"); render();};
});
tb.addEventListener("click",e=>{
  const b=e.target.closest("button[data-i]");
  if(b){focusNode(+b.dataset.i);return;}
  const tr=e.target.closest("tr"); if(tr) tr.classList.toggle("open");
});
q.oninput=render; ty.onchange=render;

render(); addEventListener("resize",fit); fit();
</script>
"""

if __name__ == "__main__":
    sys.exit(main())
