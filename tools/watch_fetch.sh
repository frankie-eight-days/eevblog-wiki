#!/bin/bash
# Observability for the sharded caption fetch. One line per event:
#   heartbeat every 2 min (count, rate, ETA, live workers)
#   THROTTLE/ERROR the moment a new one appears in any shard log
#   a final summary when the last worker exits
cd "$(dirname "$0")/.." || exit 1

TOTAL=2104
prev_n=$(ls captions/*.json3 2>/dev/null | wc -l | tr -d ' ')
prev_t=$(date +%s)
prev_err=0
start_n=$prev_n
start_t=$prev_t
tick=0

# signatures that mean YouTube is pushing back, as opposed to one bad video
THROTTLE='429|Too Many Requests|Sign in to confirm|not a bot|temporarily blocked|HTTP Error 40[0-9]|Video unavailable|Private video|unable to download|giving up'

while true; do
  live=$(pgrep -f 'yt-dlp -a scratch/shards' | wc -l | tr -d ' ')

  # new pushback since last check -> emit immediately, with an example
  err=$(grep -Ehc "$THROTTLE" logs/shard*.log 2>/dev/null | paste -sd+ - | bc 2>/dev/null)
  err=${err:-0}
  if [ "$err" -gt "$prev_err" ]; then
    echo "THROTTLE/ERROR: $((err - prev_err)) new (total $err) | $(grep -Ehm1 "$THROTTLE" logs/shard*.log 2>/dev/null | tail -1 | cut -c1-140)"
    prev_err=$err
  fi

  tick=$((tick + 1))
  if [ $((tick % 8)) -eq 0 ] || [ "$live" -eq 0 ]; then
    n=$(ls captions/*.json3 2>/dev/null | wc -l | tr -d ' ')
    now=$(date +%s)
    rate=$(echo "scale=1; ($n - $prev_n) * 60 / ($now - $prev_t + 1)" | bc)
    avg=$(echo "scale=1; ($n - $start_n) * 60 / ($now - $start_t + 1)" | bc)
    eta=$(echo "scale=1; ($TOTAL - $n) / ($avg + 0.01) / 60" | bc)
    pct=$(echo "scale=1; $n * 100 / $TOTAL" | bc)
    echo "fetch $n/$TOTAL (${pct}%) | now ${rate}/min avg ${avg}/min | ETA ${eta} h | workers $live | errs $err"
    prev_n=$n; prev_t=$now
  fi

  if [ "$live" -eq 0 ]; then
    echo "ALL WORKERS EXITED - $(ls captions/*.json3 2>/dev/null | wc -l | tr -d ' ')/$TOTAL tracks on disk"
    exit 0
  fi
  sleep 15
done
