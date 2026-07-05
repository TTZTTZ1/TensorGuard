# tf.experimental.numpy.arange

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/arange](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/arange)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_array_ops.py#L259-L301) |

TensorFlow variant of NumPy's `arange`.

```
tf.experimental.numpy.arange(
    start, stop=None, step=1, dtype=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [NumPy API on TensorFlow](https://tensorflow.google.cn/guide/tf_numpy) |

Returns `step`-separated values in the range [start, stop).

Args:
start: Start of the interval. Included in the range.
stop: End of the interval. If not specified, `start` is treated as 0 and
`start` value is used as `stop`. If specified, it is not included in the
range if `step` is integer. When `step` is floating point, it may or may
not be included.
step: The difference between 2 consecutive values in the output range. It is
recommended to use `linspace` instead of using non-integer values for
`step`.
dtype: Optional. Type of the resulting ndarray. Could be a python type, a
NumPy type or a TensorFlow `DType`. If not provided, the largest type of
`start`, `stop`, `step` is used.

Raises:
ValueError: If step is zero.

See the NumPy documentation for [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html).