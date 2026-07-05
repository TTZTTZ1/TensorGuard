# tf.signal.irfft

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/irfft](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L174-L196) |

Inverse real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.irfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft), [`tf.compat.v1.spectral.irfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft)

```
tf.signal.irfft(
    input_tensor, fft_length=None, name=None
)
```

Computes the inverse 1-dimensional discrete Fourier transform of a real-valued
signal over the inner-most dimension of `input_tensor`.

The inner-most dimension of `input_tensor` is assumed to be the result of `RFFT`: the
`fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If
`fft_length` is not provided, it is computed from the size of the inner-most
dimension of `input_tensor` (`fft_length = 2 * (inner - 1)`). If the FFT length used to
compute `input_tensor` is odd, it should be provided since it cannot be inferred
properly.

Along the axis `IRFFT` is computed on, if `fft_length / 2 + 1` is smaller
than the corresponding dimension of `input_tensor`, the dimension is cropped. If it is
larger, the dimension is padded with zeros.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape [1]. The FFT length. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Treal`. | |