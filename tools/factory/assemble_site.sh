#!/bin/bash
# Assemble the single EEVblog site (wiki + transcripts + graph) and deploy it.
#
# Builds into a staging directory OUTSIDE ~/Documents on purpose. That folder is
# iCloud-synced, and iCloud restores files deleted from it -- a `rm -rf` of the
# transcript output came back minutes later with its original mtimes, and its
# conflict copies ("VIDEOID 3.html") are where the duplicate pages came from in
# the first place. Anything generated is therefore assembled fresh in /tmp, and
# only files tracked in git are treated as real.
set -e
ROOT="/Users/frankwalsh/Documents/vibecoding/eevblog_wiki"
STAGE="/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding-amp-hour-wiki/2f6e7b82-f9a2-4e98-aa31-4d30e2a5da6c/scratchpad/eev_site"
cd "$ROOT"

echo "== sync articles -> quartz content"
python3 tools/factory/sync_wiki.py

echo "== quartz build"
(cd wiki && npx quartz build >/dev/null 2>&1)

echo "== assemble staging dir"
rm -rf "$STAGE"; mkdir -p "$STAGE"
cp -R wiki/public/. "$STAGE"/

# transcripts, taken from GIT rather than the working tree so iCloud's
# conflict copies can never reach the deploy
mkdir -p "$STAGE/transcripts/t"
git archive HEAD site/transcripts | tar -x -C "$STAGE/.tmp_ts" --strip-components=2 2>/dev/null || {
  mkdir -p "$STAGE/.tmp_ts"
  git archive HEAD site/transcripts | (mkdir -p "$STAGE/.tmp_ts" && tar -x -C "$STAGE/.tmp_ts")
}
if [ -d "$STAGE/.tmp_ts/site/transcripts" ]; then
  cp -R "$STAGE/.tmp_ts/site/transcripts/." "$STAGE/transcripts/"
fi
rm -rf "$STAGE/.tmp_ts"

# graph explorer
[ -f site/explore.html ] && cp site/explore.html "$STAGE/explore.html"

cat > "$STAGE/vercel.json" <<'JSON'
{ "cleanUrls": true, "trailingSlash": false }
JSON

TS=$(find "$STAGE/transcripts/t" -name '*.html' 2>/dev/null | wc -l | tr -d ' ')
DUP=$(find "$STAGE/transcripts/t" -name '* [0-9].html' 2>/dev/null | wc -l | tr -d ' ')
WIKI=$(find "$STAGE" -maxdepth 1 -name '*.html' | wc -l | tr -d ' ')
echo "   wiki pages: $WIKI   transcript pages: $TS   duplicates: $DUP"
if [ "$DUP" != "0" ]; then echo "   ABORT: duplicates reached the staging dir"; exit 1; fi

echo "== deploy"
cd "$STAGE"
if [ ! -d .vercel ]; then
  npx vercel link --yes --project eevblog-wiki --scope frankie-eight-days-projects
fi
npx vercel deploy --prod --yes --archive=tgz 2>&1 | grep -iE "^▲|Aliased|Error" || true
