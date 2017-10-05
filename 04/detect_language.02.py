import matplotlib.pyplot as pyplot
import pandas
import json


with open("./lang/frequencies.json", "r", encoding="utf-8") as fp:
    frequencies = json.load(fp)

data = frequencies[0]
test = frequencies[1]

languages = {}

for index, label in enumerate(data["labels"]):

    language = data["frequencies"][index]

    if label not in languages:
        languages[label] = language

    for index, value in enumerate(language):
        languages[label][index] += value

alphabets = [chr(n) for n in range(97, 97 + 26)]
frame = pandas.DataFrame(languages, index=alphabets)

pyplot.style.use('ggplot')

# frame.plot(kind="line")
frame.plot(kind="bar", subplots=True, ylim=(0, 1))

pyplot.savefig("language-plot.png")
