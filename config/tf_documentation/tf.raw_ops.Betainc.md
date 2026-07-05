# tf.raw_ops.Betainc

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Betainc](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Betainc)

---

Compute the regularized incomplete beta integral \(I\_x(a, b)\).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Betainc`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Betainc)

```
tf.raw_ops.Betainc(
    a, b, x, name=None
)
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