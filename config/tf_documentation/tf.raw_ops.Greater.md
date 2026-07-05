# tf.raw_ops.Greater

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Greater](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Greater)

---

Returns the truth value of (x > y) element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Greater`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Greater)

```
tf.raw_ops.Greater(
    x, y, name=None
)
```

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