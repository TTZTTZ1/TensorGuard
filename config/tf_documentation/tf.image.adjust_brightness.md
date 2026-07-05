# tf.image.adjust_brightness

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/adjust_brightness](https://tensorflow.google.cn/api_docs/python/tf/image/adjust_brightness)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2200-L2250) |

Adjust the brightness of RGB or Grayscale images.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.adjust_brightness`](https://tensorflow.google.cn/api_docs/python/tf/image/adjust_brightness)

```
tf.image.adjust_brightness(
    image, delta
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

This is a convenience method that converts RGB images to float
representation, adjusts their brightness, and then converts them back to the
original data type. If several adjustments are chained, it is advisable to
minimize the number of redundant conversions.

The value `delta` is added to all components of the tensor `image`. `image` is
converted to `float` and scaled appropriately if it is in fixed-point
representation, and `delta` is converted to the same data type. For regular
images, `delta` should be in the range `(-1,1)`, as it is added to the image
in floating point representation, where pixel values are in the `[0,1)` range.

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.adjust_brightness(x, delta=0.1)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 1.1,  2.1,  3.1],
        [ 4.1,  5.1,  6.1]],
       [[ 7.1,  8.1,  9.1],
        [10.1, 11.1, 12.1]]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `image` | RGB image or images to adjust. |
| `delta` | A scalar. Amount to add to the pixel values. |

| Returns | |
| A brightness-adjusted tensor of the same shape and type as `image`. | |