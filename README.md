<h1 align="center">ISLGrind</h1>
<p align="center"><b>An adaptive trainer for the hardest pre-olympiad math problems on Earth.</b><br>
Practice 1,627 olympiad problems — the <a href="https://www.imo-official.org/">IMO Shortlist</a> plus USAMO, USA TST/TSTST, EGMO, APMO, and RMM — and the difficulty adapts to you, topic by topic.</p>

<p align="center">🔗 <b>Live:</b> <a href="https://islgrind.vercel.app">islgrind.vercel.app</a></p>

---

## What it is

The **IMO Shortlist** is the pool of ~30 problems each year from which the International Mathematical Olympiad exam is chosen — the gold standard of hard, beautiful math. ISLGrind turns 35 years of them into a personal coach:

- 🎯 **Adaptive, per-topic difficulty.** Algebra, Combinatorics, Geometry, and Number Theory each get their own ability estimate. Like a good tutor, ISLGrind serves you problems a notch *above* your level — and updates by how *surprising* each result is (nailing a hard one moves you up a lot; missing an easy one moves you down a lot; an on-level result barely moves you).
- 🃏 **Four at a time, one per topic.** Work whichever appeals; mark it solved or not and only that card is replaced — so you're always being stretched across all four areas.
- 🏆 **Filter by competition.** Grind a single source — USAMO, EGMO, APMO, RMM, USA TST/TSTST, or the full IMO Shortlist — or mix them all.
- 👤 **Up to 4 profiles**, each with completely separate progress.
- 📚 **1,627 problems** across 7 competitions, every one rendered as clean math (not blurry PDF scans).
- 💾 **No login, no tracking.** Your progress lives entirely in your own browser.

## Use it yourself

**Easiest — just open the live site:** **[islgrind.vercel.app](https://islgrind.vercel.app)** (works on desktop and mobile; nothing to install).

**Or run it on your own computer:**
1. Click the green **`Code`** button at the top of this repo → **Download ZIP** (or `git clone https://github.com/Tensored-Flow/ISLGrind.git`).
2. Unzip it and double-click **`index.html`** — it opens in your browser and you're training.
   - *(Optional, for a cleaner setup: open a terminal in the unzipped folder and run `python3 -m http.server`, then visit the link it prints.)*
   - *Tip: to keep progress when moving between computers, use the **⬇ Backup** button to save a file and **⬆ Restore** it elsewhere.*

Your progress saves automatically in that browser. Pick a profile and go — solve two notches above your level, and watch each topic's bar climb.

## How it was built

The official shortlists live in PDFs whose math doesn't copy out cleanly. ISLGrind was assembled by **rendering every problem page to an image and using a vision model to transcribe the math into LaTeX**, then verifying each one — so all 1,004 problems render crisply via [KaTeX](https://katex.org/). The adaptive engine is a lightweight **Elo / item-response model** with per-topic ability and confidence that grows as you practice. It's a single static page — no backend, no accounts.

## Attribution

- **IMO Shortlist** (1,004 problems, 1990–2024) — the official shortlists, from [imo-official.org](https://www.imo-official.org/) and [The IMO Compendium](https://www.imomath.com/).
- **USAMO** (156, 2000–2025) and **EGMO 2012–2022** — from the [AoPS Wiki](https://artofproblemsolving.com/wiki/), each problem linking back to its page.
- **USA TSTST** (114, 2011–2024) and **USA TST** (79, 2012–2025) — from [Evan Chen's exam archive](https://web.evanchen.cc/problems.html).
- **EGMO 2023–2025** — from the official [egmo.org](https://www.egmo.org/) papers (EGMO is now complete, 84 problems 2012–2025).
- **RMM** (66, 2012–2025, a few editions unavailable) — from the official [Romanian Master of Mathematics](https://rmms.lbi.ro/) papers.
- **APMO** (124) — from [MathNet](https://huggingface.co/datasets/ShadenA/MathNet) (MIT, CC-BY-4.0).

All problems from PDF sources were transcribed to LaTeX and render via KaTeX; competition topics (Algebra/Combinatorics/Geometry/Number Theory) are auto-classified. Everything except APMO is year- and problem-number-labeled. All rights to the problems remain with their authors and the respective competitions. ISLGrind is a free, non-commercial study tool.
