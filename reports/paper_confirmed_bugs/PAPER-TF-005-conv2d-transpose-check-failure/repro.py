import tensorflow as tf

output_image = tf.random.normal([1, 3, 3, 8])
tf.nn.conv2d_transpose(
    output_image,
    8,
    (2, 2),
    strides=(2, 2),
    padding="SAME",
)
