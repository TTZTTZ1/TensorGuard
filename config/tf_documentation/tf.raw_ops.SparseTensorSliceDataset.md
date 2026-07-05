# tf.raw_ops.SparseTensorSliceDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseTensorSliceDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseTensorSliceDataset)

---

Creates a dataset that splits a SparseTensor into elements row-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseTensorSliceDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseTensorSliceDataset)

```
tf.raw_ops.SparseTensorSliceDataset(
    indices, values, dense_shape, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `indices` | A `Tensor` of type `int64`. |
| `values` | A `Tensor`. |
| `dense_shape` | A `Tensor` of type `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |