# tf.raw_ops.ReaderSerializeStateV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderSerializeStateV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderSerializeStateV2)

---

Produce a string tensor that encodes the state of a Reader.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReaderSerializeStateV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReaderSerializeStateV2)

```
tf.raw_ops.ReaderSerializeStateV2(
    reader_handle, name=None
)
```

Not all Readers support being serialized, so this can produce an
Unimplemented error.

| Args | |

|  |  |
| --- | --- |
| `reader_handle` | A `Tensor` of type `resource`. Handle to a Reader. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |