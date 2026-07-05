# tf.raw_ops.SparseMatrixSoftmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmax](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmax)

---

Calculates the softmax of a CSRSparseMatrix.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseMatrixSoftmax`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmax)

```
tf.raw_ops.SparseMatrixSoftmax(
    logits, type, name=None
)
```

Calculate the softmax of the innermost dimensions of a SparseMatrix.

Missing values are treated as `-inf` (i.e., logits of zero probability); and
the output has the same sparsity structure as the input (though missing values
in the output may now be treated as having probability zero).

| Args | |

|  |  |
| --- | --- |
| `logits` | A `Tensor` of type `variant`. A CSRSparseMatrix. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |