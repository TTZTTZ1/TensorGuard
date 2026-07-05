import numpy as np
import tensorflow as tf

input_tensor = np.array([[[1], [2]], [[3], [4]]])
output_tensor = tf.signal.irfft(input_tensor)
print(output_tensor)
