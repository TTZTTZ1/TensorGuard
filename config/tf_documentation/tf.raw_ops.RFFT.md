# tf.raw_ops.RFFT

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RFFT](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RFFT)

---

Real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RFFT`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RFFT)

```
tf.raw_ops.RFFT(
    input,
    fft_length,
    Tcomplex=tf.dtypes.complex64,
    name=None
)

tf.dtypes.complex64
```

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
| `Tcomplex` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.complex64, tf.complex128`. Defaults to [`tf.complex64`](https://tensorflow.google.cn/api_docs/python/tf#complex64). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tcomplex`. | |