# tf.signal.ifft2d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/ifft2d](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft2d)

---

Inverse 2D fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ifft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft2d), [`tf.compat.v1.signal.ifft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft2d), [`tf.compat.v1.spectral.ifft2d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft2d)

```
tf.signal.ifft2d(
    input: Annotated[Any, TV_IFFT2D_Tcomplex], name=None
) -> Annotated[Any, TV_IFFT2D_Tcomplex]
```

Computes the inverse 2-dimensional discrete Fourier transform over the
inner-most 2 dimensions of `input`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |