# tf.raw_ops.AddV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AddV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AddV2)

---

Returns x + y element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AddV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AddV2)

```
tf.raw_ops.AddV2(
    x, y, name=None
)
```

**Note:** `Add` supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |