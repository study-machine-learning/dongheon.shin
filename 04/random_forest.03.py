from sklearn import metrics
from sklearn.model_selection import train_test_split as split
from sklearn.ensemble import RandomForestClassifier

import pandas

mushroom = pandas.read_csv("mushroom.csv", header=None)

data = []
labels = []
attributes = []

for row_index, row in mushroom.iterrows():

    labels.append(row.ix[0])
    result = []

    for column, value in enumerate(row.ix[1:]):

        # add or get table for characteristics
        if row_index == 0:
            attribute = {"dictionary": {}, "count": 0}
            attributes.append(attribute)
        else:
            attribute = attributes[column]

        # initialize characteristics : support 12 features to the max
        characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # get index of the feature in the table
        # in defect of feature, add the feature into dictionary
        if value in attribute["dictionary"]:
            index = attribute["dictionary"][value]
        else:
            index = attribute["count"]
            attribute["dictionary"][value] = index
            attribute["count"] += 1

        # validate the feature
        characteristics[index] = 1
        result += characteristics

    data.append(result)

train_data, test_data, train_label, test_label = split(data, labels)

classifier = RandomForestClassifier()
classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)

score = metrics.accuracy_score(test_label, predict)
report = metrics.classification_report(test_label, predict)

print("score = ", score)
print("report")
print(report)
