import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from A01_common_func import title_case, author_sequence, author_sequence, format_authors, get_journal_issue, \
    get_paper_type, print_stats


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
    df = df.astype(object).replace({np.nan: None})
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

    num_J = len(df.loc[df['paper_type'] == 'J'])
    num_C = len(df.loc[df['paper_type'] == 'C'])
    num_P = len(df.loc[df['paper_type'] == 'P'])

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

        paper_type_part = get_paper_type(row, version='CN')



        # Base entry format
        entry = (paper_type_part+ "{{{}}}".format(f"\\textbf{{{title}}}{doi_part}"))
        entry += "{{\\newline {}}}".format(formatted_authors)
        entry += "{{\\newline \\emph{{{}}}}}".format(journal_issue_part)
        entry += "{{"
        entry += ("\\; \\keys{SCI} " if row['if_sci'] == 1 else "")
        entry += (f"\\keys{{IF {round(row['impact_factor'],1)}}} " if row['impact_factor'] else "")
        entry += (f"\\keys{{Q{int(round(row['CAS_Q']))}}} " if row['CAS_Q'] else "")
        entry += ("\\keys{Top} " if row['if_CAS_Top'] else "")
        entry += "}}{}\n"
        entry += "\\vspace{7pt}\n"
        # Add stepcounter logic based on paper type
        if row['paper_type'] == 'J':
            # if len(cventries_J) != num_J-1:
                # last one not add
            entry = "\\stepcounter{myCounter}\n" + entry
            if row['is_first_authored']:
                entry = "\\stepcounter{myFirstAuthor}\n" + entry
            cventries_J.append(entry)

        elif row['paper_type'] == 'C':
            # if len(cventries_C) != num_C - 1:
            entry = "\\stepcounter{myCounterNew}\n" + entry
            cventries_C.append(entry)
        else:
            # if len(cventries_P) != num_P - 1:
            entry = "\\stepcounter{myPrePrint}\n" + entry
            cventries_P.append(entry)

        # Add LaTeX sections and preambles
        result = ""

        # Journal Publications
        if cventries_J:
            result += "\\section{期刊论文}\n"
            result += (
                "{\\small{\href{https://scholar.google.com/citations?user=ORhrfXoAAAAJ&hl=en}{\\textcolor{blue}{\\underline{[Google Scholar}}}}\\; ; \\;}"
                "{\\small{\href{https://www.researchgate.net/profile/Baichuan-Mo}{\\textcolor{blue}{\\underline{Research Gate]}}}}}"
                "\\quad {\\small{* 代表通讯作者，}}{\\small{$ ^ \\dagger$ 代表贡献相同，\\keys{Q1-4}代表中科院分区，\\keys{Top}代表中科院Top期刊}，\\keys{IF}代表论文发表时的期刊影响因子}{}{}\n\n"
                "\\vspace{7pt}\n\n"
            )
        result += "\n\n".join(cventries_J) + "\n\n"

        # Conference Proceedings
        if cventries_C:
            result += "\\section{会议论文}\n" + "\n\n".join(cventries_C) + "\n\n" + "\\vspace{7pt}\n\n"

        # In Preparation
        if cventries_P:
            result += (
                    "\\section{在投或准备中论文}\n"
                    "{\small{所有论文初稿均已完成}}{}{}{}\n\n"
                    "\\vspace{7pt}"
                    + "\n\n".join(cventries_P)
                    + "\n\n"
            )


    return result

if __name__ == '__main__':
    # Example usage
    file_path = 'papers.xlsx'  # Replace with the path to your Excel file
    result = generate_cventries_from_excel(file_path)

    # Save or print the results
    with open('publication_CN.txt', 'w') as f:
        f.write(result)
    print("Cventries saved to 'publication_CN.txt'")