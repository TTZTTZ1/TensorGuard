# tf.math.betainc

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/betainc](https://tensorflow.google.cn/api_docs/python/tf/math/betainc)

---

Compute the regularized incomplete beta integral \(I\_x(a, b)\).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.betainc`](https://tensorflow.google.cn/api_docs/python/tf/math/betainc), [`tf.compat.v1.math.betainc`](https://tensorflow.google.cn/api_docs/python/tf/math/betainc)

```
tf.math.betainc(
    a: Annotated[Any, tf.raw_ops.Any],
    b: Annotated[Any, tf.raw_ops.Any],
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

The regularized incomplete beta integral is defined as:

\(I\_x(a, b) = \frac{B(x; a, b)}{B(a, b)}\)

where

\(B(x; a, b) = \int\_0^x t^{a-1} (1 - t)^{b-1} dt\)

is the incomplete beta function and \(B(a, b)\) is the *complete*
beta function.

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `b` | A `Tensor`. Must have the same type as `a`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |