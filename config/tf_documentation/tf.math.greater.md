# tf.math.greater

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/greater](https://tensorflow.google.cn/api_docs/python/tf/math/greater)

---

Returns the truth value of (x > y) element-wise.

#### View aliases

**Main aliases**

[`tf.greater`](https://tensorflow.google.cn/api_docs/python/tf/math/greater)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.greater`](https://tensorflow.google.cn/api_docs/python/tf/math/greater), [`tf.compat.v1.math.greater`](https://tensorflow.google.cn/api_docs/python/tf/math/greater)

```
tf.math.greater(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) | * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [TFX Estimator Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

**Note:** [`math.greater`](https://tensorflow.google.cn/api_docs/python/tf/math/greater) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5, 2, 5])
tf.math.greater(x, y) ==> [False, True, True]

x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.greater(x, y) ==> [False, False, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |