# tf.math.xlogy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/xlogy](https://tensorflow.google.cn/api_docs/python/tf/math/xlogy)

---

Returns 0 if x == 0, and x \* log(y) otherwise, elementwise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.xlogy`](https://tensorflow.google.cn/api_docs/python/tf/math/xlogy)

```
tf.math.xlogy(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |