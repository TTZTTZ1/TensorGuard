# tf.raw_ops.LookupTableSizeV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSizeV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSizeV2)

---

Computes the number of elements in the given table.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LookupTableSizeV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableSizeV2)

```
tf.raw_ops.LookupTableSizeV2(
    table_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `table_handle` | A `Tensor` of type `resource`. Handle to the table. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |