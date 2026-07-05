# tf.math.greater_equal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal)

---

Returns the truth value of (x >= y) element-wise.

#### View aliases

**Main aliases**

[`tf.greater_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.greater_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal), [`tf.compat.v1.math.greater_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal)

```
tf.math.greater_equal(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TensorFlow Ranking Keras pipeline for distributed training](https://tensorflow.google.cn/ranking/tutorials/ranking_dnn_distributed) |

**Note:** [`math.greater_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6, 7])
y = tf.constant([5, 2, 5, 10])
tf.math.greater_equal(x, y) ==> [True, True, True, False]

x = tf.constant([5, 4, 6, 7])
y = tf.constant([5])
tf.math.greater_equal(x, y) ==> [True, False, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |