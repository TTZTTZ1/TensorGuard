# tf.raw_ops.RaggedTensorToSparse

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedTensorToSparse](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedTensorToSparse)

---

Converts a `RaggedTensor` into a `SparseTensor` with the same values.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RaggedTensorToSparse`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedTensorToSparse)

```
tf.raw_ops.RaggedTensorToSparse(
    rt_nested_splits, rt_dense_values, name=None
)
```

input=ragged.from\_nested\_row\_splits(rt\_dense\_values, rt\_nested\_splits)
output=SparseTensor(indices=sparse\_indices, values=sparse\_values,
dense\_shape=sparse\_dense\_shape)

| Args | |

|  |  |
| --- | --- |
| `rt_nested_splits` | A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`. The `row_splits` for the `RaggedTensor`. |
| `rt_dense_values` | A `Tensor`. The `flat_values` for the `RaggedTensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (sparse\_indices, sparse\_values, sparse\_dense\_shape). | |
| `sparse_indices` | A `Tensor` of type `int64`. |
| `sparse_values` | A `Tensor`. Has the same type as `rt_dense_values`. |
| `sparse_dense_shape` | A `Tensor` of type `int64`. |