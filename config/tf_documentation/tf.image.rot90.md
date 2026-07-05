# tf.image.rot90

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/rot90](https://tensorflow.google.cn/api_docs/python/tf/image/rot90)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L659-L722) |

Rotate image(s) by 90 degrees.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.rot90`](https://tensorflow.google.cn/api_docs/python/tf/image/rot90)

```
tf.image.rot90(
    image, k=1, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

#### For example:

```
>>> a=tf.constant([[[1],[2]],
...                [[3],[4]]])
>>> # rotating `a` counter clockwise by 90 degrees
>>> a_rot=tf.image.rot90(a)
>>> print(a_rot[...,0].numpy())
[[2 4]
 [1 3]]
>>> # rotating `a` counter clockwise by 270 degrees
>>> a_rot=tf.image.rot90(a, k=3)
>>> print(a_rot[...,0].numpy())
[[3 1]
 [4 2]]
>>> # rotating `a` clockwise by 180 degrees
>>> a_rot=tf.image.rot90(a, k=-2)
>>> print(a_rot[...,0].numpy())
[[4 3]
 [2 1]]
```

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `k` | A scalar integer tensor. The number of times the image(s) are rotated by 90 degrees. |
| `name` | A name for this operation (optional). |

| Returns | |
| A rotated tensor of the same type and shape as `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the shape of `image` not supported. |