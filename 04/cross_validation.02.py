from sklearn import svm, model_selection

import pandas

csv = pandas.read_csv("iris.csv")

data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
labels = csv["Name"]

classifier = svm.SVC()
scores = model_selection.cross_val_score(classifier, data, labels, cv=5)

print("score = ", scores)
print("avg = ", scores.mean())
