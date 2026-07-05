# tf.raw_ops.FixedLengthRecordDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDatasetV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FixedLengthRecordDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDatasetV2)

```
tf.raw_ops.FixedLengthRecordDatasetV2(
    filenames,
    header_bytes,
    record_bytes,
    footer_bytes,
    buffer_size,
    compression_type,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `filenames` | A `Tensor` of type `string`. |
| `header_bytes` | A `Tensor` of type `int64`. |
| `record_bytes` | A `Tensor` of type `int64`. |
| `footer_bytes` | A `Tensor` of type `int64`. |
| `buffer_size` | A `Tensor` of type `int64`. |
| `compression_type` | A `Tensor` of type `string`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |