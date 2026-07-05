# tf.math.reciprocal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reciprocal](https://tensorflow.google.cn/api_docs/python/tf/math/reciprocal)

---

Computes the reciprocal of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.reciprocal`](https://tensorflow.google.cn/api_docs/python/tf/math/reciprocal)

```
tf.math.reciprocal(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

I.e., \(y = 1 / x\).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |