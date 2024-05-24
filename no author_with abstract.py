import pandas as pd

text_file_path = '<input file path, in .txt format>'  #change the input location

with open(text_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

title = []
year = []
journal = []
url = []
abstract = []
current_title = None
current_year = None
current_journal = None
current_abstract = None

for line in lines:
    line = line.strip()
        
    if line.startswith('title'):
        current_title = line[:-1]
        start_index = current_title.index("{") + 1
        end_index = current_title.index("}")
        current_title = current_title[start_index:end_index]
        title.append(current_title)
        
    
    if line.startswith('year'):
        current_year = line[:]
        start_index = current_year.index("{") + 1
        end_index = current_year.index("}")
        current_year = current_year[start_index:end_index]
        year.append(current_year)
        
    if line.startswith('doi'):
        current_url = line[:]
        start_index = current_url.index("{") + 1
        end_index = current_url.index("}")
        current_url = current_url[start_index:end_index]
        url.append(current_url)

    if line.startswith('journal'):
        current_journal = line[:-1]
        start_index = current_journal.index("{") + 1
        end_index = current_journal.index("}")
        current_journal = current_journal[start_index:end_index]
        journal.append(current_journal)

    if line.startswith('abstract'):
        current_abstract = line[:]
        start_index = current_abstract.index("{") + 1
        end_index = current_abstract.index("}")
        current_abstract = current_abstract[start_index:end_index]
        abstract.append(current_abstract)


data = {'Title': title, 'Year': year, 'Journal': journal, "Source": url, 'Abstract': abstract}
df_title = pd.DataFrame(data)

df_title.sort_values(by='Title', inplace=True)

excel_path = '<output file path, in .xlsx format>' #change the output location
writer = pd.ExcelWriter(excel_path)

df_title.to_excel(writer, sheet_name='Title', index=False)

df_year = pd.DataFrame({'Year': year})
df_year.sort_values(by='Year', inplace=True)

df_journal = pd.DataFrame({'Journal': journal})
df_journal.sort_values(by='Journal', inplace=True)

df_url = pd.DataFrame({'Source': url})
df_url.sort_values(by='Source', inplace=True)

df_url = pd.DataFrame({'Abstract': abstract})
df_url.sort_values(by='Abstract', inplace=True)


# Save the Excel file
writer.save()
