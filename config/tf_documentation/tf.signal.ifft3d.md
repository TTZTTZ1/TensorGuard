# tf.signal.ifft3d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/ifft3d](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft3d)

---

Inverse 3D fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ifft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft3d), [`tf.compat.v1.signal.ifft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft3d), [`tf.compat.v1.spectral.ifft3d`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifft3d)

```
tf.signal.ifft3d(
    input: Annotated[Any, TV_IFFT3D_Tcomplex], name=None
) -> Annotated[Any, TV_IFFT3D_Tcomplex]
```

Computes the inverse 3-dimensional discrete Fourier transform over the
inner-most 3 dimensions of `input`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |