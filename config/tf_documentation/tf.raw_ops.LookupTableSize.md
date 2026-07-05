# tf.raw_ops.LookupTableSize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSize)

---

Computes the number of elements in the given table.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LookupTableSize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSize)

```
tf.raw_ops.LookupTableSize(
    table_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `table_handle` | A `Tensor` of type mutable `string`. Handle to the table. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |