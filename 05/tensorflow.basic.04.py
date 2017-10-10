import tensorflow as tf

a = tf.placeholder(tf.int32, [3])
b = tf.constant(2)

multiply_operation = a * b

sess = tf.Session()

result = sess.run(multiply_operation, feed_dict={a: [1, 2, 3]})
print(result)

result = sess.run(multiply_operation, feed_dict={a: [10, 20, 30]})
print(result)
