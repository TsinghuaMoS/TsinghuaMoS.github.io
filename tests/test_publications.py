"""Regression checks for the Excel -> website/CV publication pipeline."""
import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import sync_publications as sync
from A01_common_func import latex_text, publication_links


class PublicationsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.settings = sync.read_workbook()

    def test_generated_files_match_excel(self):
        for filename, text in sync.outputs(self.rows, self.settings).items():
            with self.subTest(filename=filename):
                self.assertEqual((ROOT / filename).read_text(encoding='utf-8'), text)

    def test_titles_authors_and_links_match_across_outputs(self):
        site = yaml.safe_load((ROOT / '_data/publist.yml').read_text())
        index = {(r['paper_type'], r['title']): r for r in site}
        self.assertEqual(len(site), len(self.rows))
        for row in self.rows:
            item = index[row['paper_type'], row['title']]
            self.assertEqual(item['authors_text'], row['authors'])
            self.assertEqual(item['external_url'], row.get('doi') or row.get('external_url') or '')
            self.assertEqual(item['pdf_url'], row.get('pdf_url') or '')
            for language in ('EN', 'CN'):
                cv = (ROOT / f'cv/publication_{language}.txt').read_text()
                self.assertIn(latex_text(row['title']), cv)
                self.assertIn(publication_links(row), cv)
        for language in ('EN', 'CN'):
            cv = (ROOT / f'cv/publication_{language}.txt').read_text()
            self.assertNotIn('[PDF]', cv)
            self.assertNotIn('[Code]', cv)
            self.assertNotIn('[DOI]', cv)
            self.assertNotIn('[OpenReview]', cv)
            self.assertEqual(cv.count('faExternalLink'), sum(bool(r.get('doi') or r.get('external_url')) for r in self.rows))

    def test_conflux_and_known_metadata_corrections(self):
        conflux = next(r for r in self.rows if r['title'].startswith('ConFlux:'))
        self.assertEqual(conflux['paper_type'], 'C')
        self.assertIn('ICML 2026', conflux['journal'])
        self.assertTrue(conflux['pdf_url'])
        mobility = next(r for r in self.rows if r['title'].startswith('Individual mobility prediction'))
        self.assertEqual(mobility['doi'], 'https://doi.org/10.1109/TITS.2021.3109428')
        housing = next(r for r in self.rows if r['title'].startswith('Housing exchange'))
        self.assertEqual(housing['doi'], 'https://doi.org/10.1038/s41893-025-01658-x')
        ex_post = next(r for r in self.rows if r['title'].startswith('Ex post path choice'))
        self.assertEqual(ex_post['year'], 2023)
        self.assertTrue(all(r.get('doi') for r in self.rows if r['paper_type'] == 'J'))

    def test_validation_rejects_duplicate_doi_and_missing_pdf(self):
        changed = copy.deepcopy(self.rows)
        changed[1]['doi'] = changed[0]['doi']
        with self.assertRaisesRegex(ValueError, 'Duplicate DOI'):
            sync.validate(changed)
        changed = copy.deepcopy(self.rows)
        changed[0]['pdf_url'] = '/documents/publication/not-a-real-paper.pdf'
        with self.assertRaisesRegex(ValueError, 'Missing or invalid local'):
            sync.validate(changed)

    def test_cv_uses_one_online_paper_icon_and_tex_escaping(self):
        links = publication_links({'external_url': 'https://openreview.net/forum?id=test', 'external_label': 'OpenReview', 'pdf_url': '/paper%20one.pdf'})
        self.assertIn('https://openreview.net/forum?id=test', links)
        self.assertIn(r'\faExternalLink', links)
        self.assertNotIn('paper', links)
        self.assertEqual(publication_links({'pdf_url': '/paper.pdf'}), '')
        links = publication_links({'doi': 'https://doi.org/10.1234/test', 'pdf_url': '/paper.pdf', 'code_url': 'https://example.org/code'})
        self.assertIn(r'\faExternalLink', links)
        self.assertIn('https://doi.org/10.1234/test', links)
        self.assertNotIn('[DOI]', links)
        self.assertNotIn('paper.pdf', links)
        self.assertNotIn('example.org/code', links)
        self.assertEqual(latex_text('TimeMixer++ & 0.6%'), r'TimeMixer++ \& 0.6\%')
        self.assertEqual(latex_text('origin–destination; Computer‐Aided'), 'origin--destination; Computer-Aided')


if __name__ == '__main__':
    unittest.main()
