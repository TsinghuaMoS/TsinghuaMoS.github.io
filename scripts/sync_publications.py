#!/usr/bin/env python3
"""Generate website and both CV publication lists from documents/papers.xlsx.

Use --build-cv to compile the PDFs, or --check for a read-only text drift check.
"""
import argparse
import html
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / 'documents/papers.xlsx'
sys.path.insert(0, str(ROOT / 'cv'))
from A01_common_func import author_sequence
from A02_generate_CV_EN import generate_cventries_from_excel as generate_en
from A03_generate_CV_CN import generate_cventries_from_excel as generate_cn

TYPES = {'C': (1, 'Conference Paper'), 'J': (2, 'Journal Article'),
         'B': (3, 'Book Chapter'), 'P': (4, 'Preprint / Working Paper')}
CATEGORIES = {'Public Transit Resilience', 'Travel Behavior & Demand',
              'Mobility AI', 'Sustainable Urban Systems'}
FEATURE_FIELDS = ('feature_image', 'feature_title', 'feature_description',
                  'feature_title_zh', 'feature_description_zh', 'feature_alt')


def read_workbook(path=WORKBOOK):
    book = openpyxl.load_workbook(path, data_only=False)
    for cells in book['Sheet1']:
        for cell in cells:
            if cell.hyperlink and isinstance(cell.value, str) and cell.value.startswith('https://'):
                if cell.hyperlink.target != cell.value:
                    raise ValueError(f'Stale Excel hyperlink at {cell.coordinate}: target differs from displayed URL')
    values = list(book['Sheet1'].values)
    rows = [dict(zip(values[0], row)) for row in values[1:] if any(v is not None for v in row)]
    for row in rows:
        for key, value in row.items():
            if isinstance(value, str):
                if value.startswith('='):
                    raise ValueError(f'Literal publication metadata required, not a formula: {key}')
                row[key] = value.strip() if value.strip() != 'NA' else None
    settings = {r[0]: r[1] for r in list(book['Settings'].values)[1:] if r[0]}
    book.close()
    validate(rows)
    return rows, settings


def validate(rows):
    seen, dois = set(), set()
    for row in rows:
        for field in ('title', 'authors', 'paper_type', 'journal', 'category'):
            if not row.get(field):
                raise ValueError(f'Missing {field}: {row.get("title")}')
        title = row['title']
        key = (row['paper_type'], title.casefold())
        if key in seen:
            raise ValueError(f'Duplicate publication: {title}')
        seen.add(key)
        if row['paper_type'] not in TYPES or row['category'] not in CATEGORIES:
            raise ValueError(f'Invalid paper type/category: {title}')
        if row['paper_type'] != 'P' and not row.get('year'):
            raise ValueError(f'Missing publication year: {title}')
        names = {n.strip() for n in row['authors'].split(',')}
        for field in ('corresponding_authors', 'co_first_authors'):
            if not {n.strip() for n in (row.get(field) or '').split(',') if n.strip()} <= names:
                raise ValueError(f'{field} contains a name absent from authors: {title}')
        doi = row.get('doi')
        if doi:
            if not doi.startswith('https://doi.org/10.'):
                raise ValueError(f'Use a DOI URL in doi; other links belong in external_url: {title}')
            if doi.lower() in dois:
                raise ValueError(f'Duplicate DOI: {doi}')
            dois.add(doi.lower())
        for field in ('external_url', 'code_url'):
            if row.get(field) and urlparse(row[field]).scheme not in ('http', 'https'):
                raise ValueError(f'Invalid {field}: {title}')
        for field in ('pdf_url', 'feature_image'):
            if row.get(field):
                path = (ROOT / unquote(row[field]).lstrip('/')).resolve()
                if not row[field].startswith('/') or not path.is_relative_to(ROOT) or not path.is_file():
                    raise ValueError(f'Missing or invalid local {field}: {row[field]}')


def authors_html(row):
    corresponding = {n.strip() for n in (row.get('corresponding_authors') or '').split(',')}
    equal = {n.strip() for n in (row.get('co_first_authors') or '').split(',')}
    result = []
    for name in map(str.strip, row['authors'].split(',')):
        text = html.escape(name)
        if name == 'Baichuan Mo':
            text = f'<strong class="author-me">{text}</strong>'
        elif name in corresponding:
            text = f'<span class="author-corresponding-name">{text}</span>'
        elif name in equal:
            text = f'<span class="author-equal-name">{text}</span>'
        if name in equal:
            text += '<sup class="author-equal">&dagger;</sup>'
        if name in corresponding:
            text += '<sup class="author-corresponding">*</sup>'
        result.append(text)
    return ', '.join(result)


