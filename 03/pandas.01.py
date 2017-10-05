import pandas

filename = "data.xlsx"
sheet = "stats_104102"

book = pandas.read_excel(filename, sheetname=sheet, header=1)

book = book.sort_values(by=2015, ascending=False)
print(book)
