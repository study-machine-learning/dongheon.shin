from sklearn import svm, metrics
from sklearn.model_selection import train_test_split as split

import pandas

table = pandas.read_csv("bmi.csv")

weight = table["weight"] / 100
height = table["height"] / 200
label = table["label"]

multi = pandas.concat([weight, height], axis=1)

train_data, test_data, train_label, test_label = split(multi, label)

classifier = svm.SVC()
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)

score = metrics.accuracy_score(test_label, predict)
report = metrics.classification_report(test_label, predict)

print("score = ", score)
print("report")
print(report)
