# tf.raw_ops.ReaderResetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderResetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderResetV2)

---

Restore a Reader to its initial clean state.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReaderResetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderResetV2)

```
tf.raw_ops.ReaderResetV2(
    reader_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `reader_handle` | A `Tensor` of type `resource`. Handle to a Reader. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |