#!/usr/bin/env bash
# Pull IMO Shortlists reliably.
#
#   * 2006 -> latest : official PDFs from imo-official.org (authoritative,
#                      problems + official solutions, one file per year)
#   * 1959 -> 2009   : The IMO Compendium (single PDF; use it for 1990-2005,
#                      the years the official site does not host)
#
# Shortlists are confidential for ~1 year, so the newest available year is
# normally (current year - 1).
set -euo pipefail

OUT="${1:-./IMO_Shortlists}"
UA="Mozilla/5.0 (compatible; isl-fetch/1.0)"
END_YEAR="$(date +%Y)"          # try up to this year; missing ones just 404
START_OFFICIAL=2006

mkdir -p "$OUT"

echo ">> Official shortlists ($START_OFFICIAL-$END_YEAR) from imo-official.org"
for y in $(seq "$END_YEAR" -1 "$START_OFFICIAL"); do
  url="https://www.imo-official.org/problems/IMO${y}SL.pdf"
  fallback="https://www.imo-official.org/assets/documents/problems/${y}/IMO${y}SL.pdf"
  dest="$OUT/ISL-${y}.pdf"
  code=$(curl -sSL -A "$UA" -o "$dest" -w "%{http_code}" "$url")
  if [ "$code" != "200" ] || [ ! -s "$dest" ]; then
    code=$(curl -sSL -A "$UA" -o "$dest" -w "%{http_code}" "$fallback")
  fi
  if [ "$code" = "200" ] && [ -s "$dest" ]; then
    echo "   ISL-${y}.pdf  ✓"
  else
    rm -f "$dest"
    echo "   ${y}: not available (HTTP $code) — skipped"
  fi
done

echo ">> IMO Compendium (covers 1959-2009; use for 1990-2005)"
curl -sSL -A "$UA" -o "$OUT/IMO-Compendium-1959-2009.pdf" \
  "https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/imo-compendium.pdf" \
  && echo "   IMO-Compendium-1959-2009.pdf  ✓"

echo ">> Done. Files in: $OUT"
ls -lh "$OUT"
