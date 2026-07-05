# tf.raw_ops.Xlogy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xlogy](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xlogy)

---

Returns 0 if x == 0, and x \* log(y) otherwise, elementwise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Xlogy`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xlogy)

```
tf.raw_ops.Xlogy(
    x, y, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |