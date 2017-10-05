from sklearn import svm, metrics

import random
import re


def split(rows):

    data = []
    labels = []

    for row in rows:

        data.append(row[0:4])
        labels.append(row[4])

    return (data, labels)


def calculate_score(train, test):

    train_data, train_label = split(train)
    test_data, test_label = split(test)

    classifier = svm.SVC()
    classifier.fit(train_data, train_label)

    predict = classifier.predict(test_data)
    return metrics.accuracy_score(test_label, predict)


def to_number(n):
    return float(n) if re.match(r"^[0-9\.]+$", n) else n


def to_columm(line):
    return list(map(to_number, line.strip().split(",")))


lines = open("iris.csv", "r", encoding="utf-8").read().split("\n")

csv = list(map(to_columm, lines))
del csv[0]

random.shuffle(csv)

k = 5

csv_k = [[] for i in range(k)]
scores = []

for i in range(len(csv)):
    csv_k[i % k].append(csv[i])

for test in csv_k:

    train = []

    for data in csv_k:

        if test != data:
            train += data

    score = calculate_score(train, test)
    scores.append(score)

print("score = ", scores)
print("avg = ", sum(scores) / len(scores))
