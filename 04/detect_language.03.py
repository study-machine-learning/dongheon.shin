from sklearn import svm
from sklearn.externals import joblib

import json

with open("./lang/frequencies.json", "r", encoding="utf-8") as fp:
    data = json.load(fp)[0]

classifier = svm.SVC()
classifier.fit(data["frequencies"], data["labels"])

joblib.dump(classifier, "./lang/frequencies.pkl")
