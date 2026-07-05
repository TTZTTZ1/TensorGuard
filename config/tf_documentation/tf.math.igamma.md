# tf.math.igamma

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/igamma](https://tensorflow.google.cn/api_docs/python/tf/math/igamma)

---

Compute the lower regularized incomplete Gamma function `P(a, x)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.igamma`](https://tensorflow.google.cn/api_docs/python/tf/math/igamma), [`tf.compat.v1.math.igamma`](https://tensorflow.google.cn/api_docs/python/tf/math/igamma)

```
tf.math.igamma(
    a: Annotated[Any, tf.raw_ops.Any],
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) |

The lower regularized incomplete Gamma function is defined as:

\(P(a, x) = gamma(a, x) / Gamma(a) = 1 - Q(a, x)\)

where

\(gamma(a, x) = \int\_{0}^{x} t^{a-1} exp(-t) dt\)

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