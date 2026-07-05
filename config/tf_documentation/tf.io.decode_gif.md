# tf.io.decode_gif

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/decode_gif](https://tensorflow.google.cn/api_docs/python/tf/io/decode_gif)

---

Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_gif`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_gif)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.decode_gif`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_gif), [`tf.compat.v1.io.decode_gif`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_gif)

```
tf.io.decode_gif(
    contents: Annotated[Any, _atypes.String], name=None
) -> Annotated[Any, _atypes.UInt8]
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [MoveNet: Ultra fast and accurate pose detection model.](https://tensorflow.google.cn/hub/tutorials/movenet) * [MoViNet for streaming action recognition](https://tensorflow.google.cn/hub/tutorials/movinet) |

GIF images with frame or transparency compression are not supported.
On Linux and MacOS systems, convert animated GIFs from compressed to
uncompressed by running:

```
convert \\(src.gif -coalesce \\)dst.gif
```

This op also supports decoding JPEGs and PNGs, though it is cleaner to use
[`tf.io.decode_image`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_image).

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. 0-D. The GIF-encoded image. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `uint8`. | |