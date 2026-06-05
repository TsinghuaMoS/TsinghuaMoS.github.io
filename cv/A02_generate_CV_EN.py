import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from A01_common_func import title_case, author_sequence, author_sequence, format_authors, get_journal_issue, get_paper_type, print_stats


def generate_cventries_from_excel(file_path):
    """
    Generates formatted LaTeX entries for all papers in the Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        str: LaTeX-formatted sections for journal publications, conference proceedings, and in preparation.
    """
    df = pd.read_excel(file_path)
    df = df.where(pd.notnull(df), None)
    # Add a column for first-authored status
    df[['is_first_authored', 'author_position']] = df[['authors','co_first_authors']].apply(
        lambda row: pd.Series(author_sequence(row['authors'], row['co_first_authors'])),
        axis=1
    )

    # Sort the DataFrame by year (descending), first-authored (True first), and impact factor (descending)
    df = df.sort_values(by=['year', 'author_position', 'impact_factor'], ascending=[False, True, False])
    df = df.reset_index(drop=True)
    # Separate entries by paper type
    cventries_J = []
    cventries_C = []
    cventries_P = []

    print_stats(df)


    for idx, row in df.iterrows():
        formatted_authors = format_authors(
            authors=row['authors'],
            co_first_authors=row['co_first_authors'],
            corresponding_authors=row['corresponding_authors']
        )

        title = title_case(row['title'])

        # Check if DOI exists
        doi_part = ""
        if row['doi']:
            doi_part = f" \\href{{{row['doi']}}}{{\\textcolor{{cadmiumorange}}{{\\faExternalLink}}}}"

        ### get journal issue
        journal_issue_part = get_journal_issue(row)

        paper_type_part = get_paper_type(row, version = 'EN')

        # Base entry format
        entry = (paper_type_part+ "{{{}}}".format(f"{title}{doi_part}"))
        entry += "{{\\newline {}}}".format(formatted_authors)
        entry += "{{\\newline \\emph{{{}}}}}".format(journal_issue_part)
        entry += "{{"
        entry += ("\\; \\keys{SCI} " if row['if_sci'] == 1 else "")
        entry += (f"\\keys{{IF {round(row['impact_factor'],1)}}}" if not np.isnan(row['impact_factor']) else "")
        entry += "}}{}\n"

        # Add stepcounter logic based on paper type
        if row['paper_type'] == 'J':
            entry = "\\stepcounter{myCounter}\n" + entry
            if row['is_first_authored']:
                entry = "\\stepcounter{myFirstAuthor}\n" + entry
            cventries_J.append(entry)
        elif row['paper_type'] == 'C':
            entry = "\\stepcounter{myCounterNew}\n" + entry
            cventries_C.append(entry)
        else:
            entry = "\\stepcounter{myPrePrint}\n" + entry
            cventries_P.append(entry)

        # Add LaTeX sections and preambles
        result = ""

        # Journal Publications
        if cventries_J:
            result += "\\section{Journal Publications}\n"
            result += (
                "\\cventry{}{}\n"
                "{\\small{\\href{https://scholar.google.com/citations?user=ORhrfXoAAAAJ&hl=en}{\\textcolor{blue}{\\underline{[Google Scholar}}}} ; }\n"
                "{\\small{\\href{https://www.researchgate.net/profile/Baichuan-Mo}{\\textcolor{blue}{\\underline{Research Gate]}}}}}\n"
                "{}{}\n"
                "\\cventry{}{}{\small{* means corresponding author. }}{\small{$^\\dagger$ means contributing equally}}{}{}\n\n"
            )
        result += "\n\n".join(cventries_J) + "\n\n"

        # Conference Proceedings
        if cventries_C:
            result += "\\section{Conference Proceedings}\n" + "\n\n".join(cventries_C) + "\n\n"

        # In Preparation
        if cventries_P:
            result += (
                    "\\section{In Preparation}\n"
                    "\\cventry{}{}{\small{All manuscripts are available upon reasonable requests}}{}{}{}\n\n"
                    + "\n\n".join(cventries_P)
                    + "\n\n"
            )


    return result

if __name__ == '__main__':
    # Example usage
    file_path = 'papers.xlsx'  # Replace with the path to your Excel file
    result = generate_cventries_from_excel(file_path)

    # Save or print the results
    with open('publication_EN.txt', 'w') as f:
        f.write(result)
    print("Cventries saved to 'publication_EN.txt'")