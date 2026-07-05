# tf.math.is_nan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/is_nan](https://tensorflow.google.cn/api_docs/python/tf/math/is_nan)

---

Returns which elements of x are NaN.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_nan`](https://tensorflow.google.cn/api_docs/python/tf/math/is_nan), [`tf.compat.v1.is_nan`](https://tensorflow.google.cn/api_docs/python/tf/math/is_nan), [`tf.compat.v1.math.is_nan`](https://tensorflow.google.cn/api_docs/python/tf/math/is_nan)

```
tf.math.is_nan(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) | * [TFX Estimator Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

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