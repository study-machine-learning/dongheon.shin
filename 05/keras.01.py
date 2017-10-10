from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils

pixels = 28 * 28

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape(60000, pixels).astype("float32") / 255
train_labels = np_utils.to_categorical(train_labels, 10)

test_images = test_images.reshape(10000, pixels).astype("float") / 255
test_labels = np_utils.to_categorical(test_labels, 10)


model = Sequential()

model.add(Dense(512, input_shape=(784, )))
model.add(Activation("relu"))
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation("relu"))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation("softmax"))


loss = "categorical_crossentropy"
optimizer = Adam()
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


history = model.fit(train_images, train_labels)
score = model.evaluate(test_images, test_labels, verbose=1)

print("loss = ", score[0])
print("accuracy = ", score[1])
