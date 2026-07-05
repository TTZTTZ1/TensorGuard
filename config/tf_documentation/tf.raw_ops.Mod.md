# tf.raw_ops.Mod

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Mod](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Mod)

---

Returns element-wise remainder of division.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Mod`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Mod)

```
tf.raw_ops.Mod(
    x, y, name=None
)
```

This emulates C semantics in that

the result here is consistent with a truncating divide. E.g.
`tf.truncatediv(x, y) * y + truncate_mod(x, y) = x`.

**Note:** `Mod` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `int32`, `int64`, `half`, `half`, `bfloat16`, `float32`, `float64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |