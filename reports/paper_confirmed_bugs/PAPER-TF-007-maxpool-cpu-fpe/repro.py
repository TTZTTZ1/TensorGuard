import tensorflow as tf

input_data = tf.constant(
    [[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]],
    dtype=tf.float32,
)
pool = tf.keras.layers.MaxPool1D(pool_size=3, strides=1, padding="valid")
y = pool(input_data)
print(y)
