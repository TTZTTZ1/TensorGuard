# tf.raw_ops.CSRSparseMatrixToSparseTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToSparseTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToSparseTensor)

---

Converts a (possibly batched) CSRSparesMatrix to a SparseTensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CSRSparseMatrixToSparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CSRSparseMatrixToSparseTensor)

```
tf.raw_ops.CSRSparseMatrixToSparseTensor(
    sparse_matrix, type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `sparse_matrix` | A `Tensor` of type `variant`. A (possibly batched) CSRSparseMatrix. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.complex64, tf.complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (indices, values, dense\_shape). | |
| `indices` | A `Tensor` of type `int64`. |
| `values` | A `Tensor` of type `type`. |
| `dense_shape` | A `Tensor` of type `int64`. |