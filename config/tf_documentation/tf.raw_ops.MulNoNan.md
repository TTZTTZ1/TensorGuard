# tf.raw_ops.MulNoNan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MulNoNan](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MulNoNan)

---

Returns x \* y element-wise. Returns zero if y is zero, even if x if infinite or NaN.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MulNoNan`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MulNoNan)

```
tf.raw_ops.MulNoNan(
    x, y, name=None
)
```

**Note:** `MulNoNan` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |