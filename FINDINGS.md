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

## Next session

1. Fetch all 2,104 caption tracks as json3 (~450 MB, ~1 h, polite rate limits).
2. Score each by punctuation density; write a **ledger**: id, title, date,
   duration, words, words/sentence, verdict good | needs-whisper, provenance.
   That replaces the 40% sample estimate with the real number and the real cost.
3. Draft the reply to Dave (five scoping questions + paid pilot proposal).
4. Run the 25-video pilot: 10 Fundamentals, 10 teardown/repair, 5 mailbag/BLAB
   — deliberately including the worst case so the quote is honest.
