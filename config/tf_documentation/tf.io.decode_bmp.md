# tf.io.decode_bmp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/decode_bmp](https://tensorflow.google.cn/api_docs/python/tf/io/decode_bmp)

---

Decode the first frame of a BMP-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_bmp`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_bmp)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.decode_bmp`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_bmp), [`tf.compat.v1.io.decode_bmp`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_bmp)

```
tf.io.decode_bmp(
    contents: Annotated[Any, _atypes.String], channels: int = 0, name=None
) -> Annotated[Any, _atypes.UInt8]
```

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:

* 0: Use the number of channels in the BMP-encoded image.
* 3: output an RGB image.
* 4: output an RGBA image.

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. 0-D. The BMP-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `uint8`. | |