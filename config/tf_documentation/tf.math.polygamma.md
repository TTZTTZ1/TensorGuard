# tf.math.polygamma

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/polygamma](https://tensorflow.google.cn/api_docs/python/tf/math/polygamma)

---

Compute the polygamma function \(\psi^{(n)}(x)\).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.polygamma`](https://tensorflow.google.cn/api_docs/python/tf/math/polygamma), [`tf.compat.v1.polygamma`](https://tensorflow.google.cn/api_docs/python/tf/math/polygamma)

```
tf.math.polygamma(
    a: Annotated[Any, tf.raw_ops.Any],
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

The polygamma function is defined as:

\(\psi^{(a)}(x) = \frac{d^a}{dx^a} \psi(x)\)

where \(\psi(x)\) is the digamma function.
The polygamma function is defined only for non-negative integer orders \a\.

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |