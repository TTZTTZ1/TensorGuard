# tf.raw_ops.SerializeSparse

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeSparse](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeSparse)

---

Serialize a `SparseTensor` into a `[3]` `Tensor` object.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SerializeSparse`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeSparse)

```
tf.raw_ops.SerializeSparse(
    sparse_indices,
    sparse_values,
    sparse_shape,
    out_type=tf.dtypes.string,
    name=None
)

tf.dtypes.string
```

| Args | |

|  |  |
| --- | --- |
| `sparse_indices` | A `Tensor` of type `int64`. 2-D. The `indices` of the `SparseTensor`. |
| `sparse_values` | A `Tensor`. 1-D. The `values` of the `SparseTensor`. |
| `sparse_shape` | A `Tensor` of type `int64`. 1-D. The `shape` of the `SparseTensor`. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.string, tf.variant`. Defaults to [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string). The `dtype` to use for serialization; the supported types are `string` (default) and `variant`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |