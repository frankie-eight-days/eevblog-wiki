#!/usr/bin/env python3
"""Progress report for the whisper daemon.

Counts transcripts on disk rather than trusting the daemon's own tally, so the
number stays true across restarts, crashes and manual intervention.
"""
import json, pathlib, csv, time

B = pathlib.Path.home() / "eevblog"
rows = list(csv.DictReader(open(B / "queue.tsv"), delimiter="\t"))
have = {p.stem for p in (B / "out").glob("*.json")}

ch = {}
for r in rows:
    d = ch.setdefault(r["channel"], {"n": 0, "done": 0, "h": 0.0, "dh": 0.0})
    d["n"] += 1
    d["h"] += int(r["duration_s"]) / 3600
    if r["id"] in have:
        d["done"] += 1
        d["dh"] += int(r["duration_s"]) / 3600

done, total = len(have), len(rows)
print(f"transcripts on disk: {done}/{total}  ({done/total*100:.1f}%)")
for k, d in ch.items():
    print(f"  {k:<9} {d['done']:5d}/{d['n']:<5} videos   "
          f"{d['dh']:6.1f}/{d['h']:.1f} h audio")

try:
    s = json.loads((B / "status.json").read_text())
except Exception:
    print("\n(no status.json yet)")
    raise SystemExit(0)

age = time.time() - (B / "status.json").stat().st_mtime
print(f"\nrate {s['realtime_factor']}x realtime | elapsed {s['elapsed_hours']}h "
      f"| ETA {s.get('eta_hours','?')}h | failed {s['failed']}"
      f"{' | PAUSED' if s['paused'] else ''}")
# a stale heartbeat is the signal that something is wrong -- launchd should have
# restarted it within ~30s, so anything over a few minutes wants a look
print(f"heartbeat {age:.0f}s old" + ("   <-- STALE, check ./ctl.sh log" if age > 300 else ""))
for v in s.get("in_flight", {}).values():
    print(f"  now: {v}")
