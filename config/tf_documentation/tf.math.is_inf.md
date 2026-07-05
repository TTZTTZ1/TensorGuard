# tf.math.is_inf

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/is_inf](https://tensorflow.google.cn/api_docs/python/tf/math/is_inf)

---

Returns which elements of x are Inf.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_inf`](https://tensorflow.google.cn/api_docs/python/tf/math/is_inf), [`tf.compat.v1.is_inf`](https://tensorflow.google.cn/api_docs/python/tf/math/is_inf), [`tf.compat.v1.math.is_inf`](https://tensorflow.google.cn/api_docs/python/tf/math/is_inf)

```
tf.math.is_inf(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

#### Example:

```
x = tf.constant([5.0, np.inf, 6.8, np.inf])
tf.math.is_inf(x) ==> [False, True, False, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

## numpy compatibility

Equivalent to np.isinf