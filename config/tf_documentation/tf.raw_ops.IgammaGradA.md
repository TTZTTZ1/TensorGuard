# tf.raw_ops.IgammaGradA

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgammaGradA](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgammaGradA)

---

Computes the gradient of `igamma(a, x)` wrt `a`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IgammaGradA`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgammaGradA)

```
tf.raw_ops.IgammaGradA(
    a, x, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |