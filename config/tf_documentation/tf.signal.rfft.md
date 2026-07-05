# tf.signal.rfft

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/rfft](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L140-L166) |

Real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.rfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft), [`tf.compat.v1.spectral.rfft`](https://tensorflow.google.cn/api_docs/python/tf/signal/rfft)

```
tf.signal.rfft(
    input_tensor, fft_length=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) |

Computes the 1-dimensional discrete Fourier transform of a real-valued signal
over the inner-most dimension of `input`.

Since the DFT of a real signal is Hermitian-symmetric, `RFFT` only returns the
`fft_length / 2 + 1` unique components of the FFT: the zero-frequency term,
followed by the `fft_length / 2` positive-frequency terms.

Along the axis `RFFT` is computed on, if `fft_length` is smaller than the
corresponding dimension of `input`, the dimension is cropped. If it is larger,
the dimension is padded with zeros.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`. A float32 tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape [1]. The FFT length. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tcomplex`. | |