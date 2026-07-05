# tf.signal.mdct

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/mdct](https://tensorflow.google.cn/api_docs/python/tf/signal/mdct)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/spectral_ops.py#L291-L364) |

Computes the [Modified Discrete Cosine Transform](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform) of `signals`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.mdct`](https://tensorflow.google.cn/api_docs/python/tf/signal/mdct)

```
tf.signal.mdct(
    signals,
    frame_length,
    window_fn=tf.signal.vorbis_window,
    pad_end=False,
    norm=None,
    name=None
)

tf.signal.vorbis_window
```

Implemented with TPU/GPU-compatible ops and supports gradients.

| Args | |

|  |  |
| --- | --- |
| `signals` | A `[..., samples]` `float32`/`float64` `Tensor` of real-valued signals. |
| `frame_length` | An integer scalar `Tensor`. The window length in samples which must be divisible by 4. |
| `window_fn` | A callable that takes a frame\_length and a `dtype` keyword argument and returns a `[frame_length]` `Tensor` of samples in the provided datatype. If set to `None`, a rectangular window with a scale of 1/sqrt(2) is used. For perfect reconstruction of a signal from `mdct` followed by `inverse_mdct`, please use [`tf.signal.vorbis_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/vorbis_window), [`tf.signal.kaiser_bessel_derived_window`](https://tensorflow.google.cn/api_docs/python/tf/signal/kaiser_bessel_derived_window) or `None`. If using another window function, make sure that w[n]^2 + w[n + frame\_length // 2]^2 = 1 and w[n] = w[frame\_length - n - 1] for n = 0,...,frame\_length // 2 - 1 to achieve perfect reconstruction. |
| `pad_end` | Whether to pad the end of `signals` with zeros when the provided frame length and step produces a frame that lies partially past its end. |
| `norm` | If it is None, unnormalized dct4 is used, if it is "ortho" orthonormal dct4 is used. |
| `name` | An optional name for the operation. |

| Returns | |
| A `[..., frames, frame_length // 2]` `Tensor` of `float32`/`float64` MDCT values where `frames` is roughly `samples // (frame_length // 2)` when `pad_end=False`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `signals` is not at least rank 1, `frame_length` is not scalar, or `frame_length` is not a multiple of `4`. |