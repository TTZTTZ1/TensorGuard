# tf.raw_ops.LookupTableRemoveV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableRemoveV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableRemoveV2)

---

Removes keys and its associated values from a table.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LookupTableRemoveV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LookupTableRemoveV2)

```
tf.raw_ops.LookupTableRemoveV2(
    table_handle, keys, name=None
)
```

The tensor `keys` must of the same type as the keys of the table. Keys not
already in the table are silently ignored.

| Args | |

|  |  |
| --- | --- |
| `table_handle` | A `Tensor` of type `resource`. Handle to the table. |
| `keys` | A `Tensor`. Any shape. Keys of the elements to remove. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |