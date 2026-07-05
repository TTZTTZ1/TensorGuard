# tf.signal.vorbis_window

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/vorbis_window](https://tensorflow.google.cn/api_docs/python/tf/signal/vorbis_window)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/window_ops.py#L120-L142) |

Generate a [Vorbis power complementary window](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform#Window_functions).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.vorbis_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/vorbis_window)

```
tf.signal.vorbis_window(
    window_length,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `window_length` | A scalar `Tensor` indicating the window length to generate. |
| `dtype` | The data type to produce. Must be a floating point type. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor` of shape `[window_length]` of type `dtype`. | |