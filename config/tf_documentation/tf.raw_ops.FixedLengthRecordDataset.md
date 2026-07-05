# tf.raw_ops.FixedLengthRecordDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDataset)

---

Creates a dataset that emits the records from one or more binary files.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FixedLengthRecordDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FixedLengthRecordDataset)

```
tf.raw_ops.FixedLengthRecordDataset(
    filenames,
    header_bytes,
    record_bytes,
    footer_bytes,
    buffer_size,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `filenames` | A `Tensor` of type `string`. A scalar or a vector containing the name(s) of the file(s) to be read. |
| `header_bytes` | A `Tensor` of type `int64`. A scalar representing the number of bytes to skip at the beginning of a file. |
| `record_bytes` | A `Tensor` of type `int64`. A scalar representing the number of bytes in each record. |
| `footer_bytes` | A `Tensor` of type `int64`. A scalar representing the number of bytes to skip at the end of a file. |
| `buffer_size` | A `Tensor` of type `int64`. A scalar representing the number of bytes to buffer. Must be > 0. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |