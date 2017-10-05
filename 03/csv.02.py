import csv
import codecs

filename = "data.csv"
fp = codecs.open(filename, "r", "utf-8")

reader = csv.reader(fp, delimiter=",", quotechar='"')

for cells in reader:
    print(cells[1], cells[2])
