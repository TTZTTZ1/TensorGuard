# tf.raw_ops.DenseToCSRSparseMatrix

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DenseToCSRSparseMatrix](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DenseToCSRSparseMatrix)

---

Converts a dense tensor to a (possibly batched) CSRSparseMatrix.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DenseToCSRSparseMatrix`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DenseToCSRSparseMatrix)

```
tf.raw_ops.DenseToCSRSparseMatrix(
    dense_input, indices, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dense_input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`. A Dense tensor. |
| `indices` | A `Tensor` of type `int64`. Indices of nonzero elements. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |