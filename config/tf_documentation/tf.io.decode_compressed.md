# tf.io.decode_compressed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/decode_compressed](https://tensorflow.google.cn/api_docs/python/tf/io/decode_compressed)

---

Decompress strings.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.decode_compressed`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_compressed), [`tf.compat.v1.io.decode_compressed`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_compressed)

```
tf.io.decode_compressed(
    bytes: Annotated[Any, _atypes.String],
    compression_type: str = '',
    name=None
) -> Annotated[Any, _atypes.String]
```

This op decompresses each element of the `bytes` input `Tensor`, which
is assumed to be compressed using the given `compression_type`.

The `output` is a string `Tensor` of the same shape as `bytes`,
each element containing the decompressed data from the corresponding
element in `bytes`.

| Args | |

|  |  |
| --- | --- |
| `bytes` | A `Tensor` of type `string`. A Tensor of string which is compressed. |
| `compression_type` | An optional `string`. Defaults to `""`. A scalar containing either (i) the empty string (no compression), (ii) "ZLIB", or (iii) "GZIP". |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |