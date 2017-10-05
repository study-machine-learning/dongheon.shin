import csv
import codecs

filename = "output.csv"

with codecs.open(filename, "w", "utf-8") as fp:

    writer = csv.writer(fp, delimiter=",", quotechar='"')

    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "비누", "300"])
    writer.writerow(["1001", "장갑", "150"])
    writer.writerow(["1002", "마스크", "230"])
