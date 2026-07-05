# tf.experimental.numpy.pad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/pad](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/pad)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_array_ops.py#L1018-L1033) |

TensorFlow variant of NumPy's `pad`.

```
tf.experimental.numpy.pad(
    array, pad_width, mode, **kwargs
)
```

Only supports modes 'constant', 'reflect' and 'symmetric' currently.

See the NumPy documentation for [`numpy.pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html).