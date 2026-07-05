# tf.math.less

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/less](https://tensorflow.google.cn/api_docs/python/tf/math/less)

---

Returns the truth value of (x < y) element-wise.

#### View aliases

**Main aliases**

[`tf.less`](https://tensorflow.google.cn/api_docs/python/tf/math/less)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.less`](https://tensorflow.google.cn/api_docs/python/tf/math/less), [`tf.compat.v1.math.less`](https://tensorflow.google.cn/api_docs/python/tf/math/less)

```
tf.math.less(
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
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) | * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) |

**Note:** [`math.less`](https://tensorflow.google.cn/api_docs/python/tf/math/less) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less(x, y) ==> [False, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 7])
tf.math.less(x, y) ==> [False, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |