from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping

import pandas
import numpy

csv = pandas.read_csv("bmi.csv")

csv["height"] /= 200
csv["weight"] /= 100

category = {"thin": [1, 0, 0], "normal": [0, 1, 0], "fat": [0, 0, 1]}

data = csv[["height", "weight"]].as_matrix()
labels = numpy.empty((20000, 3))

for index, label in enumerate(csv["label"]):
    labels[index] = category[label]

train_data, train_labels = data[1: 15001], labels[1: 15001]
test_data, test_labels = data[15001: 20001], labels[15001: 20001]

model = Sequential()

model.add(Dense(512, input_shape=(2, )))
model.add(Activation("relu"))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation("relu"))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation("softmax"))


loss = "categorical_crossentropy"
optimizer = "rmsprop"
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


history = model.fit(
    train_data, train_labels,
    batch_size=100, epochs=20, validation_split=0.1, verbose=1,
    callbacks=[EarlyStopping(monitor="val_loss", patience=2)])

score = model.evaluate(test_data, test_labels)

print("loss = ", score[0])
print("accuracy = ", score[1])
