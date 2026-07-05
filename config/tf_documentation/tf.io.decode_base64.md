# tf.io.decode_base64

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/decode_base64](https://tensorflow.google.cn/api_docs/python/tf/io/decode_base64)

---

Decode web-safe base64-encoded strings.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.decode_base64`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_base64), [`tf.compat.v1.io.decode_base64`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_base64)

```
tf.io.decode_base64(
    input: Annotated[Any, _atypes.String], name=None
) -> Annotated[Any, _atypes.String]
```

Input may or may not have padding at the end. See
[EncodeBase64](https://tensorflow.google.cn/api_docs/python/tf/io/encode_base64)
for padding. Web-safe means that input must use - and \_ instead of + and /.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. Base64 strings to decode. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |