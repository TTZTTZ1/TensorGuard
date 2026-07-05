import tensorflow as tf

tf.raw_ops.FusedPadConv2D(
    input=tf.zeros([3, 2], tf.float32),
    paddings=[[0, 0], [1, 1], [1, 1], [0, 0]],
    filter=tf.zeros([2, 2, 1, 1], tf.float32),
    mode="REFLECT",
    strides=[1, 1, 1, 1],
    padding="VALID",
)
