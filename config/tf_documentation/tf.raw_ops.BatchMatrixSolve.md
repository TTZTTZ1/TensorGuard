# tf.raw_ops.BatchMatrixSolve

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatrixSolve](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatrixSolve)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BatchMatrixSolve`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatrixSolve)

```
tf.raw_ops.BatchMatrixSolve(
    matrix, rhs, adjoint=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `matrix` | A `Tensor`. Must be one of the following types: `float64`, `float32`. |
| `rhs` | A `Tensor`. Must have the same type as `matrix`. |
| `adjoint` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `matrix`. | |