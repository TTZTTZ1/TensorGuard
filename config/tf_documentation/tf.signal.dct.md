# tf.signal.dct

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/dct](https://tensorflow.google.cn/api_docs/python/tf/signal/dct)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/dct_ops.py#L50-L97) |

Computes the 1D [Discrete Cosine Transform (DCT)](https://en.wikipedia.org/wiki/Discrete_cosine_transform) of `input`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.dct`](https://tensorflow.google.cn/api_docs/python/tf/signal/dct), [`tf.compat.v1.spectral.dct`](https://tensorflow.google.cn/api_docs/python/tf/signal/dct)

```
tf.signal.dct(
    input, type=2, n=None, axis=-1, norm=None, name=None
)
```

Types I, II, III and IV are supported.
Type I is implemented using a length `2N` padded [`tf.signal.rfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft).
Type II is implemented using a length `2N` padded [`tf.signal.rfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft), as
described here: [Type 2 DCT using 2N FFT padded (Makhoul)](https://dsp.stackexchange.com/a/10606).
Type III is a fairly straightforward inverse of Type II
(i.e. using a length `2N` padded [`tf.signal.irfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft)).
Type IV is calculated through 2N length DCT2 of padded signal and
picking the odd indices.

| Args | |

|  |  |
| --- | --- |
| `input` | A `[..., samples]` `float32`/`float64` `Tensor` containing the signals to take the DCT of. |
| `type` | The DCT type to perform. Must be 1, 2, 3 or 4. |
| `n` | The length of the transform. If length is less than sequence length, only the first n elements of the sequence are considered for the DCT. If n is greater than the sequence length, zeros are padded and then the DCT is computed as usual. |
| `axis` | For future expansion. The axis to compute the DCT along. Must be `-1`. |
| `norm` | The normalization to apply. `None` for no normalization or `'ortho'` for orthonormal normalization. |
| `name` | An optional name for the operation. |

| Returns | |
| A `[..., samples]` `float32`/`float64` `Tensor` containing the DCT of `input`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `type` is not `1`, `2`, `3` or `4`, `axis` is not `-1`, `n` is not `None` or greater than 0, or `norm` is not `None` or `'ortho'`. |
| `ValueError` | If `type` is `1` and `norm` is `ortho`. |

## scipy compatibility

Equivalent to [scipy.fftpack.dct](https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.dct.html)
for Type-I, Type-II, Type-III and Type-IV DCT.