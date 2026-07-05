# tf.raw_ops.Igammac

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igammac](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igammac)

---

Compute the upper regularized incomplete Gamma function `Q(a, x)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Igammac`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igammac)

```
tf.raw_ops.Igammac(
    a, x, name=None
)
```

The upper regularized incomplete Gamma function is defined as:

\(Q(a, x) = Gamma(a, x) / Gamma(a) = 1 - P(a, x)\)

where

\(Gamma(a, x) = \int\_{x}^{\infty} t^{a-1} exp(-t) dt\)

is the upper incomplete Gamma function.

Note, above `P(a, x)` (`Igamma`) is the lower regularized complete
Gamma function.

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |