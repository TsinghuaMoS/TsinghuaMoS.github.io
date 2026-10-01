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

Maintain the canonical title in `documents/papers.xlsx` (`Sheet1.title`). The website and both CVs use that exact sentence-case title, without independent recasing. Then run from the repository root:

```
python3 scripts/sync_publications.py --build-cv
```

The old `sentence_case_titles.py` and `cv/A02`–`A04` entry points now delegate to the unified generator. They no longer maintain separate publication lists.

## Adding a new publication — checklist

1. **`documents/papers.xlsx` → `Sheet1`** — add one row. This is the sole source for **all publication metadata**, not just the CV. The workbook's `Guide` sheet documents every field. Main fields:
   - `title` — sentence case (see rule above).
   - `year`, `paper_type` (`J`/`C`/`B`/`P`). For published papers, use the volume/issue year, not the first-online year. Preprints may have a blank year.
   - `category` — exactly one of the four directions: `Public Transit Resilience`, `Travel Behavior & Demand`, `Mobility AI`, `Sustainable Urban Systems`. **No other labels.**
   - `journal`, `issue_page`; the generator derives the website's venue display.
   - `authors`, `corresponding_authors`, `co_first_authors`: plain comma-separated full names, with identical spelling. Website author markup and CV symbols are generated.
   - `doi`: a DOI URL only. Put OpenReview/other landing pages in `external_url` and their label in `external_label`. DOI takes display priority. Leave unavailable links blank; do not invent DOIs.
   - `pdf_url` — put the PDF in `documents/publication/journals/`, `documents/publication/conferences/`, or `documents/publication/preprints/` according to `type`, and use a URL-encoded path (spaces → `%20`, commas → `%2C`, plus signs → `%2B`).
   - `code_url` — repo link if any.
   - `impact_factor` (preserve source precision; displayed to 1 decimal), `CAS_Q` (1–4), `if_CAS_Top`, `if_sci`. Historical metrics are not automatically updated.
   - `if_featured` (1/0) + `feature_image` — see step 3.
   - `metadata_source`, `metadata_notes`: verification provenance and unresolved issues, not displayed publicly. Original Chinese comments/descriptions remain in the workbook.
2. **PDF** — add the file under the matching `documents/publication/{journals,conferences,preprints}/` folder; reference it from `pdf_url`.
3. **Feature it (optional)** — set Excel `if_featured` to 1. This generates the amber **"Featured"** badge + purple border and the "★ Featured only" filter. To also show a **Featured Research card**, add `feature_image` and optionally `feature_title`, `feature_description`, `feature_alt`, `feature_title_zh`, `feature_description_zh`. Follow `FEATURED_RESEARCH_IMAGES.md`. The grids show the **4 most recent** featured papers with an image. Featured papers should be Baichuan-Mo first/co-first authored.
4. **News** — add a line to `_data/news.yml`.
5. **Generate and verify** — run `python3 scripts/sync_publications.py --build-cv`, then `python3 scripts/sync_publications.py --check`. This updates `_data/publist.yml`, both CV publication sources/text copies, publication statistics, both downloadable PDFs, and their tracked legacy copies. Do not edit generated files directly. Review PDF layout and build the Jekyll site before publishing.
6. **Commit & push** — pushing to `main` rebuilds and deploys via GitHub Actions.

`Settings` contains the citation-count value retained from the previous CV until explicitly verified and updated. The generator does not query Scholar. CVs use the original external-link icon for the DOI or an online paper landing page such as OpenReview, not local PDF or code links; the website keeps all links. Education, employment, awards, recruitment, and other non-publication content still use their existing source files; this workbook migration covers publication data only.

## Adding a team member

Edit `_data/team_members.yml` (group codes: `0` PI · `7` Researchers · `1` PhD · `2` MSc · `3` Undergrad · `4` Interns · `8` Alumni), add the photo to `images/teampic/`, and a profile markdown to `team/` if needed.

## PI personal-information synchronization

Whenever the PI biography, position, education, employment dates, contact details, research summary, awards, or representative publications change, update all applicable copies together:

1. Website profile and recruitment content in `team/baichuan_mo.md`, `team/baichuan_mo_zh.md`, and `_pages/admission.md`.
2. English and Chinese CV sources and generated PDFs under `cv/`.
3. The two local Tsinghua faculty-profile forms:
   - `private/tsinghua_profile_forms/清华大学土水学院教师个人信息登记表（中文）_填写版.docx`
   - `private/tsinghua_profile_forms/清华大学土水学院教师个人信息登记表（英文）_填写版.docx`

The two `.docx` forms are intentionally ignored by Git because this is a public repository and the forms may contain personal information. Keep them local and visually verify both documents after every content update.

## Logos (funding / collaborating institutions)

Drop the official logo into `images/funding/` or `images/partners/`, then trim whitespace and normalize it to a uniform content height on a white background (so the row stays even). Each logo links to the institution's site with a `title` for the hover name.

For new **Research Support / 科研支持** logos, use the current Mercedes-Benz mark as the visual-size reference: its dedicated class renders it at `50px` high, giving it approximately the same perceived size and visual weight as the NSFC emblem. Match this perceived footprint rather than blindly giving every source image the same CSS height, since logos contain different amounts of internal whitespace. Use a logo-specific class when adjustment is needed, and verify alignment at both desktop and `390px` mobile widths.
