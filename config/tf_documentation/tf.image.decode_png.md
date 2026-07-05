# tf.image.decode_png

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/decode_png](https://tensorflow.google.cn/api_docs/python/tf/image/decode_png)

---

Decode a PNG-encoded image to a uint8 or uint16 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_png`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_png)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.decode_png`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_png), [`tf.compat.v1.io.decode_png`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_png)

```
tf.io.decode_png(
    contents: Annotated[Any, _atypes.String],
    channels: int = 0,
    dtype: TV_DecodePng_dtype = tf.dtypes.uint8,
    name=None
) -> Annotated[Any, TV_DecodePng_dtype]

tf.dtypes.uint8
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) | * [Displaying image data in TensorBoard](https://tensorflow.google.cn/tensorboard/image_summaries) |

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:

* 0: Use the number of channels in the PNG-encoded image.
* 1: output a grayscale image.
* 3: output an RGB image.
* 4: output an RGBA image.

If needed, the PNG-encoded image is transformed to match the requested number
of color channels.

This op also supports decoding JPEGs and non-animated GIFs since the interface
is the same, though it is cleaner to use [`tf.io.decode_image`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_image).

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. 0-D. The PNG-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.uint8, tf.uint16`. Defaults to [`tf.uint8`](https://tensorflow.google.cn/api_docs/python/tf#uint8). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |