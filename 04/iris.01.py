from sklearn import svm, metrics

import random
import re


def convert(v):
    if re.match(r"^[0-9\.]+$", v):
        return float(v)
    else:
        return v


csv = []

with open("iris.csv", "r", encoding="utf-8") as fp:

    for line in fp:

        line = line.strip()
        columns = list(map(convert, line.split(",")))

        csv.append(columns)


del csv[0]
random.shuffle(csv)

total_length = len(csv)

train_length = int(total_length * 2 / 3)
train_data = []
train_label = []

test_data = []
test_label = []


for i in range(total_length):

    data = csv[i][0:4]
    label = csv[i][4]

    if i < train_length:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)


classifier = svm.SVC()
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)
score = metrics.accuracy_score(test_label, predict)

print("score = ", score)
