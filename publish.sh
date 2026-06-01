#!/usr/bin/env bash
# Commit & push the whole project. Vercel deploys the site from app/ and auto-redeploys.
set -euo pipefail
cd "$(dirname "$0")"
git add -A
if git diff --cached --quiet; then echo "Nothing to commit."; exit 0; fi
git -c user.name="Leonardo Wang" -c user.email="leonardowang050428@outlook.com" commit -q -m "${1:-update}"
git push -q origin main
echo "Pushed. Vercel redeploys from app/ in ~30s."
