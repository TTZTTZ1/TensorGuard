# tf.raw_ops.DivNoNan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DivNoNan](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DivNoNan)

---

Returns 0 if the denominator is zero.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DivNoNan`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DivNoNan)

```
tf.raw_ops.DivNoNan(
    x, y, name=None
)
```

**Note:** `DivNoNan` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `half`, `float32`, `bfloat16`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |