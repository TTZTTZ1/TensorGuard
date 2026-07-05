# tf.raw_ops.ReaderNumWorkUnitsCompletedV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompletedV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompletedV2)

---

Returns the number of work units this Reader has finished processing.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReaderNumWorkUnitsCompletedV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderNumWorkUnitsCompletedV2)

```
tf.raw_ops.ReaderNumWorkUnitsCompletedV2(
    reader_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `reader_handle` | A `Tensor` of type `resource`. Handle to a Reader. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |