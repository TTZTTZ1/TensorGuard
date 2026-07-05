# tf.raw_ops.IsInf

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsInf](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsInf)

---

Returns which elements of x are Inf.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IsInf`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsInf)

```
tf.raw_ops.IsInf(
    x, name=None
)
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