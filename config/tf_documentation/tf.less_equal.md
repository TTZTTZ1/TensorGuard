# tf.less_equal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/less_equal](https://tensorflow.google.cn/api_docs/python/tf/less_equal)

---

Returns the truth value of (x <= y) element-wise.

#### View aliases

**Main aliases**

[`tf.less_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/less_equal)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.less_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/less_equal), [`tf.compat.v1.math.less_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/less_equal)

```
tf.math.less_equal(
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
| * [Federated Reconstruction for Matrix Factorization](https://tensorflow.google.cn/federated/tutorials/federated_reconstruction_for_matrix_factorization) |

**Note:** [`math.less_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/less_equal) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less_equal(x, y) ==> [True, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 6])
tf.math.less_equal(x, y) ==> [True, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |