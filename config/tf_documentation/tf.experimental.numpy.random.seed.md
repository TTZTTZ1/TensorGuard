# tf.experimental.numpy.random.seed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/random/seed](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/random/seed)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_random.py#L33-L50) |

TensorFlow variant of NumPy's `random.seed`.

```
tf.experimental.numpy.random.seed(
    s
)
```

Sets the seed for the random number generator.

Uses `tf.set_random_seed`.

Args:
s: an integer.

See the NumPy documentation for [`numpy.random.seed`](https://numpy.org/doc/stable/reference/generated/numpy.random.seed.html).