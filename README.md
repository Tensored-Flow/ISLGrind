# ISLGrind

Adaptive practice for **IMO Shortlist** problems (1990–2024). The board shows four
problems — one per topic (Algebra / Combinatorics / Geometry / Number Theory) — and
calibrates difficulty per topic with an Elo/IRT-style ability estimate, serving each
problem a notch above your current level. Up to 4 local profiles; progress is stored
in your browser (`localStorage`). Live site is the static app in [`app/`](app/).

## Repo layout
- `app/` — the deployable static site (`index.html` + `bank.js` + `vercel.json`). **No build step.**
- `ISL_problems/` — extracted problems: per-year `*.tex`/`*.txt` + `index.json` (the source of truth).
- `IMO_Shortlists/` — the official source PDFs (2006–2024) and the IMO Compendium PDFs (1990–2005).
- `pull_isl.sh` — download official ISL PDFs. `extract_isl.py` — split PDFs → per-problem text.
- `ingest_compendium.py` — compendium (1990–2005) → LaTeX. `assemble_bank.py` — build `app/bank.js`.
- `publish.sh` — commit & push (Vercel auto-redeploys).

## Run locally
Open `app/index.html`, or `cd app && python3 -m http.server`.

## Deploy (Vercel)
vercel.com/new → Import this repo → **set Root Directory to `app`** → Deploy.

## Attribution
Problems are the official IMO Shortlists, from imo-official.org and The IMO Compendium;
all rights to the problems remain with their authors and the IMO. Free, non-commercial tool.
