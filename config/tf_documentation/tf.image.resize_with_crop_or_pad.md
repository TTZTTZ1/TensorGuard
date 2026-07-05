# tf.image.resize_with_crop_or_pad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/resize_with_crop_or_pad](https://tensorflow.google.cn/api_docs/python/tf/image/resize_with_crop_or_pad)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L1276-L1430) |

Crops and/or pads an image to a target width and height.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.resize_image_with_crop_or_pad`](https://tensorflow.google.cn/api_docs/python/tf/image/resize_with_crop_or_pad), [`tf.compat.v1.image.resize_with_crop_or_pad`](https://tensorflow.google.cn/api_docs/python/tf/image/resize_with_crop_or_pad)

```
tf.image.resize_with_crop_or_pad(
    image, target_height, target_width
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Artistic Style Transfer with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/style_transfer/overview) |

Resizes an image to a target width and height by either centrally
cropping the image or padding it evenly with zeros.

If `width` or `height` is greater than the specified `target_width` or
`target_height` respectively, this op centrally crops along that dimension.

#### For example:

```
>>> image = np.arange(75).reshape(5, 5, 3)  # create 3-D image input
>>> image[:,:,0]  # print first channel just for demo purposes
array([[ 0,  3,  6,  9, 12],
       [15, 18, 21, 24, 27],
       [30, 33, 36, 39, 42],
       [45, 48, 51, 54, 57],
       [60, 63, 66, 69, 72]])
>>> image = tf.image.resize_with_crop_or_pad(image, 3, 3)  # crop
>>> # print first channel for demo purposes; centrally cropped output
>>> image[:,:,0]
<tf.Tensor: shape=(3, 3), dtype=int64, numpy=
array([[18, 21, 24],
       [33, 36, 39],
       [48, 51, 54]])>
```

If `width` or `height` is smaller than the specified `target_width` or
`target_height` respectively, this op centrally pads with 0 along that
dimension.

#### For example:

```
>>> image = np.arange(1, 28).reshape(3, 3, 3)  # create 3-D image input
>>> image[:,:,0]  # print first channel just for demo purposes
array([[ 1,  4,  7],
       [10, 13, 16],
       [19, 22, 25]])
>>> image = tf.image.resize_with_crop_or_pad(image, 5, 5)  # pad
>>> # print first channel for demo purposes; we should see 0 paddings
>>> image[:,:,0]
<tf.Tensor: shape=(5, 5), dtype=int64, numpy=
array([[ 0,  0,  0,  0,  0],
       [ 0,  1,  4,  7,  0],
       [ 0, 10, 13, 16,  0],
       [ 0, 19, 22, 25,  0],
       [ 0,  0,  0,  0,  0]])>
```

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `target_height` | Target height. |
| `target_width` | Target width. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `target_height` or `target_width` are zero or negative. |

| Returns | |
| Cropped and/or padded image. If `images` was 4-D, a 4-D float Tensor of shape `[batch, new_height, new_width, channels]`. If `images` was 3-D, a 3-D float Tensor of shape `[new_height, new_width, channels]`. | |