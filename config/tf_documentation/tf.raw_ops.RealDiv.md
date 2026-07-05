# tf.raw_ops.RealDiv

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RealDiv](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RealDiv)

---

Returns x / y element-wise for real types.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RealDiv`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RealDiv)

```
tf.raw_ops.RealDiv(
    x, y, name=None
)
```

If `x` and `y` are reals, this will return the floating-point division.

**Note:** `Div` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |