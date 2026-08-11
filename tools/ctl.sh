#!/bin/bash
# eevblog whisper control:  ./ctl.sh status | pause | resume | log [n] | stop | start
B=$HOME/eevblog
PLIST=$HOME/Library/LaunchAgents/com.frank.eevwhisper.plist
case "$1" in
  status)  python3 "$B/status.py" ;;
  pause)   touch "$B/PAUSE"; echo "paused - in-flight videos will finish, then it idles" ;;
  resume)  rm -f "$B/PAUSE"; echo "resumed" ;;
  log)     tail -"${2:-25}" "$B/logs/daemon.log" ;;
  stop)    launchctl unload -w "$PLIST"; echo "stopped (will NOT restart on reboot)" ;;
  start)   launchctl load -w "$PLIST"; echo "started" ;;
  *)       echo "usage: ./ctl.sh status|pause|resume|log [n]|stop|start" ;;
esac
