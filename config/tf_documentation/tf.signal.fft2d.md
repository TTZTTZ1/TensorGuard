# tf.signal.fft2d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/fft2d](https://tensorflow.google.cn/api_docs/python/tf/signal/fft2d)

---

2D fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft2d), [`tf.compat.v1.signal.fft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft2d), [`tf.compat.v1.spectral.fft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft2d)

```
tf.signal.fft2d(
    input: Annotated[Any, TV_FFT2D_Tcomplex], name=None
) -> Annotated[Any, TV_FFT2D_Tcomplex]
```

Computes the 2-dimensional discrete Fourier transform over the inner-most
2 dimensions of `input`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |