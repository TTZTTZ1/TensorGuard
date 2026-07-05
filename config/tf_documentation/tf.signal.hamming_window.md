# tf.signal.hamming_window

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/hamming_window](https://tensorflow.google.cn/api_docs/python/tf/signal/hamming_window)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/window_ops.py#L171-L196) |

Generate a [Hamming](https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows) window.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.hamming_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/hamming_window)

```
tf.signal.hamming_window(
    window_length,
    periodic=True,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `window_length` | A scalar `Tensor` indicating the window length to generate. |
| `periodic` | A bool `Tensor` indicating whether to generate a periodic or symmetric window. Periodic windows are typically used for spectral analysis while symmetric windows are typically used for digital filter design. |
| `dtype` | The data type to produce. Must be a floating point type. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor` of shape `[window_length]` of type `dtype`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `dtype` is not a floating point type. |