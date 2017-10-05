from sklearn import svm, metrics
from sklearn.model_selection import train_test_split as split

import pandas

filename = "iris.csv"
csv = pandas.read_csv(filename)

data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
labels = csv["Name"]

train_data, test_data, train_label, test_label = split(data, labels)

classifier = svm.SVC()
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)
score = metrics.accuracy_score(test_label, predict)

print("score = ", score)
