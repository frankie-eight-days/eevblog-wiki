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

## Next session

1. ~~Fetch and score all caption tracks~~ — **done**, see above.
2. Draft the reply to Dave (scoping questions + paid pilot proposal).
3. Run the 25-video pilot: 10 Fundamentals, 10 teardown/repair, 5 mailbag/BLAB
   — deliberately including the worst case so the quote is honest. Pick the
   worst case from the ledger's `needs-whisper` rows.
4. Fetch the age-gated video with `--cookies-from-browser`.

## Reproducing this

    yt-dlp -a <shard> --skip-download --write-auto-subs --no-write-subs \
      --sub-langs en --sub-format json3 --no-overwrites --ignore-errors \
      --sleep-requests 0.5 -o "captions/%(id)s.%(ext)s"

Sharded 10 ways round-robin across the catalogue. Sustained **~196 videos/min**,
whole channel in **~11 minutes**, with **zero throttling** — no 429s, no bot
checks. Serial with a 1 s sleep managed 4.5/min (7+ hours), so the concurrency
is worth it. `tools/score_captions.py` rebuilds the ledger from what is on disk;
`tools/watch_fetch.sh` is the progress/throttle monitor.
