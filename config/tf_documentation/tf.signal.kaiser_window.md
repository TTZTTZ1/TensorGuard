# tf.signal.kaiser_window

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_window](https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_window)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/window_ops.py#L53-L89) |

Generate a [Kaiser window](https://docs.scipy.org/doc/numpy/reference/generated/numpy.kaiser.html).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.kaiser_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_window)

```
tf.signal.kaiser_window(
    window_length,
    beta=12.0,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `window_length` | A scalar `Tensor` indicating the window length to generate. |
| `beta` | Beta parameter for Kaiser window, see reference below. |
| `dtype` | The data type to produce. Must be a floating point type. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor` of shape `[window_length]` of type `dtype`. | |