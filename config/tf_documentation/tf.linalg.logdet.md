# tf.linalg.logdet

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/logdet](https://tensorflow.google.cn/api_docs/python/tf/linalg/logdet)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L68-L99) |

Computes log of the determinant of a hermitian positive definite matrix.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.logdet`](https://tensorflow.google.cn/api_docs/python/tf/linalg/logdet)

```
tf.linalg.logdet(
    matrix, name=None
)
```

```
# Compute the determinant of a matrix while reducing the chance of over- or
underflow:
A = ... # shape 10 x 10
det = tf.exp(tf.linalg.logdet(A))  # scalar
```

| Args | |

|  |  |
| --- | --- |
| `matrix` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op`. Defaults to `logdet`. |

| Returns | |
| The natural log of the determinant of `matrix`. | |

## numpy compatibility

Equivalent to numpy.linalg.slogdet, although no sign is returned since only
hermitian positive definite matrices are supported.