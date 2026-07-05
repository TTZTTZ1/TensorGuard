# tf.experimental.numpy.array

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/array](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/array)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_array_ops.py#L217-L228) |

TensorFlow variant of NumPy's `array`.

```
tf.experimental.numpy.array(
    val, dtype=None, copy=True, ndmin=0
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [TF-NumPy Type Promotion](https://tensorflow.google.cn/guide/tf_numpy_type_promotion) |

Since Tensors are immutable, a copy is made only if val is placed on a

different device than the current one. Even if `copy` is False, a new Tensor
may need to be built to satisfy `dtype` and `ndim`. This is used only if `val`
is an ndarray or a Tensor.

See the NumPy documentation for [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html).