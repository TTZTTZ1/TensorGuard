# tf.experimental.numpy.meshgrid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/meshgrid](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/meshgrid)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_math_ops.py#L1514-L1538) |

TensorFlow variant of NumPy's `meshgrid`.

```
tf.experimental.numpy.meshgrid(
    *xi, **kwargs
)
```

Unsupported arguments: `copy`, `sparse`, `indexing`.

This currently requires copy=True and sparse=False.

See the NumPy documentation for [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html).