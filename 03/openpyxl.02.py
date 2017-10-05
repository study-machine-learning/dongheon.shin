import openpyxl

filename = "data.xlsx"

book = openpyxl.load_workbook(filename)
sheet = book.active

for i in range(0, 10):

    row = str(chr(i + 66))

    total = int(sheet[row + "3"].value)
    seoul = int(sheet[row + "4"].value)

    page = str(chr(i + 66)) + "21"

    sheet[page] = total - seoul

    cell = sheet[page]
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

filename = "output.xlsx"
book.save(filename)
