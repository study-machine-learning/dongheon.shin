from sklearn import svm, metrics
from sklearn.grid_search import GridSearchCV
from urllib.parse import urljoin

import pandas

dirpath = "./mnist/handwriting/"

train_csv = pandas.read_csv(urljoin(dirpath, "train.csv"))
test_csv = pandas.read_csv(urljoin(dirpath, "t10k.csv"))

train_data = train_csv.ix[:, 1:577]
train_label = train_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:577]
test_label = test_csv.ix[:, 0]

params = [
    {"C": [1, 10, 100, 1000], "kernel": ["linear"]},
    {"C": [1, 10, 100, 1000], "kernel": ["rbf"], "gamma": [0.001, 0.0001]},
]

classifier = GridSearchCV(svm.SVC(), params, n_jobs=-1)
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)

score = metrics.accuracy_score(test_label, predict)
report = metrics.classification_report(test_label, predict)

print("score = ", score)
print("report")
print(report)
