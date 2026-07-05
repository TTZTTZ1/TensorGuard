# tf.raw_ops.Div

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Div](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Div)

---

Returns x / y element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Div`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Div)

```
tf.raw_ops.Div(
    x, y, name=None
)
```

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