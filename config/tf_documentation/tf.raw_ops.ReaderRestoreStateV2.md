# tf.raw_ops.ReaderRestoreStateV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderRestoreStateV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderRestoreStateV2)

---

Restore a reader to a previously saved state.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReaderRestoreStateV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderRestoreStateV2)

```
tf.raw_ops.ReaderRestoreStateV2(
    reader_handle, state, name=None
)
```

Not all Readers support being restored, so this can produce an
Unimplemented error.

| Args | |

|  |  |
| --- | --- |
| `reader_handle` | A `Tensor` of type `resource`. Handle to a Reader. |
| `state` | A `Tensor` of type `string`. Result of a ReaderSerializeState of a Reader with type matching reader\_handle. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |