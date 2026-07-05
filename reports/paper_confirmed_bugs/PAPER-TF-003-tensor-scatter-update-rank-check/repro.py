import tensorflow as tf

tf.raw_ops.TensorScatterUpdate(
    tensor=tf.zeros([8], tf.int32),
    indices=tf.constant([[[4]]]),
    updates=tf.constant([3]),
)
