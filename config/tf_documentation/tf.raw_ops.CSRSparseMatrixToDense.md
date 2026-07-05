# tf.raw_ops.CSRSparseMatrixToDense

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToDense](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToDense)

---

Convert a (possibly batched) CSRSparseMatrix to dense.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CSRSparseMatrixToDense`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToDense)

```
tf.raw_ops.CSRSparseMatrixToDense(
    sparse_input, type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `sparse_input` | A `Tensor` of type `variant`. A batched CSRSparseMatrix. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.complex64, tf.complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `type`. | |