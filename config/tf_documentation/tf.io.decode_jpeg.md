# tf.io.decode_jpeg

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/decode_jpeg](https://tensorflow.google.cn/api_docs/python/tf/io/decode_jpeg)

---

Decode a JPEG-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_jpeg)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.decode_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_jpeg), [`tf.compat.v1.io.decode_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_jpeg)

```
tf.io.decode_jpeg(
    contents: Annotated[Any, _atypes.String],
    channels: int = 0,
    ratio: int = 1,
    fancy_upscaling: bool = True,
    try_recover_truncated: bool = False,
    acceptable_fraction: float = 1,
    dct_method: str = '',
    name=None
) -> Annotated[Any, _atypes.UInt8]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) | * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Load and preprocess images](https://tensorflow.google.cn/tutorials/load_data/images) * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) |

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:

* 0: Use the number of channels in the JPEG-encoded image.
* 1: output a grayscale image.
* 3: output an RGB image.

If needed, the JPEG-encoded image is transformed to match the requested number
of color channels.

The attr `ratio` allows downscaling the image by an integer factor during
decoding. Allowed values are: 1, 2, 4, and 8. This is much faster than
downscaling the image later.

This op also supports decoding PNGs and non-animated GIFs since the interface is
the same, though it is cleaner to use [`tf.io.decode_image`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_image).

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. 0-D. The JPEG-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `ratio` | An optional `int`. Defaults to `1`. Downscaling ratio. |
| `fancy_upscaling` | An optional `bool`. Defaults to `True`. If true use a slower but nicer upscaling of the chroma planes (yuv420/422 only). |
| `try_recover_truncated` | An optional `bool`. Defaults to `False`. If true try to recover an image from truncated input. |
| `acceptable_fraction` | An optional `float`. Defaults to `1`. The minimum required fraction of lines before a truncated input is accepted. |
| `dct_method` | An optional `string`. Defaults to `""`. string specifying a hint about the algorithm used for decompression. Defaults to "" which maps to a system-specific default. Currently valid values are ["INTEGER\_FAST", "INTEGER\_ACCURATE"]. The hint may be ignored (e.g., the internal jpeg library changes to a version that does not have that specific option.) |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `uint8`. | |