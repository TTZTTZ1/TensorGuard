# tf.raw_ops.SparseMatrixZeros

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixZeros](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixZeros)

---

Creates an all-zeros CSRSparseMatrix with shape `dense_shape`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseMatrixZeros`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixZeros)

```
tf.raw_ops.SparseMatrixZeros(
    dense_shape, type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dense_shape` | A `Tensor` of type `int64`. The desired matrix shape. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.complex64, tf.complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |