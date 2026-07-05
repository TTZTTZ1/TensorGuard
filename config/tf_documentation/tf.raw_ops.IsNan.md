# tf.raw_ops.IsNan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsNan](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsNan)

---

Returns which elements of x are NaN.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IsNan`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsNan)

```
tf.raw_ops.IsNan(
    x, name=None
)
```

#### Example:

```
x = tf.constant([5.0, np.nan, 6.8, np.nan, np.inf])
tf.math.is_nan(x) ==> [False, True, False, True, False]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

## numpy compatibility

Equivalent to np.isnan