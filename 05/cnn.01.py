from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

mnist = input_data.read_data_sets("mnist/", one_hot=True)

pixels = 28 * 28
numbers = 10

x = tf.placeholder(tf.float32, shape=(None, pixels), name="x")
y_ = tf.placeholder(tf.float32, shape=(None, numbers), name="y_")


def weight_variable(name, shape):

    weight_initialization = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(weight_initialization, name="weight_" + name)


def bias_variable(name, size):

    bias_initialization = tf.constant(0.1, shape=[size])
    return tf.Variable(bias_initialization, name="bias_" + name)


def convolution_layer(x, weight):

    strides = [1, 1, 1, 1]
    return tf.nn.conv2d(x, weight, strides=strides, padding="SAME")


def max_pooling_layer(x):

    size = [1, 2, 2, 1]
    strides = [1, 2, 2, 1]

    return tf.nn.max_pool(x, ksize=size, strides=strides, padding="SAME")


with tf.name_scope("layers") as scope:

    with tf.name_scope("hidden_layers") as scope:

        with tf.name_scope("conv_1") as scope:

            images = tf.reshape(x, [-1, 28, 28, 1])

            weight_1 = weight_variable("conv_1", [5, 5, 1, 32])
            bias_1 = bias_variable("conv_1", 32)
            conv_1 = tf.nn.relu(convolution_layer(images, weight_1) + bias_1)

        with tf.name_scope("pool_1") as scope:

            pool_1 = max_pooling_layer(conv_1)

        with tf.name_scope("conv_2") as scope:

            weight_2 = weight_variable("conv_2", [5, 5, 32, 64])
            bias_2 = bias_variable("conv_2", 64)
            conv_2 = tf.nn.relu(convolution_layer(pool_1, weight_2) + bias_2)

        with tf.name_scope("pool_2") as scope:

            pool_2 = max_pooling_layer(conv_2)

    with tf.name_scope("fully_connected") as scope:

        size = 7 * 7 * 64

        images_fc = tf.reshape(pool_2, [-1, size])

        weight_fc = weight_variable("fc", [size, 1024])
        bias_fc = bias_variable("fc", 1024)
        pool_fc = tf.nn.relu(tf.matmul(images_fc, weight_fc) + bias_fc)

    with tf.name_scope("dropout") as scope:

        keep_probability = tf.placeholder(tf.float32)
        pool_dropout = tf.nn.dropout(pool_fc, keep_probability)

    with tf.name_scope("readout") as scope:

        weight_final = weight_variable("final", [1024, 10])
        bias_final = bias_variable("final", 10)

        images_final = tf.matmul(pool_dropout, weight_final) + bias_final
        conv_final = tf.nn.softmax(images_final)

    with tf.name_scope("loss") as scope:
        cross_entropy = -tf.reduce_sum(y_ * tf.log(conv_final))


with tf.name_scope("training") as scope:
    optimzer = tf.train.AdamOptimizer(1e-4)
    train_step = optimzer.minimize(cross_entropy)

with tf.name_scope("predict") as scope:

    predict_operation = tf.equal(tf.argmax(conv_final, 1), tf.argmax(y_, 1))
    accuracy_operation = tf.reduce_mean(tf.cast(predict_operation, tf.float32))


def get_feed_dict(images, labels, probability):
    return {x: images, y_: labels, keep_probability: probability}


with tf.Session() as sess:

    sess.run(tf.global_variables_initializer())
    tf.summary.FileWriter("log_dir/4", graph=sess.graph)

    test_feed = get_feed_dict(mnist.test.images, mnist.test.labels, 1)

    for step in range(10000):

        batch = mnist.train.next_batch(50)

        train_feed = get_feed_dict(batch[0], batch[1], 0.5)
        _, loss = sess.run([train_step, cross_entropy], feed_dict=train_feed)

        if step % 500 is 0:

            accuracy = sess.run(accuracy_operation, feed_dict=test_feed)
            print("step = ", step, "loss = ", loss, "accuracy = ", accuracy)

    accuracy_final = sess.run(accuracy_operation, feed_dict=test_feed)
    print("accuracy => ", accuracy_final)
