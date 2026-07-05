# tf.raw_ops.LookupTableExportV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableExportV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableExportV2)

---

Outputs all keys and values in the table.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LookupTableExportV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableExportV2)

```
tf.raw_ops.LookupTableExportV2(
    table_handle, Tkeys, Tvalues, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `table_handle` | A `Tensor` of type `resource`. Handle to the table. |
| `Tkeys` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `Tvalues` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (keys, values). | |
| `keys` | A `Tensor` of type `Tkeys`. |
| `values` | A `Tensor` of type `Tvalues`. |