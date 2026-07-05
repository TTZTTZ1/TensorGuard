# tf.image.crop_to_bounding_box

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/crop_to_bounding_box](https://tensorflow.google.cn/api_docs/python/tf/image/crop_to_bounding_box)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L1169-L1273) |

Crops an `image` to a specified bounding box.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.crop_to_bounding_box`](https://tensorflow.google.cn/api_docs/python/tf/image/crop_to_bounding_box)

```
tf.image.crop_to_bounding_box(
    image, offset_height, offset_width, target_height, target_width
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Image Super Resolution using ESRGAN](https://tensorflow.google.cn/hub/tutorials/image_enhancing) * [Fast Style Transfer for Arbitrary Styles](https://tensorflow.google.cn/hub/tutorials/tf2_arbitrary_image_stylization) * [Frame interpolation using the FILM model](https://tensorflow.google.cn/hub/tutorials/tf_hub_film_example) |

This op cuts a rectangular bounding box out of `image`. The top-left corner
of the bounding box is at `offset_height, offset_width` in `image`, and the
lower-right corner is at
`offset_height + target_height, offset_width + target_width`.

#### Example Usage:

```
>>> image = tf.constant(np.arange(1, 28, dtype=np.float32), shape=[3, 3, 3])
>>> image[:,:,0] # print the first channel of the 3-D tensor
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[ 1.,  4.,  7.],
       [10., 13., 16.],
       [19., 22., 25.]], dtype=float32)>
>>> cropped_image = tf.image.crop_to_bounding_box(image, 0, 0, 2, 2)
>>> cropped_image[:,:,0] # print the first channel of the cropped 3-D tensor
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
array([[ 1.,  4.],
       [10., 13.]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D `Tensor` of shape `[batch, height, width, channels]` or 3-D `Tensor` of shape `[height, width, channels]`. |
| `offset_height` | Vertical coordinate of the top-left corner of the bounding box in `image`. Must be 0-D int32 `Tensor` or python integer. |
| `offset_width` | Horizontal coordinate of the top-left corner of the bounding box in `image`. Must be 0-D int32 `Tensor` or python integer. |
| `target_height` | Height of the bounding box. Must be 0-D int32 `Tensor` or python integer. |
| `target_width` | Width of the bounding box. Must be 0-D int32 `Tensor` or python integer. |

| Returns | |
| If `image` was 4-D, a 4-D `Tensor` of shape `[batch, target_height, target_width, channels]`. If `image` was 3-D, a 3-D `Tensor` of shape `[target_height, target_width, channels]`. It has the same dtype with `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | `image` is not a 3-D or 4-D `Tensor`. |
| `ValueError` | `offset_width < 0` or `offset_height < 0`. |
| `ValueError` | `target_width <= 0` or `target_height <= 0`. |
| `ValueError` | `width < offset_width + target_width` or `height < offset_height + target_height`. |