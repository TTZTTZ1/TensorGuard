# tf.math.zeta

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/zeta](https://tensorflow.google.cn/api_docs/python/tf/math/zeta)

---

Compute the Hurwitz zeta function \(\zeta(x, q)\).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.zeta`](https://tensorflow.google.cn/api_docs/python/tf/math/zeta), [`tf.compat.v1.zeta`](https://tensorflow.google.cn/api_docs/python/tf/math/zeta)

```
tf.math.zeta(
    x: Annotated[Any, tf.raw_ops.Any],
    q: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

The Hurwitz zeta function is defined as:

\(\zeta(x, q) = \sum\_{n=0}^{\infty} (q + n)^{-x}\)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `q` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |