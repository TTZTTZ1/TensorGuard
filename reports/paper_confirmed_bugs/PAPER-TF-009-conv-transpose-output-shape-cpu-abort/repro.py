import tensorflow as tf

x = tf.random.normal([1, 4, 4, 3])
f = tf.random.normal([3, 3, 3, 3])
tf.nn.conv2d_transpose(
    x,
    f,
    output_shape=(2, 4, 2),
    strides=[1, 2, 2, 1],
    padding="SAME",
)
