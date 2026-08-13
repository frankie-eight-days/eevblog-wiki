#!/bin/bash
# Wait for transcription, then run every downstream stage unattended.
#
# Each stage is resumable and idempotent, so a crash anywhere means re-running
# this script rather than unpicking state. Everything logs to logs/pipeline.log
# with a timestamp so the sequence can be reconstructed after the fact.
set -u
cd /Users/frankwalsh/Documents/vibecoding/eevblog_wiki
LOG=logs/pipeline.log
say(){ echo "$(date '+%H:%M:%S') $*" | tee -a "$LOG"; }

say "=== pipeline armed; waiting for transcription ==="

# 1. Wait for the runner to exit. Poll the PROCESS, not the transcript count: the
#    queue legitimately sits still for 45+ minutes inside a bot-check cooldown, and
#    a count-based wait would call that "done".
#
#    Require the process to be absent THREE consecutive times. Restarting the
#    runner to change a setting leaves a few seconds with no process, and a
#    single-poll check that landed in that gap would fire the whole downstream
#    pipeline against a half-finished corpus. Six minutes of absence is far longer
#    than any restart, and costs nothing on a genuine finish.
gone=0
while [ "$gone" -lt 3 ]; do
  if ps aux | grep -q "[a]pi_run.py"; then gone=0; else gone=$((gone+1)); fi
  sleep 120
done
N=$(find whisper_out -name '*.json' | wc -l | tr -d ' ')
say "transcription finished: $N whisper transcripts on disk"

# 2. whisper JSON -> census-ready markdown
say "converting whisper output"
python3 tools/whisper_to_transcript.py >>"$LOG" 2>&1
say "  $(find transcripts_whisper -name '*.md' | wc -l | tr -d ' ') whisper transcripts"

# 3. census over the whisper half (resumes; already-done videos are skipped)
say "census: whisper half"
EEV_TRANSCRIPTS="$PWD/transcripts_whisper" EEV_OUTDIR="$PWD/census/full-v2" \
  python3 tools/census/census_production.py >>logs/census_full_v2.log 2>&1
say "  $(ls census/full-v2/*.json 2>/dev/null | grep -vc _manifest) censused"

# 3b. a chunk-0 parse failure writes a VALID file with zero mentions and the run
#     still reports "no systemic failure", so re-run anything substantial that
#     came back empty. This silently cost 6 videos on each earlier pass.
say "re-running empty-but-substantial censuses"
python3 - <<'PY' >>"$LOG" 2>&1
import json, glob, pathlib, shutil
# Move aside rather than delete. The re-run that is supposed to replace these can
# itself fail -- a dead API key did exactly that -- and delete-then-recreate loses
# the originals when it does. Empty ones are worthless anyway, but the ordering is
# the point: never destroy until the replacement exists.
hold = pathlib.Path('census/_reruns'); hold.mkdir(parents=True, exist_ok=True)
bad = []
for f in glob.glob('census/full-v2/*.json'):
    if '_manifest' in f: continue
    if not json.loads(pathlib.Path(f).read_text()).get('mentions'):
        t = pathlib.Path('transcripts_whisper')/(pathlib.Path(f).stem+'.md')
        if t.exists() and len(t.read_text().split()) > 300:
            bad.append(f)
for f in bad: shutil.move(f, hold / pathlib.Path(f).name)
print(f"held {len(bad)} aside for re-run")
PY
EEV_TRANSCRIPTS="$PWD/transcripts_whisper" EEV_OUTDIR="$PWD/census/full-v2" \
  python3 tools/census/census_production.py >>logs/census_full_v2.log 2>&1

# GATE. Do not build canon on a partial census. The census step can fail whole --
# a missing API key, a billing stop, a network outage -- and every stage after
# this consumes its output without noticing it is short. A canon built on 80% of
# the corpus looks completely normal: right shape, plausible clusters, sensible
# article list, and no indication that 200 videos are missing. Better to stop
# with the transcripts safe and wait for a human.
TR=$(find transcripts_whisper -name '*.md' | wc -l | tr -d ' ')
CE=$(ls census/full-v2/*.json 2>/dev/null | grep -vc _manifest || echo 0)
if [ "$CE" -lt $((TR * 97 / 100)) ]; then
  say "ABORT: census covers $CE of $TR whisper transcripts (<97%)."
  say "       Transcripts are safe on disk. Fix the census, then re-run this script."
  exit 1
fi
say "census gate passed: $CE/$TR whisper transcripts censused"

# 4-6. canon -> graph -> candidates, all pointed at the complete corpus
say "canonicalisation (~90 min)"
python3 tools/canon/build_canon.py --census census/captions-v2 census/full-v2 \
  >>logs/canon_final.log 2>&1
say "  $(tail -1 logs/canon_final.log)"

say "graph"
python3 tools/canon/build_graph.py --census census/captions-v2 census/full-v2 \
  >>"$LOG" 2>&1
say "layout"
python3 tools/canon/layout_graph.py >>"$LOG" 2>&1
say "candidates"
python3 tools/canon/build_candidates.py --census census/captions-v2 census/full-v2 \
  >>logs/candidates_final.log 2>&1
say "  $(grep 'at threshold' logs/candidates_final.log | tail -1)"

# 7. rebuild the public transcript site over the whole corpus
say "transcript site"
python3 tools/build_transcript_site.py >>"$LOG" 2>&1
say "  $(tail -2 "$LOG" | head -1)"

# 8. commit; push separately so a network failure does not lose the commit
say "committing"
git add -A tools canon graph articles transcripts transcripts_whisper whisper_out \
  census/full-v2 site/transcripts/index.html FINDINGS.md >>"$LOG" 2>&1
git commit -q -m "full corpus: transcription complete, census/canon/graph/candidates rebuilt" >>"$LOG" 2>&1
git push -q origin HEAD >>"$LOG" 2>&1 && say "pushed" || say "PUSH FAILED - commit is safe locally"
say "=== pipeline complete ==="
