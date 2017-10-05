from sklearn import svm, metrics

import glob
import os.path
import re
import json


def check_frequency(filename):

    name = os.path.basename(filename)
    language = re.match(r"^[a-z]{2,}", name).group()

    with open(filename, "r", encoding="utf-8") as fp:
        text = fp.read().lower()

    # check only alphabets
    frequency = [0 for n in range(0, 26)]

    code_a = ord("a")
    code_z = ord("z")

    # count frequencies
    for ch in text:

        n = ord(ch)

        if code_a <= n <= code_z:
            frequency[n - code_a] += 1

    total = sum(frequency)

    # convert data to unit vectors and return with labels
    return (list(map(lambda n: n / total, frequency)), language)


def load_files(path):

    # read files with a given pattern
    frequencies = []
    labels = []

    filenames = glob.glob(path)

    # analyze frequencies and labels
    for filename in filenames:

        frequency, language = check_frequency(filename)

        frequencies.append(frequency)
        labels.append(language)

    return {"frequencies": frequencies, "labels": labels}


data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")

with open("./lang/frequencies.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)


classifier = svm.SVC()
classifier.fit(data["frequencies"], data["labels"])

predict = classifier.predict(test["frequencies"])

score = metrics.accuracy_score(test["labels"], predict)
report = metrics.classification_report(test["labels"], predict)

print("score = ", score)
print("report")
print(report)
