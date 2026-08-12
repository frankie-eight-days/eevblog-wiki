# EEVblog corpus — feasibility probe

*2026-08-10. Metadata + a 30-video caption sample. No bulk downloading.*

## Corpus size

| | |
|---|---|
| Videos on the main channel | **2,104** |
| Total runtime | **885 hours** |
| Median video | 21.8 min (mean 25.2) |
| Longest | 312 min |

For comparison, The Amp Hour was 719 episodes / ~719 hours. **EEVblog is roughly 1.25× the audio and 2.9× the file count**, and the files are far more variable in length.

Content mix by title keyword (videos can match more than one):

| type | count | share |
|---|---:|---:|
| teardown | 320 | 15.2% |
| mailbag | 181 | 8.6% |
| eevBLAB | 138 | 6.6% |
| fundamentals / tutorial | 131 | 6.2% |
| repair | 114 | 5.4% |
| review | 104 | 4.9% |
| dumpster diving | 74 | 3.5% |
| debunking | 8 | 0.4% |
| unclassified | 1,096 | 52.1% |

Teardown is the single largest identifiable category. That lane is already
validated: the Amp Hour teardown theme produced 46 verified claims from
material the frequency ranking scored at only 11 explanatory mentions.

## Transcripts: no human captions, auto-captions are mixed

There are **no manually-authored caption tracks** — auto-generated only.

Quality is **much better than expected but not uniform**, and the split is
*not* chronological. The 2009 oldest video transcribes cleanly ("This is the
DS1052E, the 50 MHz version… the digital logic analyzer inputs"), while
EEVblog 1652 — recent — comes back as one unbroken run.

Measured on a 30-video sample spread evenly across the catalogue, using
words-per-sentence as the discriminator:

| | | |
|---|---:|---:|
| **Usable as-is** (< 40 words/sentence) | **19** | **63%** |
| **Needs re-transcription** | **11** | **37%** |

Median on the usable ones is **12.2 words per sentence** — normal prose, with
correct jargon ("Rigol DHO 800 series", "zero crossing point", "360°").

The failures are severe rather than marginal: one 5,914-word video is a single
sentence, another 7,475 words has two. **This is the exact failure that made
passages uncitable in the Amp Hour build** — with no sentence boundary there is
no span to slice a verbatim quote from, so the claim has to be dropped.

## Why the 37% fails (diagnosed)

YouTube has **two generations of ASR**. The modern one capitalises and
punctuates; the old one emits a lowercase unbroken stream. Some videos' caption
tracks were regenerated with the new model and some never were.

Ruled out, with evidence:

- **Not scraping/throttling.** `en-orig` is byte-identical to `en` (same word
  count, same missing punctuation), re-fetches return the same bytes, and the
  failures are scattered across catalogue positions 140–2000 while the three
  *oldest* videos come back clean. Throttling would degrade through the session
  and cluster at the end; this does neither.
- **Not upload date.** 2012 is fine, 2016 is broken, 2026 is broken.
- **Not livestreams.** All sampled report `live_status: not_live`.
- **Not a format conversion artifact.** `json3` for a failing video gives 11
  sentence-enders in 9,788 words — identical to the vtt. The punctuation is
  genuinely absent from the stored track, so no format or alternate-track trick
  recovers it.

## Cost of fixing it

| | |
|---|---|
| Audio needing re-transcription (37%) | ~326 h / 19,559 min |
| OpenAI Whisper API for just that | **$117** |
| OpenAI Whisper API for the *whole* corpus | **$319** |
| whisper.cpp large-v3 on Apple Silicon (~5× realtime) | 65 h wall clock, free |
| faster-whisper / whisperx batched (~15×) | 22 h wall clock, free |

**Recommendation: Whisper the entire corpus, not just the broken third.** The
delta is ~$200 on a paid engagement, and it buys uniform transcript quality,
one code path instead of a detect-and-branch pipeline, and no seam where two
different transcription styles meet in the same wiki.

**Do NOT use punctuation restoration** on the lowercase third. Every claim in
the finished wiki is pinned to a byte-exact quote, so a restored transcript
would make a model's inserted text the citable source of truth. Whisper
produces a genuine primary transcription of the actual audio instead; that
distinction is the whole basis of the project's credibility.

## What this means for the build

1. **Don't real-time transcribe the whole corpus.** 885 hours through a
   dictation tool is ~37 days of wall clock. Unnecessary: 63% is already free
   and good.
2. **Hybrid ingest.** Take YouTube captions, score each by words-per-sentence,
   and re-transcribe only the failures with Whisper. That is ~327 hours ≈
   **$120 via API**, or free locally with whisper.cpp at the cost of time.
3. **Detection is trivial and cheap** — the words-per-sentence heuristic above
   ran over the sample instantly and can score all 2,104 in one pass.
4. **Single presenter.** Dave is usually talking alone, which removes the
   hardest data-quality problem of the Amp Hour build: speaker attribution
   repair, whose `attribution_reliable` flag still under-reports.
5. **The canon layer transfers.** The 90,150-entry alias table and vocabulary
   are electronics-domain, not Amp Hour-specific. Same field, same jargon.

## Known caption defects to handle

- Brand mangling: "EEVblog" transcribes as "EV Log". The alias table already
  handles exactly this class of problem.
- Stutter duplication is preserved verbatim ("It's It's", "This is the This is
  the"). Authentic, and harmless — but quotes must not be "cleaned up", since
  verification is byte-exact.

## Open questions for Dave

1. Deliverable: wiki, search over videos, or both?
2. Scope: videos only? blog (141 pages)? forum is explicitly out for v1.
3. Written permission to download and transcribe from the public channel —
   this replaces any need for a mirror. Audio-only is ~40–80 GB; video is 1–3 TB.
4. Metadata export (titles, descriptions, dates, numbers) for citations.
5. Anything not public: unlisted, members-only, pre-YouTube.
6. One-off build or ongoing ingest as he publishes weekly?
7. Hosting/ownership: his domain, his repo. Who owns the pipeline?


## Corrections and confirmations (research pass, 2026-08-10)

**Recovery branch is fully closed.** All seven caption formats (vtt, srt, srv1,
srv2, srv3, ttml, json3) carry the same ~3 punctuation marks on a broken video.
Pushing the track through YouTube's translation layer with `&tlang=en` is a
no-op for English→English. There is **no documented trigger** for YouTube
regenerating a track with the newer model — a genuine negative result, not a
gap in searching. Likely cause (unconfirmed): YouTube ASR barely punctuated
before ~April 2025 and the backfill is incomplete.

**Use `json3`, not `vtt`.** VTT carries ~3x word inflation from rolling-caption
duplication (yt-dlp issue 1734). Consecutive-line dedup mostly handles it, but
json3 avoids the problem.

**whisper.cpp, not faster-whisper, on Apple Silicon.** faster-whisper has no
Metal support and runs CPU-only; whisper.cpp uses Metal and can put the encoder
on the Neural Engine. Use large-v3 (not a smaller model) — dense electronics
jargon is exactly where model size pays. Checkpoint per video and make the
runner resumable.

**Tag transcript provenance per video** (`youtube-asr` vs `whisper-large-v3`)
in the packets, so spot-checks can be aimed at the re-transcribed set.

**Why restoration is disqualified, sharpened:** the old ASR is not merely
unpunctuated, it is the *weaker model* — the one mangling technical jargon.
Restoration would fix punctuation while preserving every word error underneath,
producing quotes that read fluently and are wrong, and the verifier would pass
them because the bytes match the file. Byte-exact matching against a corrupted
source guarantees internal consistency, not fidelity to what was said.

### Corrected sizing (a research estimate of 120 h was wrong)

Broken videos are **not** shorter — mean 24 min vs 20 min for good ones — so
the affected share is **40% by audio hours**, not by video count:

| | |
|---|---|
| Needs re-transcription | ~354 h |
| Whisper API for that | **$127** |
| Whisper API, whole corpus | $319 |

### Local (Mac Mini M4, 16 GB) vs cloud

| approach | cost | wall clock |
|---|---|---|
| local, turbo, broken 40% | free | 1.2–1.8 days |
| local, large-v3, broken 40% | free | 3.7–5.9 days |
| local, large-v3, whole corpus | free | 9–15 days (reject) |
| cloud, broken 40% | $127 | 2–4 h (upload-bound) |
| cloud, whole corpus | $319 | 4–8 h |

16 GB is fine for large-v3 (~3.1 GB model); the constraint is machine
availability, not RAM. **Plan: run the pilot locally for free; pay the $127 for
the full build and bill it to Dave as a pass-through.**

Storage is a non-issue: all 2,104 caption tracks ≈ **450 MB**, extracted text
≈ 50 MB. Never store audio — download, transcribe, write transcript, delete;
peak stays ~50 MB.

---

# FULL CENSUS — all 2,104 videos scored (2026-08-11)

**The sample estimates above are superseded by this section.** Every caption
track on the channel has been fetched and scored; `meta/ledger.tsv` is the
per-video record (pos, id, title, duration_s, words, sentences, wps, verdict,
provenance). Numbers below are measured, not extrapolated.

| verdict | videos | audio hours | share of audio |
|---|---:|---:|---:|
| **good** (punctuated, usable as-is) | 1,336 | 595.2 h | **67.3%** |
| **needs-whisper** (unpunctuated ASR) | 737 | 273.7 h | **30.9%** |
| **no captions at all** | 31 | 15.8 h | 1.8% |
| **total needing transcription** | **768** | **289.5 h** | **32.7%** |

The 31 with no track were verified individually with `--list-subs` — YouTube has
neither auto nor manual captions for them. They are Whisper work, not a fetch
failure to retry. One further video (`AuFSMpFzAnw`, eevBLAB 117) is age-gated
and needs `--cookies-from-browser` to fetch; it is counted in the 31.

## The threshold is empirically real, not a judgment call

Words-per-sentence across the corpus is **sharply bimodal with an empty gap**
exactly where the cut sits, so the good/broken split is not sensitive to where
the line is drawn:

| wps | videos | |
|---|---:|---|
| 0–10 | 305 | normal prose |
| 10–15 | 843 | normal prose |
| 15–20 | 187 | |
| 20–30 | 5 | |
| **30–40** | **0** | **← the cut sits in an empty gap** |
| 40–60 | 1 | |
| 60–200 | 30 | |
| 200+ | 702 | unpunctuated runs |

Median on the good tracks is **11.9 wps** — unchanged from the 30-video sample
(12.2), which also confirms that fetching at high concurrency did not cause
YouTube to serve degraded tracks.

## Corrected cost (this replaces the $127 figure above)

| | |
|---|---|
| Audio needing Whisper | **289.5 h** |
| OpenAI Whisper API @ $0.006/min | **$104** |
| Whole corpus for comparison | $319 |
| Local whisper.cpp large-v3, broken third only (~5× realtime) | ~2.4 days, free |

An earlier correction claimed broken videos run *longer* (24 vs 20 min) and put
the affected share at 40% by audio hours. On the full census the opposite is
true — **broken mean 22.3 min, good mean 26.7 min** — so the share by audio
hours (30.9%) is *lower* than the share by video count (35.6%). The 30-video
sample was too small to resolve this.

## The failure is era-correlated but not era-bounded

Broken share by catalogue position (0 = newest):

| position | broken |
|---|---:|
| 0–209 (newest) | 12% |
| 210–419 | 24% |
| 420–839 | 36% |
| 840–1259 | **~52%** |
| 1260–1889 | ~32% |
| 1890–2104 (oldest) | 43% |

The middle of the catalogue is worst, and even the newest 10% is 12% broken.
**No date cutoff cleanly separates the two populations**, which is why ingest
must score every video individually rather than branch on upload year.

## EEVblog2 — the second channel (Dave asked for it too)

Censused the same way. **It is materially worse than the main channel** and the
difference matters for the quote:

| | videos | hours | good h | needs Whisper | % broken by audio |
|---|---:|---:|---:|---:|---:|
| EEVblog | 2,104 | 885 | 595 | 290 h | 33% |
| EEVblog2 | 1,290 | 268 | 88 | 180 h | **67%** |
| **combined** | **3,394** | **1,153** | **683** | **470 h** | **41%** |

EEVblog2 adds 61% more files but only 30% more audio — median video is 7.1 min
vs 21.8 on the main channel. But two-thirds of its audio has unpunctuated
captions, so it carries a disproportionate share of the transcription work:
38% of the Whisper hours from 23% of the audio.

**Whisper for the whole job: $169** (470 h), or ~3.9 days unattended on the M4.

Short videos also mean fewer claims per file, so EEVblog2's contribution to
article count will be lower per video than the main channel. Do not price it
per-video at the same rate.

## Storage

All 2,073 tracks as json3: **791 MB** on disk (higher than the 450 MB estimate).
Extracted text will be far smaller. Still trivial; audio is never stored.

## Local transcription: measured, not projected (2026-08-11)

Running on the M4 Mini (16 GB, 10 cores) via a launchd daemon. **Sustained
throughput is 3.99x realtime**, which is the number to plan with. Everything
that got us there, including two of my own bad estimates:

| configuration | throughput | note |
|---|---|---|
| single file, idle machine, pre-made WAV | 5.3-5.4x | benchmark conditions, not reachable in production |
| 2 workers + 2 downloaders, launchd default QoS | 2.32x | |
| 2 workers, downloaders niced, Interactive QoS | 3.33x | |
| **1 worker, downloader niced, Interactive QoS** | **3.99x** | **shipping config** |

Three real causes of the gap between benchmark and production:

1. **launchd confines LaunchAgents to efficiency cores** under default
   background QoS. The benchmark ran in an interactive SSH shell with P-core
   access. Fixed with `ProcessType=Interactive`.
2. **Downloaders steal cores.** ffmpeg decoding to WAV is CPU-hungry enough to
   slow whisper measurably. Fixed with `nice -n 15` and `-threads 2`.
3. **A second transcriber makes it slower, not faster.** The work is GPU-bound;
   whisper's idle CPU during decode is not spare capacity. My original 8.5x
   concurrency figure was an artifact of benchmarking two files of unequal
   length -- the short one finished early and the long one ran alone for the
   rest, so the number described a brief overlap rather than sustained rate.

Flash attention (`-fa on`) made no difference (301.5s vs 301.8s). Core ML/ANE
remains untried; docs claim >3x on the encoder but it needs a source rebuild.

### What that costs in time

| scope | audio | local @ 3.99x | API @ $0.36/h |
|---|---:|---:|---:|
| main channel | 289.6 h | **3.0 days** | $104, ~2 h |
| both channels | 449 h | **4.7 days** | $169, ~2.5 h |

**Recommended hybrid:** buy the main channel via API so article work can start
immediately, and let the Mini grind through EEVblog2 for free in the background
(~1.9 days). That is $104 to take transcription off the critical path entirely
while still paying nothing for the half of the corpus nobody is waiting on.

## Article structure: brand pages beat model pages (2026-08-11)

Measured from titles alone, before transcripts add in-passing mentions:

| unit | evidence available |
|---|---|
| **Brand** (Fluke, Rigol, Tektronix) | Rigol 50 videos, Fluke 45, Keysight 42, Agilent 36, Siglent 28, Tektronix 28, R&S 20, Brymen 18. **22 brands appear in 5+ titles**; 481 titles name a tracked brand. |
| **Model** (Fluke 91, Rigol DS1054Z) | 223 candidates, but only **30 appear in 2+ videos**. |

So the instrument layer is really two different articles:

1. **Brand pages** — genuine cross-video synthesis, and the natural home for
   Dave's accumulated judgment ("Rigol's firmware", "Fluke build quality",
   "why Keysight costs what it does"). This is the lane no other site has,
   because nobody else has 16 years of one expert opening the same brands.
2. **Teardown pages** — mostly single-video, so these are video-anchored
   articles: specs plus what Dave noticed. Cross-video synthesis is available
   for only ~30 models, so do not build the pipeline assuming otherwise.

The census `type` vocabulary already separates these: `company-product` for the
brand axis, `tool-equipment` for instrument classes (oscilloscope, multimeter).
Neither is currently used to select or shape anything -- `type` is written into
packet metadata at build_bundles.py:356 and never read again.

# PIPELINE BUILT AND RUN (2026-08-12, overnight)

Every stage now exists and has been run end to end on 2,064 videos. The wiki
tooling from the Amp Hour was NOT in that repo — only its outputs were committed —
so canon, graph and candidate selection were all rebuilt from
`canon/_canon_report.md`, with stage numbering kept aligned so the two read side
by side.

## Numbers as of 03:50

| stage | result |
|---|---|
| transcripts | 1,763 caption + ~470 whisper (of an eventual ~2,900) |
| census | 194,417 caption + 31,024 whisper mentions |
| canon | 65,311 raw → 61,280 canonical (6.2% compression, $0.88) |
| graph | 3,961 nodes, 13,883 edges, 49 communities |
| candidates | **747 articles** at explains≥15 (Amp Hour: 412 from 717 episodes) |

## The caption census was silently discarding 22% of its evidence

Rejection was 21.6% against 7.8% on the whisper half. Measured across 8,413
rejects: **48% were snippets spanning a paragraph boundary**. The census locates a
mention by finding its `context_snippet` inside the paragraph it names, so a
snippet crossing a break can never be found and the mention is dropped.

The cause was not the word cap. `json3_to_transcript` tested for a sentence end
only at CAPTION EVENT boundaries — an event is an arbitrary display line and
sentences end mid-event constantly, so the test almost always said no and
paragraphs ran to the cap, breaking wherever they landed. The whisper converter
split into sentences first, which is exactly why it never had the problem.

What made it findable: a first fix requiring a sentence end at the event level
pushed paragraphs to 71 words, past the 45 the census needs, and a parameter
sweep showed **no setting could give both**. That impossibility pointed at the
real bug.

    kept 151,849 → 194,417     rejected 21.6% → 7.8%     articles 588 → 747

**This bug was invisible in every health metric.** Depth mix, mentions/1000 words
and type mix all looked fine on the broken census because the losses were spread
evenly. Only the whisper-vs-caption comparison exposed it — an argument for
keeping both transcription paths rather than standardising early.

## Two canon bugs caught before they corrupted the vocabulary

- Stage 3 used the aggressive stemmer, which folds `-ing`/`-er`, so `3d-printer`
  and `3d-printing` were merged **by rule**. Stage 3 now uses a plural-only
  stemmer; the aggressive stem stays in stage 5 where a type-compatibility check
  backs it up.
- Acronym pairs were auto-merged rather than adjudicated, collapsing `hp` into
  `hackaday-prize`. Initials matching is good recall and bad evidence, so stage 7
  now feeds stage 8.

`louvain()` also needed its aggregation phase — local moving alone gave 312
communities against the Amp Hour's 26. Aggregating each community to a super-node
and re-running gives 49.

## YouTube throttling: it is a volume quota, not a rate limit

**This corrects an earlier conclusion in this file.** I first read the blocks as
rate-triggered and slowed the downloader from a 15s gap to 75s. It ran clean for
two and a half hours and then blocked anyway. Measuring every window in the log:

| videos before block | rate during window |
|---|---|
| 99 | 63/h |
| 79 | 89/h |
| 87 | 37/h |

The block lands at **~85 videos whatever the pace**. 37/h and 89/h hit the same
wall. Slowing down buys nothing — it stretches one quota over three times the
wall-clock:

    15s gap: ~85 videos in ~50 min + 30 min cooldown  -> ~64/h
    75s gap: ~87 videos in 141 min + 30 min cooldown  -> ~30/h

So spend the quota fast and wait out the cooldown. What misled me the first time
was cooldown ESCALATION: resuming while the quota was still exhausted re-blocked
instantly and doubled the wait (30 -> 60 -> 120), which looked like the fast
setting being punished. It was the resume timing, not the gap.

Blocks are not permanent bans — every one has cleared on its own.

**The block is IP-scoped, not account-scoped.** Probed the same video with and
without `--cookies` while blocked: identical "Sign in to confirm you're not a bot"
both times. So cookies neither cause nor cure it, and there is no account-level
lever — only waiting, or a different network.

**30 minutes is not long enough to clear it.** Three cycles out of four re-blocked
on the first retry and then doubled to 60 anyway, costing 90 minutes where one
clean wait would do. Base cooldown is now 45 minutes; a 40-minute gap succeeded
when it was tried. Roughly 85 videos per window, then the wait.

Cumulative volume matters too: after ~685 downloads in a day the windows get
shorter and the blocks longer, which looks like a daily budget on top of the
per-window one.

Two `api_run.py` bugs found the hard way:
- `urlopen(timeout=1800)` — a hung socket parked each of 6 workers for 30 minutes,
  the ready queue filled, the downloader blocked in `put()`, total deadlock.
- `RuntimeError(stderr[-200:])` truncated away the bot-check marker, which
  yt-dlp puts at the START of a long error. `BOT_BLOCK` never matched, so instead
  of pausing the run would have marked all 748 videos failed.

## Article lanes (agreed with Frank)

concept · brand/product · teardown · debunked · safety/standards · series index ·
people. Four port from the Amp Hour; teardown and brand need new gatherers and a
second template. Debunked needs no census change — it reuses the concept template
but promotes `opinion` evidence instead of discarding it.

Census prompt was retuned for EEVblog: demonstrative resolution against the video
title (Dave is holding the thing and never names it), and device-under-test
promoted to `main_topics[0]`. Measured: 93% of teardowns name a specific device,
including ones the title does not ("Sony Mystery Teardown" → `sony-pc216ax`).

## Next session

1. Finish transcription (~667 remaining, ~16h at the sustainable rate).
2. Re-run census → canon → graph → candidates on the complete corpus. All cheap.
3. Set the explains threshold from the full sweep rather than inheriting 15.
4. Review the 13 sibling-split pairs (`3d-printer`/`3d-printing`) — a judgment
   call each; ADC/DAC is in that list and must stay split.
5. Build the teardown and brand gatherers, then the first articles.

## Reproducing this

    yt-dlp -a <shard> --skip-download --write-auto-subs --no-write-subs \
      --sub-langs en --sub-format json3 --no-overwrites --ignore-errors \
      --sleep-requests 0.5 -o "captions/%(id)s.%(ext)s"

Sharded 10 ways round-robin across the catalogue. Sustained **~196 videos/min**,
whole channel in **~11 minutes**, with **zero throttling** — no 429s, no bot
checks. Serial with a 1 s sleep managed 4.5/min (7+ hours), so the concurrency
is worth it. `tools/score_captions.py` rebuilds the ledger from what is on disk;
`tools/watch_fetch.sh` is the progress/throttle monitor.
