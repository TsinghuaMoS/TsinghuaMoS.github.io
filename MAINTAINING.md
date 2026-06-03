# Maintaining the MoS Lab site

Conventions and checklists for keeping content consistent. See `README.md` for the overall structure.

## Title casing rule (publications)

All publication titles use **sentence case**: capitalize only the **first word**, the **first word after a colon**, and proper nouns / acronyms. Everything else is lowercase.

Keep capitalized:
- Proper nouns and places: `Singapore`, `Beijing`, `Nanning`, `China`, `Markov`, `Bayesian`, `MIT`, …
- Acronyms / branded names exactly as written: `COVID-19`, `V2I`, `SCOPE-MoE`, `MoE-based`, `TimeMixer++`, `IEEE`, `LLM`, …
- The first letter right after a colon, e.g. `… modeling: An empirical benchmark`.

Examples:
- ✅ `Robust transit frequency setting problem with demand uncertainty`
- ✅ `Built environment and autonomous vehicle mode choice: A first-mile scenario in Singapore`
- ✅ `SCOPE-MoE: Supply chain forecasting with a pretrained MoE-based large time series model in e-commerce`
- ❌ `Modeling Epidemic Spreading Through Public Transit Using Time-Varying Encounter Network` (Title Case — don't use)

Don't hand-fix casing — after editing `_data/publist.yml`, just run:

```
python3 scripts/sentence_case_titles.py
```

It rewrites every title to sentence case and is **idempotent** (already-correct titles are left alone, so re-running it after adding a new paper only normalizes the new entry). Genuine proper nouns are kept via the `PROPER` set, and acronyms (all-caps, internal caps, or containing digits — `IEEE`, `MoE`, `V2I`, `COVID-19`) are auto-detected; add new proper nouns to `PROPER` in that script if needed.

(The LaTeX CV applies its own Title Case via `cv/A01_common_func.py` → `title_case()`; the `words_map` there is the source of truth for special tokens like `COVID-19`, `V2I`, `TimeMixer++`, `SCOPE-MoE`, `MoE-Based`.)

## Adding a new publication — checklist

1. **`_data/publist.yml`** — add an entry (newest first). Required fields:
   - `title` — sentence case (see rule above).
   - `year`, `type` (`1`=conference, `2`=journal, `4`=preprint/working), `paper_type` (`J`/`C`/`P`).
   - `category` — exactly one of the four directions: `Public Transit Resilience`, `Travel Behavior & Demand`, `Mobility AI`, `Sustainable Urban Systems`. **No other labels.**
   - `category_label` — `Journal Article` / `Conference Paper` / `Preprint / Working Paper`.
   - `venue`, `issue_page`, `venue_display`.
   - `authors_text` (plain) and `authors_html`. In `authors_html`:
     - PI: `<strong class="author-me">Baichuan Mo</strong>`
     - corresponding: `<span class="author-corresponding-name">Name</span><sup class="author-corresponding">*</sup>`
     - equal contribution: `<sup class="author-equal">&dagger;</sup>`
   - `corresponding_authors`, `co_first_authors`.
   - `external_url` = DOI (the **title links here**; leave empty → plain title), `external_label` (`DOI`).
   - `pdf_url` — put the PDF in `documents/publication/` and use a URL-encoded path (spaces → `%20`, commas → `%2C`).
   - `code_url` — repo link if any.
   - `impact_factor` (JCR, 1 decimal) and `cas_quartile` (`Q1 Top`, `Q1`, `Q2`, `Q3`, `Q4`; empty to hide).
   - `if_sci`, `representative`, `first_author`.
   - `featured` + `feature_image` — see step 3.
2. **PDF** — add the file under `documents/publication/`; reference it from `pdf_url`.
3. **Feature it (optional)** — set `featured: true` and `feature_image: /images/featured/<name>.png`, add a matching card to `_data/featured_research.yml`, and put a **real figure from the paper** in `images/featured/`. Featured papers should be Baichuan-Mo first/co-first authored.
4. **News** — add a line to `_data/news.yml`.
5. **CV** — add the row to `documents/papers.xlsx` (the CV's data source), then rebuild both CVs (see README → CV) and place the PDFs at `cv/CV_Baichuan_EN.pdf` and `cv/CV_Baichuan_CN.pdf`.
6. **Commit & push** — pushing to `main` rebuilds and deploys via GitHub Actions.

## Adding a team member

Edit `_data/team_members.yml` (group codes: `0` PI · `7` Researchers · `1` PhD · `2` MSc · `3` Undergrad · `4` Interns · `8` Alumni), add the photo to `images/teampic/`, and a profile markdown to `team/` if needed.

## Logos (funding / collaborating institutions)

Drop the official logo into `images/funding/` or `images/partners/`, then trim whitespace and normalize it to a uniform content height on a white background (so the row stays even). Each logo links to the institution's site with a `title` for the hover name.
