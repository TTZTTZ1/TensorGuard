# tf.experimental.numpy.experimental_enable_numpy_behavior

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numpy_ops/np_config.py#L25-L58) |

Enable NumPy behavior on Tensors.

```
tf.experimental.numpy.experimental_enable_numpy_behavior(
    prefer_float32=False, dtype_conversion_mode='legacy'
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [TF-NumPy Type Promotion](https://tensorflow.google.cn/guide/tf_numpy_type_promotion) * [NumPy API on TensorFlow](https://tensorflow.google.cn/guide/tf_numpy) |

Enabling NumPy behavior has three effects:

* It adds to [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) some common NumPy methods such as `T`,
  `reshape` and `ravel`.
* It changes dtype promotion in [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) operators to be
  compatible with NumPy. For example,
  `tf.ones([], tf.int32) + tf.ones([], tf.float32)` used to throw a
  "dtype incompatible" error, but after this it will return a
  float64 tensor (obeying NumPy's promotion rules).
* It enhances [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)'s indexing capability to be on par with
  [NumPy's](https://numpy.org/doc/stable/reference/arrays.indexing.html).

| Args | |

|  |  |
| --- | --- |
| `prefer_float32` | Controls whether dtype inference will use float32 for Python floats, or float64 (the default and the NumPy-compatible behavior). |
| `dtype_conversion_mode` | a string that specifies promotion mode. This string corresponds to a PromoMode Enum and can be 'off', 'legacy', 'safe', or 'all'. 'safe' or 'all' mode enables the auto dtype conversion semantics. |