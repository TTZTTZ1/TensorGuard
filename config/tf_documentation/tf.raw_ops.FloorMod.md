# tf.raw_ops.FloorMod

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FloorMod](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FloorMod)

---

Returns element-wise remainder of division.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FloorMod`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FloorMod)

```
tf.raw_ops.FloorMod(
    x, y, name=None
)
```

This follows Python semantics in that the
result here is consistent with a flooring divide. E.g.
`floor(x / y) * y + floormod(x, y) = x`, regardless of the signs of x and y.

**Note:** [`math.floormod`](https://tensorflow.google.cn/api_docs/python/tf/math/floormod) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `bfloat16`, `half`, `float32`, `float64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |