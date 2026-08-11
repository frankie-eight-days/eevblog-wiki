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
