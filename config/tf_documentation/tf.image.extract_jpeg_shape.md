# tf.image.extract_jpeg_shape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/extract_jpeg_shape](https://tensorflow.google.cn/api_docs/python/tf/image/extract_jpeg_shape)

---

Extract the shape information of a JPEG-encoded image.

#### View aliases

**Main aliases**

[`tf.image.extract_jpeg_shape`](https://tensorflow.google.cn/api_docs/python/tf/io/extract_jpeg_shape)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.extract_jpeg_shape`](https://tensorflow.google.cn/api_docs/python/tf/io/extract_jpeg_shape), [`tf.compat.v1.io.extract_jpeg_shape`](https://tensorflow.google.cn/api_docs/python/tf/io/extract_jpeg_shape)

```
tf.io.extract_jpeg_shape(
    contents: Annotated[Any, _atypes.String],
    output_type: TV_ExtractJpegShape_output_type = tf.dtypes.int32,
    name=None
) -> Annotated[Any, TV_ExtractJpegShape_output_type]

tf.dtypes.int32
```

This op only parses the image header, so it is much faster than DecodeJpeg.

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. 0-D. The JPEG-encoded image. |
| `output_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). (Optional) The output type of the operation (int32 or int64). Defaults to int32. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `output_type`. | |