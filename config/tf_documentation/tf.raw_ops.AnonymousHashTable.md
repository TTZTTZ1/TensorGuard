# tf.raw_ops.AnonymousHashTable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousHashTable](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousHashTable)

---

Creates a uninitialized anonymous hash table.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AnonymousHashTable`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousHashTable)

```
tf.raw_ops.AnonymousHashTable(
    key_dtype, value_dtype, name=None
)
```

This op creates a new anonymous hash table (as a resource) everytime
it is executed, with the specified dtype of its keys and values,
returning the resource handle. Before using the table you will have
to initialize it. After initialization the table will be
immutable. The table is anonymous in the sense that it can only be
accessed by the returned resource handle (e.g. it cannot be looked up
by a name in a resource manager). The table will be automatically
deleted when all resource handles pointing to it are gone.

| Args | |

|  |  |
| --- | --- |
| `key_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Type of the table keys. |
| `value_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Type of the table values. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |