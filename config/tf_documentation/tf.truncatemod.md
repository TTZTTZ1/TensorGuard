# tf.truncatemod

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/truncatemod](https://tensorflow.google.cn/api_docs/python/tf/truncatemod)

---

Returns element-wise remainder of division.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.truncatemod`](https://tensorflow.google.cn/api_docs/python/tf/truncatemod)

```
tf.truncatemod(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

This emulates C semantics in that

the result here is consistent with a truncating divide. E.g. `truncate(x / y) *
y + truncate_mod(x, y) = x`.

**Note:** `truncatemod` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |