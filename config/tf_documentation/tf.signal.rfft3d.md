# tf.signal.rfft3d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/rfft3d](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft3d)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L140-L166) |

3D real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.rfft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft3d), [`tf.compat.v1.spectral.rfft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft3d)

```
tf.signal.rfft3d(
    input_tensor, fft_length=None, name=None
)
```

Computes the 3-dimensional discrete Fourier transform of a real-valued signal
over the inner-most 3 dimensions of `input`.

Since the DFT of a real signal is Hermitian-symmetric, `RFFT3D` only returns the
`fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
of `output`: the zero-frequency term, followed by the `fft_length / 2`
positive-frequency terms.

Along each axis `RFFT3D` is computed on, if `fft_length` is smaller than the
corresponding dimension of `input`, the dimension is cropped. If it is larger,
the dimension is padded with zeros.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`. A float32 tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape [3]. The FFT length for each dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tcomplex`. | |