# tf.signal.irfft3d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/irfft3d](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft3d)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L174-L196) |

Inverse 3D real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.irfft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft3d), [`tf.compat.v1.spectral.irfft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/irfft3d)

```
tf.signal.irfft3d(
    input_tensor, fft_length=None, name=None
)
```

Computes the inverse 3-dimensional discrete Fourier transform of a real-valued
signal over the inner-most 3 dimensions of `input_tensor`.

The inner-most 3 dimensions of `input_tensor` are assumed to be the result of `RFFT3D`:
The inner-most dimension contains the `fft_length / 2 + 1` unique components of
the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
from the size of the inner-most 3 dimensions of `input_tensor`. If the FFT length used
to compute `input_tensor` is odd, it should be provided since it cannot be inferred
properly.

Along each axis `IRFFT3D` is computed on, if `fft_length` (or
`fft_length / 2 + 1` for the inner-most dimension) is smaller than the
corresponding dimension of `input_tensor`, the dimension is cropped. If it is larger,
the dimension is padded with zeros.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape [3]. The FFT length for each dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Treal`. | |