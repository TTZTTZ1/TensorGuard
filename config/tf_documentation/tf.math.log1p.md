# tf.math.log1p

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/log1p](https://tensorflow.google.cn/api_docs/python/tf/math/log1p)

---

Computes natural logarithm of (1 + x) element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.log1p`](https://tensorflow.google.cn/api_docs/python/tf/math/log1p)

```
tf.math.log1p(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

I.e., \(y = \log\_e (1 + x)\).

#### Example:

```
>>> x = tf.constant([0, 0.5, 1, 5])
>>> tf.math.log1p(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([0.       , 0.4054651, 0.6931472, 1.7917595], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |