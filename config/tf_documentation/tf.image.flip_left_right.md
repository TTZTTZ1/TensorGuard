# tf.image.flip_left_right

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/flip_left_right](https://tensorflow.google.cn/api_docs/python/tf/image/flip_left_right)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L547-L579) |

Flip an image horizontally (left to right).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.flip_left_right`](https://tensorflow.google.cn/api_docs/python/tf/image/flip_left_right)

```
tf.image.flip_left_right(
    image
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

Outputs the contents of `image` flipped along the width dimension.

See also [`tf.reverse`](https://tensorflow.google.cn/api_docs/python/tf/reverse).

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.flip_left_right(x)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 4.,  5.,  6.],
        [ 1.,  2.,  3.]],
       [[10., 11., 12.],
        [ 7.,  8.,  9.]]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |

| Returns | |
| A tensor of the same type and shape as `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the shape of `image` not supported. |