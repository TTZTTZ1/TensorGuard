# tf.experimental.numpy.moveaxis

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/moveaxis](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/moveaxis)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_array_ops.py#L953-L1015) |

TensorFlow variant of NumPy's `moveaxis`.

```
tf.experimental.numpy.moveaxis(
    a, source, destination
)
```

Raises ValueError if source, destination not in (-ndim(a), ndim(a)).

See the NumPy documentation for [`numpy.moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html).