# Tsinghua Mobility Science (MoS) Lab

<img src="images/lab_logo.jpg" width="450">

Source for the Tsinghua Mobility Science (MoS) Lab website, a [Jekyll](https://jekyllrb.com/) site deployed with GitHub Pages at **https://tsinghuamos.github.io/**.

## Structure

- `_pages/` — page content (`home`, `team`, `research`, `publications`, `contact`, `about`).
- `_data/` — site data: `publist.yml`, `featured_research.yml`, `team_members.yml`, `news.yml`.
- `_includes/`, `_layouts/` — templates (e.g. `publication_card.html`, `publication_line.html`).
- `css/main.scss` — styles (compiled to `/css/main.css` by Jekyll).
- `images/` — `featured/` (research figures), `funding/` (sponsor logos), `teampic/` (member photos), `hero/`.
- `cv/` — LaTeX sources and scripts for the PI's CV (see below).

Navigation: **Home · Team · Research · Publications · Contact**.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Deployment is automatic: pushing to `main` triggers the GitHub Actions workflow (`.github/workflows/jekyll.yml`), which builds the site and publishes it to GitHub Pages.

## Editing content

### Publications

Edit `_data/publist.yml`. Each entry:

```yaml
- title: 'Paper title'
  year: 2025
  type: 2                 # 1 = conference, 2 = journal, 4 = preprint / working paper
  paper_type: 'J'
  category: 'Mobility AI' # one of the four research directions (see below)
  category_label: 'Journal Article'
  venue: 'European Journal of Operational Research'
  issue_page: '327 (2), 577-591'
  venue_display: 'European Journal of Operational Research, 2025, 327 (2), 577-591'
  authors_text: 'Baichuan Mo, Yunhan Zheng, ...'
  authors_html: '<strong class="author-me">Baichuan Mo</strong>, <span class="author-corresponding-name">Yunhan Zheng</span><sup class="author-corresponding">*</sup>, ...'
  corresponding_authors: 'Yunhan Zheng'
  co_first_authors: ''
  pdf_url: ''            # local PDF under /documents/publication/ (optional)
  external_url: 'https://doi.org/...'   # paper title links here
  external_label: 'DOI'
  code_url: ''
  impact_factor: '6.0'
  cas_quartile: 'Q2'    # CAS quartile badge, e.g. 'Q1 Top', 'Q2'; empty to hide
  if_sci: true
  representative: false
  first_author: true
  featured: false        # show as a Featured Research card
  feature_image: ''
```

Author markup: wrap the PI in `<strong class="author-me">...</strong>` (bold), the corresponding author in `<span class="author-corresponding-name">...</span><sup class="author-corresponding">*</sup>`, and equal-contribution authors with `<sup class="author-equal">&dagger;</sup>`. The title links to `external_url` (the published page); papers without one show a plain title.

The four research directions used for `category`: **Public Transit Resilience**, **Travel Behavior & Demand**, **Mobility AI**, **Sustainable Urban Systems**.

### Featured Research cards

Edit `_data/featured_research.yml` and add the figure to `images/featured/`. Figures should be real images taken from the paper.

```yaml
- title: "Card title"
  theme: "Mobility AI"
  image: "/images/featured/example.png"
  alt: "Figure description"
  paper: "Full paper title"
  paper_url: "/documents/publication/example.pdf"
  description: "One-sentence summary."
```

### News

Edit `_data/news.yml`:

```yaml
- date: 2026/03/16
  headline: "New paper: <a href='...'>Title</a> appeared in Journal."
```

### Team members

Edit `_data/team_members.yml`, add the photo to `images/teampic/`, and (for profiles) a markdown file in `team/`.

```yaml
- group: 0
  info: Assistant Professor
  name: Baichuan Mo
  photo: baichuan_mo.jpg
  url: /team/baichuan_mo.html
  cv_cn: /cv/CV_Baichuan_CN.pdf   # optional CV links (open in browser)
  cv_en: /cv/CV_Baichuan_EN.pdf
```

Groups: `0` Principal Investigator · `7` Researchers · `1` PhD Students · `2` MSc Students · `3` Undergraduate Students · `4` Interns · `8` Alumni. Empty groups still show their heading with a recruiting note.

### Funding logos

Add logo images to `images/funding/` and reference them in the Research Support section of `_pages/home.md`.

## CV

The PI's CV is built from LaTeX sources in `cv/`:

- `cv/CV_Baichuan_Academia_EN/` — English CV (moderncv, XeLaTeX).
- `cv/CV_Baichuan_CN/` — Chinese CV (XeLaTeX with Chinese fonts; needs the `ctex` package).
- `A01`–`A04` Python scripts generate the publication sections and stats from `papers.xlsx`.

To rebuild after updating publications:

```bash
cd cv
cp /path/to/papers.xlsx .            # data source for the publication lists
python3 A02_generate_CV_EN.py        # -> publication_EN.txt -> b02_publications.tex
python3 A03_generate_CV_CN.py        # -> publication_CN.txt -> b_publication.tex
# compile each CV with xelatex (run twice for counters), then place the PDFs:
#   cv/CV_Baichuan_EN.pdf  and  cv/CV_Baichuan_CN.pdf
```

The Team page links to `cv/CV_Baichuan_CN.pdf` and `cv/CV_Baichuan_EN.pdf`.

## Acknowledgement

This site is built on the open-source academic lab website templates shared by the labs of [D. Allan Drummond](http://www.allanlab.org/aboutwebsite.html) and [Trevor Bedford](http://bedford.io/misc/about/), with later modifications. If you reuse this code, please credit the Drummond and Bedford labs as the original sources of the template.
