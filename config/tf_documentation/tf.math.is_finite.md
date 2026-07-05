# tf.math.is_finite

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/is_finite](https://tensorflow.google.cn/api_docs/python/tf/math/is_finite)

---

Returns which elements of x are finite.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_finite`](https://tensorflow.google.cn/api_docs/python/tf/math/is_finite), [`tf.compat.v1.is_finite`](https://tensorflow.google.cn/api_docs/python/tf/math/is_finite), [`tf.compat.v1.math.is_finite`](https://tensorflow.google.cn/api_docs/python/tf/math/is_finite)

```
tf.math.is_finite(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) |

#### Example:

```
x = tf.constant([5.0, 4.8, 6.8, np.inf, np.nan])
tf.math.is_finite(x) ==> [True, True, True, False, False]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

## numpy compatibility

Equivalent to np.isfinite