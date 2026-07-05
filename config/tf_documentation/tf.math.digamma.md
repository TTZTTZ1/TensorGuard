# tf.math.digamma

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/digamma](https://tensorflow.google.cn/api_docs/python/tf/math/digamma)

---

Computes Psi, the derivative of Lgamma (the log of the absolute value of

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.digamma`](https://tensorflow.google.cn/api_docs/python/tf/math/digamma)

```
tf.math.digamma(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

`Gamma(x)`), element-wise.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |