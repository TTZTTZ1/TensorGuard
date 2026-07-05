# tf.signal.kaiser_bessel_derived_window

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_bessel_derived_window](https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_bessel_derived_window)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/window_ops.py#L92-L117) |

Generate a [Kaiser Bessel derived window](https://en.wikipedia.org/wiki/Kaiser_window#Kaiser%E2%80%93Bessel-derived_(KBD)_window).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.kaiser_bessel_derived_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_bessel_derived_window)

```
tf.signal.kaiser_bessel_derived_window(
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
| `beta` | Beta parameter for Kaiser window. |
| `dtype` | The data type to produce. Must be a floating point type. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor` of shape `[window_length]` of type `dtype`. | |