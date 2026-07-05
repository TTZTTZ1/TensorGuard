# tf.io.encode_base64

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/encode_base64](https://tensorflow.google.cn/api_docs/python/tf/io/encode_base64)

---

Encode strings into web-safe base64 format.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.encode_base64`](https://tensorflow.google.cn/api_docs/python/tf/io/encode_base64), [`tf.compat.v1.io.encode_base64`](https://tensorflow.google.cn/api_docs/python/tf/io/encode_base64)

```
tf.io.encode_base64(
    input: Annotated[Any, _atypes.String], pad: bool = False, name=None
) -> Annotated[Any, _atypes.String]
```

Refer to [this article](https://en.wikipedia.org/wiki/Base64) for more information on
base64 format. Base64 strings may have padding with '=' at the
end so that the encoded has length multiple of 4. See Padding section of the
link above.

Web-safe means that the encoder uses - and \_ instead of + and /.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. Strings to be encoded. |
| `pad` | An optional `bool`. Defaults to `False`. Bool whether padding is applied at the ends. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |