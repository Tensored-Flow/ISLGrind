<h1 align="center">ISLGrind</h1>
<p align="center"><b>An adaptive trainer for the hardest pre-olympiad math problems on Earth.</b><br>
Practice 1,944 olympiad problems — the <a href="https://www.imo-official.org/">IMO Shortlist</a> plus IMO 2026, every senior Balkan MO, USAMO, USEMO, USA TST/TSTST, EGMO, APMO, and RMM — and the difficulty adapts to you, topic by topic.</p>

<p align="center">🔗 <b>Live:</b> <a href="https://isl-grind.vercel.app">isl-grind.vercel.app</a></p>

---

## What it is

The **IMO Shortlist** is the pool of ~30 problems each year from which the International Mathematical Olympiad exam is chosen — the gold standard of hard, beautiful math. ISLGrind turns 36 years of them into a personal coach:

- 🎯 **Adaptive, per-topic difficulty.** Algebra, Combinatorics, Geometry, and Number Theory each get their own ability estimate. Like a good tutor, ISLGrind serves you problems a notch *above* your level — and updates by how *surprising* each result is (nailing a hard one moves you up a lot; missing an easy one moves you down a lot; an on-level result barely moves you).
- 🃏 **Four at a time, one per topic.** Work whichever appeals; mark it solved or not and only that card is replaced — so you're always being stretched across all four areas.
- 🏆 **Filter by competition.** Grind a single source — IMO, Balkan MO, USAMO, USEMO, EGMO, APMO, RMM, USA TST/TSTST, or the full IMO Shortlist — or mix them all.
- 👤 **Up to 4 profiles**, each with completely separate progress.
- 📚 **1,944 problems** across 10 competitions, every one rendered as clean math (not blurry PDF scans).
- 💾 **No login, no tracking.** Your progress lives in your own browser — turn on **☁ Sync** to carry it to your other devices with a sync code.

Each new card is drawn from your unsolved problems within your topic and source filters. One in four comes from the problems you marked ✗ Couldn't or skipped, at any level; one in four comes from every unsolved problem, at any level, so easier ones keep turning up however high you climb; the rest come from the adaptive target difficulty, every problem there with an equal chance (if that level is exhausted, the nearest available level is used). With nothing saved for review in a topic, its review share uses the adaptive draw. Solving a problem takes it off the review list.

## Use it yourself

