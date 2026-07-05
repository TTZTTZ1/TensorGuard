# tf.raw_ops.ResizeNearestNeighborGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResizeNearestNeighborGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResizeNearestNeighborGrad)

---

Computes the gradient of nearest neighbor interpolation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResizeNearestNeighborGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResizeNearestNeighborGrad)

```
tf.raw_ops.ResizeNearestNeighborGrad(
    grads, size, align_corners=False, half_pixel_centers=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `grads` | A `Tensor`. Must be one of the following types: `uint8`, `int8`, `int32`, `half`, `float32`, `float64`, `bfloat16`. 4-D with shape `[batch, height, width, channels]`. |
| `size` | A 1-D int32 Tensor of 2 elements: `orig_height, orig_width`. The original input size. |
| `align_corners` | An optional `bool`. Defaults to `False`. If true, the centers of the 4 corner pixels of the input and grad tensors are aligned. Defaults to false. |
| `half_pixel_centers` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `grads`. | |