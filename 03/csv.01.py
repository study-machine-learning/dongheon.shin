import codecs

filename = "data.csv"
csv = codecs.open(filename, "r", "utf-8").read()

data = []
rows = csv.split("\n")

for row in rows:

    if row == "":
        continue

    cells = row.split(",")
    data.append(cells)

for cell in data:

    print(cell[1], cell[2])
