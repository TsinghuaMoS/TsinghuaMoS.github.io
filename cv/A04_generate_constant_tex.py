import csv

import pandas as pd
from scholarly import scholarly
import numpy as np
from A01_common_func import title_case, author_sequence, author_sequence, format_authors

# Search for the author by name
user_id = 'ORhrfXoAAAAJ'
author_filled = scholarly.search_author_id(user_id)


# Display basic author information
print(f"Author Name: {author_filled['name']}")
print(f"Affiliation: {author_filled['affiliation']}")
print(f"Total Citations: {author_filled.get('citedby', 'N/A')}")

total_citation = author_filled.get('citedby', 'N/A')

file_path = 'papers.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)
df = df.where(pd.notnull(df), None)
df = df.astype(object).replace({np.nan: None})
# Add a column for first-authored status
df[['is_first_authored', 'author_position']] = df['authors'].apply(
    lambda x: pd.Series(author_sequence(x))
)
num_q1top = len(df.loc[(df['CAS_Q'] == 1) & (df['if_CAS_Top'] == 1)])
total_IF = round(sum(df.loc[~df['impact_factor'].isnull()]['impact_factor']))
first_author_IF = round(sum(df.loc[(df['is_first_authored'] == 1) & (~df['impact_factor'].isnull())]['impact_factor']))

text_content = f"""
\\newcommand{{\\totalcitation}}{{{total_citation}}}
\\newcommand{{\\topnum}}{{{num_q1top}}}
\\newcommand{{\\totalif}}{{{total_IF}}}
\\newcommand{{\\firstauthorif}}{{{first_author_IF}}}
"""

# File path to save the content
file_path = "constants_latex_CN.txt"

# Saving the content to a text file
with open(file_path, 'w') as file:
    file.write(text_content)




# Initialize a list to hold all publication details
# publications_data = []
#
# # Iterate through each publication and save details to a dictionary
# for pub in author_filled['publications']:
#     publication = {
#         "Title": pub['bib'].get('title', "N/A"),
#         "Journal": pub['bib'].get('journal', "N/A"),
#         "Year": pub['bib'].get('pub_year', "N/A"),
#         "Volume": pub['bib'].get('volume', "N/A"),
#         "Issue": pub['bib'].get('issue', "N/A"),
#         "Pages": pub['bib'].get('pages', "N/A"),
#         "DOI": pub['bib'].get('doi', "N/A"),
#         "Authors": ", ".join(pub['bib'].get('author', ["N/A"])),
#         "Citations": pub.get('num_citations', 0),
#     }
#     publications_data.append(publication)
#
# # Save the dictionary data to a CSV file
# csv_file = "publications_detailed.csv"
# csv_columns = [
#     "Title", "Journal", "Year", "Volume", "Issue",
#     "Pages", "DOI", "Authors", "Citations"
# ]
#
# # Write the CSV file
# try:
#     with open(csv_file, "w", newline="", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=csv_columns)
#         writer.writeheader()
#         writer.writerows(publications_data)
#     print(f"Publications data successfully saved to {csv_file}")
# except Exception as e:
#     print(f"Error saving data to CSV: {e}")
#
# # Optional: Print the dictionary for verification
# for pub in publications_data:
#     print(pub)
