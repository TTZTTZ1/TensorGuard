# tf.raw_ops.DecodeBase64

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeBase64](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeBase64)

---

Decode web-safe base64-encoded strings.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DecodeBase64`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeBase64)

```
tf.raw_ops.DecodeBase64(
    input, name=None
)
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