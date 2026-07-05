# tf.image.rgb_to_yuv

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_yuv](https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_yuv)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L4043-L4066) |

Converts one or more images from RGB to YUV.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.rgb_to_yuv`](https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_yuv)

```
tf.image.rgb_to_yuv(
    images
)
```

Outputs a tensor of the same shape as the `images` tensor, containing the YUV
value of the pixels.
The output is only well defined if the value in images are in [0, 1].
There are two ways of representing an image: [0, 255] pixel values range or
[0, 1](/api_docs/python/tf/image/as%20float) pixel values range. Users need to convert the input image
into a float [0, 1] range.

| Args | |

|  |  |
| --- | --- |
| `images` | 2-D or higher rank. Image data to convert. Last dimension must be size 3. |

| Returns | |

|  |  |
| --- | --- |
| `images` | tensor with the same shape as `images`. |