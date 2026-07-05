# tf.raw_ops.FFT

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FFT](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FFT)

---

Fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FFT`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FFT)

```
tf.raw_ops.FFT(
    input, name=None
)
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