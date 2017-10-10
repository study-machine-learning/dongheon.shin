import tensorflow as tf

a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

calculate_operation = a + b * c
assign_operation = tf.assign(v, calculate_operation)

sess = tf.Session()
tf.summary.FileWriter("log_dir/2", graph=sess.graph)

result = sess.run(assign_operation)
print(result)
