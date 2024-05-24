import pandas as pd

text_file_path = '<File path to input file, .txt format>'    #change the input location

with open(text_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

author = []
title = []
year = []
journal = []
url = []
current_author = None
current_title = None
current_year = None
current_journal = None

for line in lines:
    line = line.strip()
    
    if line.startswith('author'):
        current_author = line[:]
        start_index = current_author.index("{") + 1
        end_index = current_author.index("}")
        current_author = current_author[start_index:end_index]
        author.append(current_author)
    
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
        
    if line.startswith('url'):
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

data = {'Author': author, 'Title': title, 'Year': year, 'Journal': journal, "Source": url}

df_authors = pd.DataFrame(data)  #since author data is not available, the authors column will be blank incase you want to combine


excel_path = '<path for output, .xlsx format>'  #change the output location
writer = pd.ExcelWriter(excel_path)

df_authors.to_excel(writer, sheet_name='Authors', index=False)

df_books = pd.DataFrame({'Book': title})
df_books.sort_values(by='Book', inplace=True)
df_books.to_excel(writer, sheet_name='Books', index=False)

df_year = pd.DataFrame({'Year': year})
df_year.sort_values(by='Year', inplace=True)
df_year.to_excel(writer, sheet_name='Year', index=False)

df_journal = pd.DataFrame({'Journal': journal})
df_journal.sort_values(by='Journal', inplace=True)
df_journal.to_excel(writer, sheet_name='Journal', index=False)

df_url = pd.DataFrame({'Source': url})
df_url.sort_values(by='Source', inplace=True)
df_url.to_excel(writer, sheet_name='Source', index=False)

# Save the Excel file
writer.save()
