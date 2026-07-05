# tf.math.igammac

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/igammac](https://tensorflow.google.cn/api_docs/python/tf/math/igammac)

---

Compute the upper regularized incomplete Gamma function `Q(a, x)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.igammac`](https://tensorflow.google.cn/api_docs/python/tf/math/igammac), [`tf.compat.v1.math.igammac`](https://tensorflow.google.cn/api_docs/python/tf/math/igammac)

```
tf.math.igammac(
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