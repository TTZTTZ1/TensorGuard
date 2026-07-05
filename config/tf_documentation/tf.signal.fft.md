# tf.signal.fft

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/fft](https://tensorflow.google.cn/api_docs/python/tf/signal/fft)

---

Fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fft`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft), [`tf.compat.v1.signal.fft`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft), [`tf.compat.v1.spectral.fft`](https://tensorflow.google.cn/api_docs/python/tf/signal/fft)

```
tf.signal.fft(
    input: Annotated[Any, TV_FFT_Tcomplex], name=None
) -> Annotated[Any, TV_FFT_Tcomplex]
```

Computes the 1-dimensional discrete Fourier transform over the inner-most
dimension of `input`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |