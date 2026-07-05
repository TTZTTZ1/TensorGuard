# tf.signal.ifft

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/ifft](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft)

---

Inverse fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ifft`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft), [`tf.compat.v1.signal.ifft`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft), [`tf.compat.v1.spectral.ifft`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft)

```
tf.signal.ifft(
    input: Annotated[Any, TV_IFFT_Tcomplex], name=None
) -> Annotated[Any, TV_IFFT_Tcomplex]
```

Computes the inverse 1-dimensional discrete Fourier transform over the
inner-most dimension of `input`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |