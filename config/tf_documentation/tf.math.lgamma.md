# tf.math.lgamma

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/lgamma](https://tensorflow.google.cn/api_docs/python/tf/math/lgamma)

---

Computes the log of the absolute value of `Gamma(x)` element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lgamma`](https://tensorflow.google.cn/api_docs/python/tf/math/lgamma)

```
tf.math.lgamma(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

For positive numbers, this function computes log((input - 1)!) for every element in the tensor.
`lgamma(5) = log((5-1)!) = log(4!) = log(24) = 3.1780539`

#### Example:

```
x = tf.constant([0, 0.5, 1, 4.5, -4, -5.6])
tf.math.lgamma(x) ==> [inf, 0.5723649, 0., 2.4537368, inf, -4.6477685]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |