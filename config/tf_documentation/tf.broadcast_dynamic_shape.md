# tf.broadcast_dynamic_shape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/broadcast_dynamic_shape](https://tensorflow.google.cn/api_docs/python/tf/broadcast_dynamic_shape)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L526-L557) |

Computes the shape of a broadcast given symbolic shapes.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.broadcast_dynamic_shape`](https://tensorflow.google.cn/api_docs/python/tf/broadcast_dynamic_shape)

```
tf.broadcast_dynamic_shape(
    shape_x, shape_y
)
```

When `shape_x` and `shape_y` are Tensors representing shapes (i.e. the result
of calling tf.shape on another Tensor) this computes a Tensor which is the
shape of the result of a broadcasting op applied in tensors of shapes
`shape_x` and `shape_y`.

This is useful when validating the result of a broadcasting operation when the
tensors do not have statically known shapes.

#### Example:

```
>>> shape_x = (1, 2, 3)
>>> shape_y = (5, 1, 3)
>>> tf.broadcast_dynamic_shape(shape_x, shape_y)
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([5, 2, 3], ...>
```

| Args | |

|  |  |
| --- | --- |
| `shape_x` | A rank 1 integer `Tensor`, representing the shape of x. |
| `shape_y` | A rank 1 integer `Tensor`, representing the shape of y. |

| Returns | |
| A rank 1 integer `Tensor` representing the broadcasted shape. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | If the two shapes are incompatible for broadcasting. |