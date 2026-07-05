# tf.math.squared_difference

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/squared_difference](https://tensorflow.google.cn/api_docs/python/tf/math/squared_difference)

---

Returns conj(x - y)(x - y) element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.squared_difference`](https://tensorflow.google.cn/api_docs/python/tf/math/squared_difference), [`tf.compat.v1.squared_difference`](https://tensorflow.google.cn/api_docs/python/tf/math/squared_difference)

```
tf.math.squared_difference(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

**Note:** [`math.squared_difference`](https://tensorflow.google.cn/api_docs/python/tf/math/squared_difference) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |