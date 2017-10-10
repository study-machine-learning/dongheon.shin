import tensorflow as tf

a = tf.constant(1234)
b = tf.constant(5000)

add = a + b

session = tf.Session()

result = session.run(add)
print(result)
