from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as split

import pandas

mushroom = pandas.read_csv("mushroom.csv", header=None)

data = []
labels = []

for row_index, row in mushroom.iterrows():

    labels.append(row.ix[0])
    row_data = []

    for value in row.ix[1:]:
        row_data.append(ord(value))

    data.append(row_data)

train_data, test_data, train_label, test_label = split(data, labels)

classifier = RandomForestClassifier()
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)

score = metrics.accuracy_score(test_label, predict)
report = metrics.classification_report(test_label, predict)

print("score = ", score)
print("report")
print(report)
