# tf.raw_ops.ReaderNumWorkUnitsCompleted

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompleted](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompleted)

---

Returns the number of work units this Reader has finished processing.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReaderNumWorkUnitsCompleted`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompleted)

```
tf.raw_ops.ReaderNumWorkUnitsCompleted(
    reader_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `reader_handle` | A `Tensor` of type mutable `string`. Handle to a Reader. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |