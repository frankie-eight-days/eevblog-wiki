#!/usr/bin/env python3
"""Generate the static transcript site: one HTML page per video plus a
searchable index.

Why this exists: YouTube does not expose captions as indexable page content, so
~8 million words of Dave talking about electronics are invisible to Google.
These pages make that text crawlable, which is the whole point of the
static-HTML constraint. Every paragraph deep-links back to the second it was
spoken, so a page is a navigation aid for the video rather than a replacement.

Output (all relative links, no server needed, no external requests):

  site/transcripts/index.html       search over every video
  site/transcripts/t/<video_id>.html

Styling follows eevblog.com's live theme (Sahifa): white ground, #2A2A2A bar,
#FF8500 accent, Droid-Sans-ish system stack. Single-theme on purpose -- it is
meant to sit beside a light site.
"""
import csv, html, json, pathlib, re, sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site/transcripts"
SRC = [(ROOT / "transcripts", "captions"), (ROOT / "transcripts_whisper", "whisper")]
CENSUS = [ROOT / "census/captions-v1", ROOT / "census/full-v1"]
TOP_CONCEPTS = 10          # per video, for the search index

CSS = """
:root{
  --ink:#2a2a2a; --ink-soft:#5a5a5a; --ink-faint:#8a8a8a;
  --ground:#ffffff; --panel:#f2f2f2; --rule:#d4d4d4;
  --accent:#ff8500; --accent-dark:#d97000; --bar:#2a2a2a;
  --font:"Droid Sans","Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--font);
     font-size:16px;line-height:1.65;-webkit-text-size-adjust:100%}
a{color:var(--accent-dark);text-decoration:none}
a:hover{text-decoration:underline}
.bar{background:var(--bar);border-bottom:3px solid var(--accent)}
.bar-in{max-width:1040px;margin:0 auto;padding:14px 20px;display:flex;
        align-items:baseline;gap:14px;flex-wrap:wrap}
.bar a.brand{color:#fff;font-weight:700;font-size:19px;letter-spacing:.2px}
.bar .tag{color:#cacaca;font-size:12.5px;text-transform:uppercase;letter-spacing:.7px}
.bar .spacer{flex:1}
.bar a.up{color:#cacaca;font-size:13.5px}
main{max-width:1040px;margin:0 auto;padding:26px 20px 70px}
h1{font-size:26px;line-height:1.3;margin:0 0 6px;text-wrap:balance}
.meta{color:var(--ink-soft);font-size:13.5px;margin-bottom:22px}
.meta span+span::before{content:"·";margin:0 8px;color:var(--ink-faint)}
.watch{display:inline-block;background:var(--accent);color:#fff;font-weight:700;
       font-size:13.5px;padding:7px 14px;border-radius:2px;margin-bottom:24px}
.watch:hover{background:var(--accent-dark);text-decoration:none}
/* transcript body */
.para{display:grid;grid-template-columns:64px 1fr;gap:14px;
      padding:7px 0;border-top:1px solid #efefef}
.para:first-of-type{border-top:0}
.para:target{background:#fff8ee}
.ts{font-size:12.5px;color:var(--ink-faint);padding-top:3px;
    font-variant-numeric:tabular-nums;white-space:nowrap}
.ts a{color:var(--ink-faint)}
.ts a:hover{color:var(--accent-dark)}
.para p{margin:0}
/* index */
.search{width:100%;padding:12px 14px;font-size:16px;font-family:inherit;
        border:2px solid var(--rule);border-radius:2px;background:#fff;color:var(--ink)}
.search:focus{outline:none;border-color:var(--accent)}
.count{color:var(--ink-soft);font-size:13.5px;margin:12px 0 18px;
       font-variant-numeric:tabular-nums}
ul.list{list-style:none;margin:0;padding:0}
ul.list li{border-top:1px solid var(--rule);padding:11px 0;
           display:grid;grid-template-columns:1fr auto;gap:16px;align-items:baseline}
ul.list li a{font-weight:600}
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:12px}
.controls label{font-size:12.5px;color:var(--ink-soft);text-transform:uppercase;
                letter-spacing:.5px}
.controls select{font-family:inherit;font-size:14px;padding:7px 9px;color:var(--ink);
                 border:1px solid var(--rule);border-radius:2px;background:#fff}
.controls select:focus{outline:none;border-color:var(--accent)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:12px 0 0}
.chip{font-family:inherit;font-size:12.5px;padding:5px 11px;border-radius:2px;
      border:1px solid var(--rule);background:#fff;color:var(--ink-soft);cursor:pointer;
      text-transform:uppercase;letter-spacing:.5px}
.chip:hover{border-color:var(--accent)}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);
                           color:#fff;font-weight:700}
.stat{color:var(--ink-soft);font-size:13px;font-variant-numeric:tabular-nums;
      white-space:nowrap;text-align:right}
.stat b{display:block;color:var(--ink);font-weight:600}
.tags{color:var(--ink-faint);font-size:12.5px;margin-top:2px}
.dur{color:var(--ink-soft);font-size:13px;font-variant-numeric:tabular-nums;
     white-space:nowrap}
.ch2{display:inline-block;background:var(--panel);color:var(--ink-soft);
     font-size:11px;padding:1px 6px;border-radius:2px;margin-left:7px;
     text-transform:uppercase;letter-spacing:.5px;vertical-align:1px}
.none{color:var(--ink-soft);padding:26px 0}
footer{border-top:1px solid var(--rule);margin-top:40px;padding-top:16px;
       color:var(--ink-faint);font-size:12.5px}
@media (max-width:620px){
  .para{grid-template-columns:52px 1fr;gap:10px}
  ul.list li{grid-template-columns:1fr}
  h1{font-size:22px}
}
"""


# The same title-keyword buckets used to scope the wiki's article lanes. A video
# can land in more than one (a "teardown and repair" is both); anything that
# matches nothing is simply unfiltered rather than forced into an "other".
CATEGORIES = [
    ("teardown", r"teardown|tear down|autopsy|what'?s inside|dumpster"),
    ("repair",   r"repair|fixing|\bfix(ed)?\b|restor|troubleshoot"),
    ("review",   r"review|shootout|compar|\bvs\b|unbox|first look|hands.?on"),
    ("tutorial", r"how (to|it works|does)|tutorial|explain|basics|fundamental|"
                 r"primer|design(ing)? a|part \d|lesson"),
    ("mailbag",  r"mailbag"),
    ("debunk",   r"\bfail\b|debunk|bust(ed|ing)?\b|scam|bogus|myth|snake ?oil|"
                 r"fake|nonsense|dodgy|rubbish|warning"),
    ("interview", r"interview|chat with|guest video"),
]


def categories(title):
    return " ".join(name for name, pat in CATEGORIES
                    if re.search(pat, title, re.I))


def hhmmss(s):
    s = int(s or 0)
    h, m = divmod(s // 60, 60)
    return f"{h}:{m:02d}:{s % 60:02d}" if h else f"{m}:{s % 60:02d}"


def shell(title, body, up=None, desc=""):
    """One page. No external requests -- fonts, CSS and data are all inline, so
    the directory can be dropped on any server or opened from disk."""
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<style>{CSS}</style>
</head><body>
<div class="bar"><div class="bar-in">
  <a class="brand" href="{'../index.html' if up else 'index.html'}">EEVblog Transcripts</a>
  <span class="tag">No Script, No Fear, All Opinion</span>
  <span class="spacer"></span>
  {'<a class="up" href="../index.html">&larr; All transcripts</a>' if up else ''}
</div></div>
<main>{body}</main>
</body></html>"""


def parse(path):
    """-> (frontmatter dict, [(seconds, text)])"""
    raw = path.read_text()
    if not raw.startswith("---"):
        return None, []
    end = raw.index("\n---", 3)
    fm = {}
    for line in raw[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    stamps = {}
    if fm.get("timestamps"):
        try:
            stamps = {int(k): v for k, v in json.loads(fm["timestamps"]).items()}
        except (ValueError, json.JSONDecodeError):
            stamps = {}
    paras = []
    for i, p in enumerate(re.findall(r"^\*\*[^:]+:\*\*\s*(.+)$",
                                     raw[end:], re.M)):
        paras.append((stamps.get(i), p.strip()))
    return fm, paras


def main():
    ledger = {}
    for f, ch in (("meta/ledger.tsv", ""), ("meta/ledger2.tsv", "2")):
        p = ROOT / f
        if p.exists():
            for r in csv.DictReader(open(p), delimiter="\t"):
                r["channel"] = ch
                ledger[r["id"]] = r

    # View counts come from one flat-playlist call per channel. Likes and upload
    # dates are NOT available that way -- they need a request per video, which is
    # ~2,900 hits on the same IP that is currently pulling audio, so they are
    # deliberately left out. `l` is carried through as null so a later polite
    # crawl can fill it in without changing this file's shape.
    views = {}
    vp = ROOT / "meta/views.txt"
    if vp.exists():
        for line in vp.read_text().splitlines():
            vid, _, v = line.partition("|")
            if v.isdigit():
                views[vid] = int(v)

    concepts = defaultdict(list)
    for cdir in CENSUS:
        for cf in cdir.glob("*.json"):
            if cf.name.startswith("_"):
                continue
            try:
                d = json.loads(cf.read_text())
            except json.JSONDecodeError:
                continue
            seen, order = set(), []
            for m in d.get("mentions", []):
                c = m.get("concept")
                if c and c not in seen:
                    seen.add(c); order.append(c)
            concepts[cf.stem] = (d.get("main_topics") or [])[:3] + order[:TOP_CONCEPTS]

    (OUT / "t").mkdir(parents=True, exist_ok=True)
    rows, n_ts = [], 0
    for src, kind in SRC:
        for path in sorted(src.glob("*.md")):
            vid = path.stem
            fm, paras = parse(path)
            if not paras:
                continue
            meta = ledger.get(vid, {})
            title = fm.get("title") or meta.get("title") or vid
            dur = int(meta.get("duration_s") or 0)
            words = sum(len(t.split()) for _, t in paras)
            has_ts = any(s is not None for s, _ in paras)
            n_ts += bool(has_ts)

            lines = []
            for i, (sec, text) in enumerate(paras):
                if sec is None:
                    stamp = ""
                else:
                    stamp = (f'<a href="https://www.youtube.com/watch?v={vid}'
                             f'&amp;t={int(sec)}s" target="_blank" rel="noopener"'
                             f' title="Play from {hhmmss(sec)}">{hhmmss(sec)}</a>')
                lines.append(f'<div class="para" id="p{i}"><div class="ts">{stamp}'
                             f'</div><p>{html.escape(text)}</p></div>')

            tags = sorted(set(concepts.get(vid, [])))
            body = (f"<h1>{html.escape(title)}</h1>"
                    f'<div class="meta"><span>{hhmmss(dur)}</span>'
                    f'<span>{words:,} words</span>'
                    f'<span>{len(paras):,} paragraphs</span>'
                    f'<span>source: {kind}</span></div>'
                    f'<a class="watch" href="https://www.youtube.com/watch?v={vid}"'
                    f' target="_blank" rel="noopener">Watch on YouTube</a>'
                    + "".join(lines)
                    + '<footer>Machine transcription. Timestamps link to the '
                      'moment in the video.</footer>')
            desc = f"Full transcript of {title}. " + " ".join(t for _, t in paras[:2])
            (OUT / "t" / f"{vid}.html").write_text(
                shell(title, body, up=True, desc=desc[:300]))

            num = re.search(r"#?\s*(\d{2,4})\b", title)
            rows.append({"i": vid, "t": title, "d": dur, "c": meta.get("channel", ""),
                         "w": words, "k": " ".join(tags),
                         "v": views.get(vid), "l": None,
                         "n": int(num.group(1)) if num else None,
                         "g": categories(title)})

    rows.sort(key=lambda r: r["t"])
    total_words = sum(r["w"] for r in rows)
    data = json.dumps(rows, separators=(",", ":"), ensure_ascii=False)
    # only offer a chip for a bucket that actually matched something
    live = [n for n, _ in CATEGORIES if any(n in r["g"] for r in rows)]
    cats = json.dumps(live)

    index_body = f"""
<h1>EEVblog video transcripts</h1>
<div class="meta"><span>{len(rows):,} videos</span><span>{total_words:,} words</span>
<span>search by title or topic</span></div>
<input class="search" id="q" type="search" autocomplete="off" autofocus
       placeholder="Search titles and topics &mdash; try &ldquo;multimeter teardown&rdquo; or &ldquo;fluke&rdquo;">
<div class="controls">
  <label for="sort">Sort</label>
  <select id="sort">
    <option value="v">Most viewed</option>
    <option value="n">Newest first</option>
    <option value="o">Oldest first</option>
    <option value="t">Title A&ndash;Z</option>
    <option value="d">Longest first</option>
    <option value="w">Most words</option>
  </select>
  <label for="ch">Channel</label>
  <select id="ch">
    <option value="">Both channels</option>
    <option value="1">EEVblog</option>
    <option value="2">EEVblog2</option>
  </select>
</div>
<div class="chips" id="chips"></div>
<div class="count" id="count"></div>
<ul class="list" id="list"></ul>
<footer>Every video with a usable transcript. Machine transcription; timestamps
deep-link into the video.</footer>
<script>
// The whole index is inlined: ~2,900 rows is small enough that filtering on
// every keystroke is instant, and it keeps the page a single self-contained
// file with no fetch (so it works from disk as well as over HTTP).
const D={data};
const CATS={cats};
const list=document.getElementById('list'),q=document.getElementById('q'),
      count=document.getElementById('count'),sortEl=document.getElementById('sort'),
      chEl=document.getElementById('ch'),chips=document.getElementById('chips');
let cat='';
const dur=s=>{{s=s|0;const h=(s/3600)|0,m=((s%3600)/60)|0;
  return h?h+':'+String(m).padStart(2,'0')+':'+String(s%60).padStart(2,'0')
          :m+':'+String(s%60).padStart(2,'0');}};
const nviews=v=>v==null?'':v>=1e6?(v/1e6).toFixed(1).replace(/\\.0$/,'')+'M'
                              :v>=1e3?Math.round(v/1e3)+'K':String(v);
const esc=s=>s.replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));

chips.innerHTML='<button class="chip" data-c="" aria-pressed="true">All</button>'+
  CATS.map(c=>'<button class="chip" data-c="'+c+'" aria-pressed="false">'+c+'</button>').join('');
chips.addEventListener('click',e=>{{
  const b=e.target.closest('.chip'); if(!b) return;
  cat=b.dataset.c;
  [...chips.children].forEach(x=>x.setAttribute('aria-pressed',x===b));
  apply();
}});

// Nulls sink to the bottom whatever the direction, so videos with no view count
// never crowd out the top of a "most viewed" sort.
function cmp(key,desc){{
  return (a,b)=>{{
    const x=a[key],y=b[key];
    if(x==null&&y==null) return a.t.localeCompare(b.t);
    if(x==null) return 1;
    if(y==null) return -1;
    if(typeof x==='string') return desc?y.localeCompare(x):x.localeCompare(y);
    return desc?y-x:x-y;
  }};
}}
const SORTS={{v:cmp('v',true),n:cmp('n',true),o:cmp('n',false),
             t:cmp('t',false),d:cmp('d',true),w:cmp('w',true)}};

function render(rs){{
  count.textContent=rs.length.toLocaleString()+
    (rs.length===D.length?' videos':' of '+D.length.toLocaleString()+' videos');
  if(!rs.length){{list.innerHTML='<li class="none">Nothing matches those filters.</li>';return;}}
  list.innerHTML=rs.slice(0,400).map(r=>
    '<li><div><a href="t/'+r.i+'.html">'+esc(r.t)+'</a>'+
    (r.c==='2'?'<span class="ch2">EEVblog2</span>':'')+
    (r.k?'<div class="tags">'+esc(r.k.split(' ').slice(0,8).join(' · ').replace(/-/g,' '))+'</div>':'')+
    '</div><div class="stat">'+(r.v!=null?'<b>'+nviews(r.v)+' views</b>':'')+
    dur(r.d)+'</div></li>').join('')+
    (rs.length>400?'<li class="none">Showing the first 400 &mdash; narrow it down to see more.</li>':'');
}}
// Every term must match somewhere, so words can be combined in any order
// ("teardown fluke" and "fluke teardown" find the same videos).
function apply(){{
  const terms=q.value.toLowerCase().split(/\\s+/).filter(Boolean);
  let rs=D;
  if(chEl.value) rs=rs.filter(r=>(r.c||'1')===chEl.value);
  if(cat) rs=rs.filter(r=>r.g.includes(cat));
  if(terms.length) rs=rs.filter(r=>{{const h=(r.t+' '+r.k).toLowerCase();
    return terms.every(t=>h.includes(t));}});
  render(rs.slice().sort(SORTS[sortEl.value]));
}}
q.addEventListener('input',apply);
sortEl.addEventListener('change',apply);
chEl.addEventListener('change',apply);
apply();
</script>"""
    (OUT / "index.html").write_text(shell(
        "EEVblog video transcripts", index_body,
        desc=f"Searchable transcripts of {len(rows):,} EEVblog videos."))

    print(f"{len(rows):,} pages -> {OUT}")
    print(f"{n_ts:,} with timestamps ({n_ts/max(len(rows),1)*100:.0f}%), "
          f"{total_words:,} words indexed")


if __name__ == "__main__":
    sys.exit(main())
