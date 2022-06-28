import camelot

tables = camelot.read_pdf('file.pdf', pages='1')
print(tables)

tables.export('file.csv', f='csv', compress=True)
tables[0].to_csv('file.csv')