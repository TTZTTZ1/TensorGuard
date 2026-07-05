# tf.image.grayscale_to_rgb

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/grayscale_to_rgb](https://tensorflow.google.cn/api_docs/python/tf/image/grayscale_to_rgb)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2599-L2632) |

Converts one or more images from Grayscale to RGB.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.grayscale_to_rgb`](https://tensorflow.google.cn/api_docs/python/tf/image/grayscale_to_rgb)

```
tf.image.grayscale_to_rgb(
    images, name=None
)
```

Outputs a tensor of the same `DType` and rank as `images`. The size of the
last dimension of the output is 3, containing the RGB value of the pixels.
The input images' last dimension must be size 1.

```
>>> original = tf.constant([[[1.0], [2.0], [3.0]]])
>>> converted = tf.image.grayscale_to_rgb(original)
>>> print(converted.numpy())
[[[1. 1. 1.]
  [2. 2. 2.]
  [3. 3. 3.]]]
```

| Args | |

|  |  |
| --- | --- |
| `images` | The Grayscale tensor to convert. The last dimension must be size 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The converted grayscale image(s). | |