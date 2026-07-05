# tf.raw_ops.Igamma

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igamma](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igamma)

---

Compute the lower regularized incomplete Gamma function `P(a, x)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Igamma`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Igamma)

```
tf.raw_ops.Igamma(
    a, x, name=None
)
```

The lower regularized incomplete Gamma function is defined as:

\(P(a, x) = gamma(a, x) / Gamma(a) = 1 - Q(a, x)\)

where

\(gamma(a, x) = \\int\_{0}^{x} t^{a-1} exp(-t) dt\)

is the lower incomplete Gamma function.

Note, above `Q(a, x)` (`Igammac`) is the upper regularized complete
Gamma function.

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |