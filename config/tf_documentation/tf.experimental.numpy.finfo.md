# tf.experimental.numpy.finfo

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/finfo](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/finfo)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_utils.py#L486-L493) |

TensorFlow variant of NumPy's `finfo`.

```
tf.experimental.numpy.finfo(
    dtype
)
```

Note that currently it just forwards to the numpy namesake, while

tensorflow and numpy dtypes may have different properties.

See the NumPy documentation for [`numpy.finfo`](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html).