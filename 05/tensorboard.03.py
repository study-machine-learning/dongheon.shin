import tensorflow as tf

import pandas
import numpy
import random

data = pandas.read_csv("bmi.csv")

# normalize data
data["height"] = data["height"] / 100
data["weight"] = data["weight"] / 200

labels = {"thin": [1, 0, 0], "normal": [0, 1, 0], "fat": [0, 0, 1]}
data["label_pattern"] = data["label"].apply(lambda x: numpy.array(labels[x]))

# make placeholders
x = tf.placeholder(tf.float32, [None, 2], name="x")
y_ = tf.placeholder(tf.float32, [None, 3], name="y_")

with tf.name_scope("interface") as scope:

    # declare variables : weight, bias
    weight = tf.Variable(tf.zeros([2, 3]), name="weight")
    bias = tf.Variable(tf.zeros([3]), name="bias")

    # declare softmax operation : take a result as an exponent with parameters
    with tf.name_scope("softmax") as scope:
        softmax = tf.nn.softmax(tf.matmul(x, weight) + bias)

# declare cross entropy operation
with tf.name_scope("loss") as scope:
    cross_entropy_operation = -tf.reduce_sum(y_ * tf.log(softmax))

# train with optimizer under cross entropy
with tf.name_scope("train") as scope:
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train_operation = optimizer.minimize(cross_entropy_operation)

# calculate accuracy
with tf.name_scope("accuracy") as scope:
    predict_operation = tf.equal(tf.argmax(softmax, 1), tf.argmax(y_, 1))
    accuracy_operation = tf.reduce_mean(tf.cast(predict_operation, tf.float32))


# subtract test dataset from origin
test = data[15000:20000]

test_data = test[["weight", "height"]]
test_labels = list(test["label_pattern"])
test_dict = {x: test_data, y_: test_labels}


# start a session with a variable initialization
sess = tf.Session()
sess.run(tf.global_variables_initializer())

tf.summary.FileWriter("log_dir/3", graph=sess.graph)

# learn from data
for step in range(10000):

    i = random.randint(0, 199)
    rows = data[i * 100:(i + 1) * 100 - 1]

    step_data = rows[["weight", "height"]]
    step_labels = list(rows["label_pattern"])
    step_dict = {x: step_data, y_: step_labels}

    sess.run(train_operation, feed_dict=step_dict)

    # check accuracy at an interval of 500 steps
    if step % 500 is 0:

        step_entropy = sess.run(cross_entropy_operation, feed_dict=step_dict)
        step_accuracy = sess.run(accuracy_operation, feed_dict=test_dict)

        print(step, "=> entropy =", step_entropy, "accuracy =", step_accuracy)

# calculate final accuracy
accuracy = sess.run(accuracy_operation, feed_dict=test_dict)
print("accuracy =", accuracy)
