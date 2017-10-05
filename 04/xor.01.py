from sklearn import svm

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

data = []
label = []

for row in xor_data:

    p = row[0]
    q = row[1]
    r = row[2]

    data.append([p, q])
    label.append(r)

# learn from data : SVC stands for Support Vector Classification
classifier = svm.SVC()
classifier.fit(data, label)

# do prediction
predict = classifier.predict(data)
print("result = ", predict)

ok = 0
total = 0

for idx, answer in enumerate(label):

    p = predict[idx]

    if p == answer:
        ok += 1

    total += 1

print("ok / total = ", ok / total)
