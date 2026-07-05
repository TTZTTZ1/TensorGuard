# tf.raw_ops.InitializeTable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InitializeTable](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InitializeTable)

---

Table initializer that takes two tensors for keys and values respectively.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.InitializeTable`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InitializeTable)

```
tf.raw_ops.InitializeTable(
    table_handle, keys, values, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `table_handle` | A `Tensor` of type mutable `string`. Handle to a table which will be initialized. |
| `keys` | A `Tensor`. Keys of type Tkey. |
| `values` | A `Tensor`. Values of type Tval. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |