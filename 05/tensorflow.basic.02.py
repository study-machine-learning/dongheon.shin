import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

operation_a = a + b + c
operation_b = (a + b) * c

session = tf.Session()

print(session.run(operation_a))
print(session.run(operation_b))
