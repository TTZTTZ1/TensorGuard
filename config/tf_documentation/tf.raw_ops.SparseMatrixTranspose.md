# tf.raw_ops.SparseMatrixTranspose

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixTranspose](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixTranspose)

---

Transposes the inner (matrix) dimensions of a CSRSparseMatrix.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseMatrixTranspose`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixTranspose)

```
tf.raw_ops.SparseMatrixTranspose(
    input, type, conjugate=False, name=None
)
```

Transposes the inner (matrix) dimensions of a SparseMatrix and optionally
conjugates its values.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `variant`. A CSRSparseMatrix. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.complex64, tf.complex128`. |
| `conjugate` | An optional `bool`. Defaults to `False`. Indicates whether `input` should be conjugated. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |