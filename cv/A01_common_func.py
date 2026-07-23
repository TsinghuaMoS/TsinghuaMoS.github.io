import numpy as np
import pandas as pd


def title_case(title):
    """
    Converts a string to title case, including handling dash-separated words,
    while excluding specific small words from capitalization.

    Args:
        title (str): The original title.

    Returns:
        str: The title-cased string.
    """
    small_words = {'of', 'on', 'with', 'and', 'but', 'or', 'nor', 'the', 'for', 'in', 'to', 'at', 'by',
                   'from'}
    words_map = {'covid-19': 'COVID-19', 'timemixer++:': 'TimeMixer$^{++}$:', 'v2i': 'V2I', 'scope-moe:': 'SCOPE-MoE:',
                 'moe-based': 'MoE-Based', 'conflux:': 'ConFlux:'
                 }
    def capitalize_word(word, is_first_word):
        # Handle dash-separated words
        parts = word.split('-')
        capitalized_parts = [
            part.capitalize() if is_first_word or part.lower() not in small_words else part.lower()
            for part in parts
        ]
        return '-'.join(capitalized_parts)

    words = title.split()
    title_cased = [
        capitalize_word(word, i == 0) for i, word in enumerate(words)
    ]

    title_cased_modified = [words_map[key.lower()] if key.lower() in words_map else key for key in title_cased]
    final = ' '.join(title_cased_modified)

    return final


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
    if row['year'] and row['paper_type'] == 'J':
        journal_issue_part += f", {int(round(row['year']))}"
    if row['issue_page']:
        journal_issue_part += f", {row['issue_page']}"
    journal_issue_part = journal_issue_part.replace('%', '\%')
    return journal_issue_part



def get_paper_type(row, version):

    if row['year'] is None or np.isnan(row['year']):
        year = ''
    else:
        year = str(int(round(row['year'])))
    if row['paper_type'] == 'J':
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyCounter, {}]\;}}}}".format('J', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyCounter]}} {}}}".format('J', year)
    elif row['paper_type'] == 'C':
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyCounterNew, {}]\;}}}}".format('C', year)
        else:
            paper_type_part = "\\cventry{{\\textcolor{{gray}}{{[{}\\themyCounterNew]}} {}}}".format('C', year)
    else:
        year = ''
        if version == 'CN':
            paper_type_part = "{{\\textcolor{{gray}}{{[{}\\themyPrePrint]\;}}}}".format('P', year)
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