**Easiest — just open the live site:** **[isl-grind.vercel.app](https://isl-grind.vercel.app)** (works on desktop and mobile; nothing to install).

**Or run it on your own computer:**
1. Click the green **`Code`** button at the top of this repo → **Download ZIP** (or `git clone https://github.com/Tensored-Flow/ISLGrind.git`).
2. Unzip it and double-click **`index.html`** — it opens in your browser and you're training.
   - *(Optional, for a cleaner setup: open a terminal in the unzipped folder and run `python3 -m http.server`, then visit the link it prints.)*
   - *Tip: to keep progress when moving between computers, turn on **☁ Sync across devices**, or use **⬇ Backup** to save a file and **⬆ Restore** it elsewhere.*

Your progress saves automatically in that browser. Pick a profile and go — solve two notches above your level, and watch each topic's bar climb.

**Sync across devices.** Click **☁ Sync across devices** (sidebar, under Data) → **Create a sync code**. On your phone or another computer, open the site, click the same button and enter the code: you get the same profiles, the same four problems, solved list, notes and gyms. Every change is sent a moment later; other devices pick it up when you open the site or switch back to it (and every 30 s while it's open). If two devices change the same profile before they can sync — say one was offline — the later change wins; different profiles combine. **Stop syncing** works like deregistering a Kindle: the device goes back to a fresh start and your progress stays saved under the code, ready to come back whenever you enter it again. Anyone with the code can see and change your progress, so keep it to yourself.

**Keep a save file (Chrome / Edge).** Click **⬇ Backup** once and create (or choose) `islgrind-progress.json` in your Downloads folder. From then on every solve, skip, note and setting is written to that file automatically. On each later visit, one click on **⬇ Backup** loads it back — or pick *"Allow on every visit"* in Chrome's prompt and it loads by itself. Other browsers download a copy instead.

**Light or dark.** The ☀ / ☾ button next to the logo switches themes; until you choose, ISLGrind follows your system setting.

## How it was built

The official shortlists live in PDFs whose math doesn't copy out cleanly. ISLGrind was assembled by **rendering every problem page to an image and using a vision model to transcribe the math into LaTeX**, then verifying each one — so all 1,035 shortlist problems render crisply via [KaTeX](https://katex.org/). The adaptive engine is a lightweight **Elo / item-response model** with per-topic ability and confidence that grows as you practice. It's a single static page with no accounts; the optional sync keeps each sync code's progress in one [Supabase](https://supabase.com/) table, reached only through three database functions (`supabase/sync.sql`), and stores only a hash of the code.

**Setting up sync on a new Supabase project:** paste [`supabase/sync.sql`](supabase/sync.sql) into the dashboard's SQL Editor and run it (safe to re-run), then set `SUPA_URL` and `SUPA_KEY` in `index.html` to the project's URL and public anon key.

## Attribution

- **IMO Shortlist** (1,035 problems, 1990–2025) — the official shortlists, from [imo-official.org](https://www.imo-official.org/) and [The IMO Compendium](https://www.imomath.com/).
- **IMO 2026** (6 problems) — the public contest paper from [imo-official.org](https://www.imo-official.org/problems/2026/). The 2026 shortlist remains confidential until after IMO 2027.
- **Balkan MO** (172 problems, every senior paper from 1984–2026) — historical statements from the [John Scholes archive](https://webee.technion.ac.il/people/aditya/www.kalva.demon.co.uk/balkan.html), the [Balkan MO Compendium](https://www.toomates.net/biblioteca/CompendiumBalkanMO.pdf), the open [AI-MO olympiads corpus](https://huggingface.co/datasets/AI-MO/olympiads/tree/main/Balkan_MO), and the [official 2026 host](https://hms.gr/43bmo2026/problems.html).
- **USEMO** (42 problems, every paper from 2019–2025) — transcribed to LaTeX from the official papers on the [USEMO page](https://web.evanchen.cc/usemo.html).
- **USAMO** (156, 2000–2025) and **EGMO 2012–2022** — from the [AoPS Wiki](https://artofproblemsolving.com/wiki/), each problem linking back to its page.
- **USA TSTST** (114, 2011–2024) and **USA TST** (79, 2012–2025) — from [Evan Chen's exam archive](https://web.evanchen.cc/problems.html).
- **EGMO 2023–2025** — from the official [egmo.org](https://www.egmo.org/) papers (EGMO is now complete, 84 problems 2012–2025).
- **RMM** (66, 2012–2025, a few editions unavailable) — from the official [Romanian Master of Mathematics](https://rmms.lbi.ro/) papers.
- **APMO** (190 problems, every paper from 1989–2026) — from the [official APMO archive](https://www.apmo-official.org/problems), labeled by year and official problem number (P1–P5), with links to the official papers. The 124 existing [MathNet](https://huggingface.co/datasets/ShadenA/MathNet) transcriptions (MIT, CC-BY-4.0) are matched to those papers, with statement corrections and embedded answers removed; their internal IDs remain stable so saved progress, notes, and gyms still work.

All problems from PDF sources were transcribed to LaTeX and render via KaTeX; competition topics (Algebra/Combinatorics/Geometry/Number Theory) are editorially classified. Every competition is year- and problem-number-labeled. All rights to the problems remain with their authors and the respective competitions. ISLGrind is a free, non-commercial study tool.

## Updating the APMO bank

Run `python import_apmo.py --refresh` to fetch the official archive and its problem PDFs, check them against the reviewed hashes in `apmo_problems.json`, and regenerate `bank_apmo.js`. Downloads stay in the ignored `.cache/apmo/` directory. The app loads the generated bank locally, including when opened offline; it does not fetch PDFs during practice.

New or changed official papers stop the refresh before it replaces the bank. Transcribe/review their five statements in `apmo_problems.json` and update the paper's SHA-256 hash, then rerun. This review keeps PDF extraction errors out of mathematical formulas. `python import_apmo.py` rebuilds from the reviewed transcriptions without network access. Existing difficulty levels are retained; the 66 added problems use provisional levels 3–7 by paper position.

Check the import and application integration with `python -m unittest discover -s tests -p "test_*.py"` and `node --test tests/*.test.cjs`.
