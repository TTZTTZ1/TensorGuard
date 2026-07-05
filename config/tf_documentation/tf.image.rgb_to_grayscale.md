# tf.image.rgb_to_grayscale

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_grayscale](https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_grayscale)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2563-L2596) |

Converts one or more images from RGB to Grayscale.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.rgb_to_grayscale`](https://tensorflow.google.cn/api_docs/python/tf/image/rgb_to_grayscale)

```
tf.image.rgb_to_grayscale(
    images, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

Outputs a tensor of the same `DType` and rank as `images`. The size of the
last dimension of the output is 1, containing the Grayscale value of the
pixels.

```
>>> original = tf.constant([[[1.0, 2.0, 3.0]]])
>>> converted = tf.image.rgb_to_grayscale(original)
>>> print(converted.numpy())
[[[1.81...]]]
```

| Args | |

|  |  |
| --- | --- |
| `images` | The RGB tensor to convert. The last dimension must have size 3 and should contain RGB values. |
| `name` | A name for the operation (optional). |

| Returns | |
| The converted grayscale image(s). | |