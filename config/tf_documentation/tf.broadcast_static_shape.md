# tf.broadcast_static_shape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/broadcast_static_shape](https://tensorflow.google.cn/api_docs/python/tf/broadcast_static_shape)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L560-L593) |

Computes the shape of a broadcast given known shapes.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.broadcast_static_shape`](https://tensorflow.google.cn/api_docs/python/tf/broadcast_static_shape)

```
tf.broadcast_static_shape(
    shape_x, shape_y
)
```

When `shape_x` and `shape_y` are fully known `TensorShape`s this computes a
`TensorShape` which is the shape of the result of a broadcasting op applied in
tensors of shapes `shape_x` and `shape_y`.

For example, if shape\_x is `TensorShape([1, 2, 3])` and shape\_y is
`TensorShape([5, 1, 3])`, the result is a TensorShape whose value is
`TensorShape([5, 2, 3])`.

This is useful when validating the result of a broadcasting operation when the
tensors have statically known shapes.

#### Example:

```
>>> shape_x = tf.TensorShape([1, 2, 3])
>>> shape_y = tf.TensorShape([5, 1 ,3])
>>> tf.broadcast_static_shape(shape_x, shape_y)
TensorShape([5, 2, 3])
```

| Args | |

|  |  |
| --- | --- |
| `shape_x` | A `TensorShape` |
| `shape_y` | A `TensorShape` |

| Returns | |
| A `TensorShape` representing the broadcasted shape. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the two shapes can not be broadcasted. |