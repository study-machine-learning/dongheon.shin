import tensorflow as tf

a = tf.placeholder(tf.int32, [None])
b = tf.constant(10)

multiply_operation = a * b

sess = tf.Session()

result = sess.run(multiply_operation, feed_dict={a: [1, 2, 3, 4, 5]})
print(result)

result = sess.run(multiply_operation, feed_dict={a: [10, 20]})
print(result)