def website_record(row):
    kind, label = TYPES[row['paper_type']]
    year = int(row['year']) if row.get('year') else None
    venue = row['journal']
    issue = str(row.get('issue_page') or '')
    first, _ = author_sequence(row['authors'], row.get('co_first_authors'))
    quartile = f'Q{int(row["CAS_Q"])}' if row.get('CAS_Q') else ''
    if quartile and row.get('if_CAS_Top'):
        quartile += ' Top'
    out = dict(title=row['title'], year=year, type=kind, paper_type=row['paper_type'],
               category=row['category'], category_label=label, venue=venue,
               issue_page=issue, venue_display=', '.join(str(v) for v in (venue, year, issue) if v),
               authors_text=row['authors'], authors_html=authors_html(row),
               corresponding_authors=row.get('corresponding_authors') or '',
               co_first_authors=row.get('co_first_authors') or '',
               pdf_url=row.get('pdf_url') or '',
               external_url=row.get('doi') or row.get('external_url') or '',
               external_label='DOI' if row.get('doi') else row.get('external_label') or '',
               code_url=row.get('code_url') or '',
               impact_factor=f'{row["impact_factor"]:.1f}' if row.get('impact_factor') is not None else '',
               cas_quartile=quartile, if_sci=bool(row.get('if_sci')),
               first_author=bool(first), featured=bool(row.get('if_featured')))
    for field in FEATURE_FIELDS:
        if field == 'feature_image' or row.get(field):
            out[field] = row.get(field) or ''
    return out


def outputs(rows, settings):
    ordered = sorted(rows, key=lambda r: -(r.get('year') or 0))
    records = [website_record(r) for r in ordered]
    website = '# GENERATED from documents/papers.xlsx. Do not edit directly.\n'
    website += '# Run: python3 scripts/sync_publications.py --build-cv\n\n'
    website += yaml.safe_dump(records, sort_keys=False, allow_unicode=True, width=10000)
    en, cn = generate_en(WORKBOOK), generate_cn(WORKBOOK)
    warning = '% GENERATED from documents/papers.xlsx; run scripts/sync_publications.py.\n'
    en, cn = warning + en, warning + cn
    stats = {
        'totalcitation': int(settings['total_citation']),
        'topnum': sum(r.get('CAS_Q') == 1 and r.get('if_CAS_Top') == 1 for r in rows),
        'totalif': round(sum(r.get('impact_factor') or 0 for r in rows)),
        'firstauthorif': round(sum((r.get('impact_factor') or 0) for r in rows
                                  if author_sequence(r['authors'], r.get('co_first_authors'))[0])),
    }
    constants = warning + '\n' + ''.join(f'\\newcommand{{\\{k}}}{{{v}}}\n' for k, v in stats.items())
    return {
        '_data/publist.yml': website,
        'cv/publication_EN.txt': en,
        'cv/CV_Baichuan_Academia_EN/b02_publications.tex': en,
        'cv/publication_CN.txt': cn,
        'cv/CV_Baichuan_CN/b_publication.tex': cn,
        'cv/CV_Baichuan_CN/a_constants.tex': constants,
    }


def build_cvs():
    jobs = [('EN', 'CV_Baichuan_Academia_EN', 'a01_main'), ('CN', 'CV_Baichuan_CN', 'a_main')]
    with tempfile.TemporaryDirectory(prefix='mos-cv-build-') as temp:
        built = []
        for language, folder, stem in jobs:
            out = Path(temp) / language
            out.mkdir()
            source = ROOT / 'cv' / folder
            for _ in range(3):
                command = ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                           f'-output-directory={out}', f'{stem}.tex']
                run = subprocess.run(command, cwd=source, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                if run.returncode:
                    raise RuntimeError(f'{language} CV build failed:\n{run.stdout[-8000:]}')
            built.append((language, source, stem, out / f'{stem}.pdf'))
        # Do not replace published copies until both languages compile successfully.
        for language, source, stem, pdf in built:
            for target in (source / f'{stem}.pdf', ROOT / 'cv' / f'CV_Baichuan_{language}.pdf',
                           ROOT / '_site_file/cv' / f'CV_Baichuan_{language}.pdf'):
                shutil.copy2(pdf, target)
            print(f'Built cv/CV_Baichuan_{language}.pdf')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Read-only text check; PDFs are not rebuilt')
    mode.add_argument('--build-cv', action='store_true', help='Also compile and synchronize all CV PDF copies')
    args = parser.parse_args()
    rows, settings = read_workbook()
    changed = []
    for name, content in outputs(rows, settings).items():
        path = ROOT / name
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            changed.append(name)
            if not args.check:
                path.write_text(content, encoding='utf-8')
    if args.check and changed:
        sys.exit('Out-of-sync generated files:\n' + '\n'.join(changed))
    if args.build_cv:
        build_cvs()
    print(f'{len(rows)} publications validated; {len(changed)} generated text files changed.')


if __name__ == '__main__':
    main()
