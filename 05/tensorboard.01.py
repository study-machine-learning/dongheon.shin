import tensorflow as tf

a = tf.constant(20, name="a")
b = tf.constant(30, name="b")

multiply_operation = a * b

sess = tf.Session()
tf.summary.FileWriter("log_dir/1", graph=sess.graph)

result = sess.run(multiply_operation)
print(result)
