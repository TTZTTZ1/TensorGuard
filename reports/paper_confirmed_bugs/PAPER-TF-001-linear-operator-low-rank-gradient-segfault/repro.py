import tensorflow as tf

base = tf.linalg.LinearOperatorIdentity(num_rows=3)
u = tf.random.normal([3, 3])
g = tf.constant([4.0])

with tf.GradientTape() as tape:
    result = tf.linalg.LinearOperatorLowRankUpdate(base, u, u).matmul(base)

tape.watch(result)
tape.gradient(result, [u], [g])
