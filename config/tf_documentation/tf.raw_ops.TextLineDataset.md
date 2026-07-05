# tf.raw_ops.TextLineDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TextLineDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TextLineDataset)

---

Creates a dataset that emits the lines of one or more text files.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TextLineDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TextLineDataset)

```
tf.raw_ops.TextLineDataset(
    filenames, compression_type, buffer_size, metadata='', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `filenames` | A `Tensor` of type `string`. A scalar or a vector containing the name(s) of the file(s) to be read. |
| `compression_type` | A `Tensor` of type `string`. A scalar containing either (i) the empty string (no compression), (ii) "ZLIB", or (iii) "GZIP". |
| `buffer_size` | A `Tensor` of type `int64`. A scalar containing the number of bytes to buffer. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |