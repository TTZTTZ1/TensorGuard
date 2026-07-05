import tensorflow as tf

value = tf.zeros([10], dtype=tf.float32)
filters = tf.zeros([5, 5, 1, 8], dtype=tf.float32)
tf.nn.atrous_conv2d(value, filters, rate=1, padding="VALID")
