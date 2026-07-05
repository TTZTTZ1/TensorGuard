# tf.experimental.numpy.random.randn

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/random/randn](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/random/randn)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_random.py#L53-L66) |

TensorFlow variant of NumPy's `random.randn`.

```
tf.experimental.numpy.random.randn(
    *args
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [NumPy API on TensorFlow](https://tensorflow.google.cn/guide/tf_numpy) |

Returns samples from a normal distribution.

Uses `tf.random_normal`.

Args:
\*args: The shape of the output array.

Returns:
An ndarray with shape `args` and dtype `float64`.

See the NumPy documentation for [`numpy.random.randn`](https://numpy.org/doc/stable/reference/generated/numpy.random.randn.html).