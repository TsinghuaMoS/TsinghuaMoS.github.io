import numpy as np
import pandas as pd

def latex_text(value):
    """Escape text without changing the canonical wording stored in Excel."""
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%',
                    '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{',
                    '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
                    '–': '--', '—': '---', '‐': '-', '‑': '-'}
    return ''.join(replacements.get(c, c) for c in str(value or ''))


def publication_links(row):
    """CV: one original-style icon for the DOI or online paper landing page."""
    url = row.get('doi') or row.get('external_url')
    if not url:
        return ''
    return (r' \href{' + latex_text(url)
            + r'}{\textcolor{cadmiumorange}{\faExternalLink}}')


def format_authors(authors, co_first_authors, corresponding_authors):
    """
    Formats authors with appropriate LaTeX notation for underlining, co-first authorship, and corresponding authorship.

    Args:
        authors (str): Comma-separated string of all authors.
        co_first_authors (str): Comma-separated string of co-first authors.
        corresponding_authors (str): Comma-separated string of corresponding authors.

    Returns:
        str: LaTeX-formatted authors.
    """
    authors_list = [author.strip() for author in authors.split(',')]
    co_first_set = []
    if isinstance(co_first_authors, str):
        co_first_set = [author.strip() for author in co_first_authors.split(',')]

    corresponding_set = []
    if isinstance(corresponding_authors, str):
        corresponding_set = [author.strip() for author in
                             corresponding_authors.split(',')] if corresponding_authors else []

    formatted_authors = []
    for author in authors_list:
        formatted_author = author
        if author == 'Haris N Koutsopoulos':
            formatted_author = 'Haris N. Koutsopoulos' # correct haris's name
        if author == "Baichuan Mo":  # Always underline Baichuan Mo
            formatted_author = f"\\underline{{{author}}}"
        if author in co_first_set:
            formatted_author += "$^\\dagger$"
        if author in corresponding_set:
            formatted_author += "*"
        formatted_authors.append(formatted_author)

    return ', '.join(formatted_authors)



def author_sequence(authors, co_first_authors):
    author_list = [a.strip() for a in authors.split(',')]
    try:
        position = author_list.index("Baichuan Mo") + 1  # +1 because index starts at 0
    except ValueError:
        position = None  # Target author not found
    is_first_authored = position == 1
    if co_first_authors and 'Baichuan Mo' in co_first_authors:
        is_first_authored = True
    return is_first_authored, position


def get_journal_issue(row):
    journal_issue_part = ''
    if row['journal']:
        journal_issue_part += row['journal']
    if row['year'] and row['paper_type'] in {'J', 'B'}:
        journal_issue_part += f", {int(round(row['year']))}"
    if row['issue_page']:
        journal_issue_part += f", {row['issue_page']}"
    return latex_text(journal_issue_part)



def get_paper_type(row, version):

    if row['year'] is None or np.isnan(row['year']):
        year = ''
    else:
        year = str(int(round(row['year'])))
    if row['paper_type'] == 'J':
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyCounter, {}]\\;}}}}".format('J', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyCounter]}} {}}}".format('J', year)
    elif row['paper_type'] == 'C':
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyCounterNew, {}]\\;}}}}".format('C', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyCounterNew]}} {}}}".format('C', year)
    elif row['paper_type'] == 'B':
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyBookChapter, {}]\\;}}}}".format('B', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyBookChapter]}} {}}}".format('B', year)
    else:
        year = ''
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyPrePrint]\\;}}}}".format('P', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyPrePrint]}} {}}}".format('P', year)


    return paper_type_part


def print_stats(df):
    print(f"num journal: {len(df.loc[(df['paper_type'] == 'J')])}")
    print(f"num CAS Q1 & Top: {len(df.loc[(df['CAS_Q'] == 1) & (df['if_CAS_Top'] == 1)])}")
    print(f"num first author journal: {len(df.loc[(df['paper_type'] == 'J') & (df['is_first_authored'] == 1)])}")
    print(f"total IF: {round(sum(df.loc[~df['impact_factor'].isnull()]['impact_factor']))}")
    print(f"first author IF: {round(sum(df.loc[(df['is_first_authored']==1)&(~df['impact_factor'].isnull())]['impact_factor']))}")
    return None
# Apply the function to the DataFrame

