import tensorflow as tf

a = tf.constant(100)
b = tf.constant(50)

add_operation = a + b

v = tf.Variable(0)

assign_operation = tf.assign(v, add_operation)

sess = tf.Session()

sess.run(tf.global_variables_initializer())
sess.run(assign_operation)

print(sess.run(v))
