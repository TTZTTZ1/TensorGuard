# tf.raw_ops.Minimum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Minimum](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Minimum)

---

Returns the min of x and y (i.e. x < y ? x : y) element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Minimum`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Minimum)

```
tf.raw_ops.Minimum(
    x, y, name=None
)
```

Both inputs are number-type tensors (except complex). `minimum` expects that
both tensors have the same `dtype`.

#### Examples:

```
>>> x = tf.constant([0., 0., 0., 0.])
>>> y = tf.constant([-5., -2., 0., 3.])
>>> tf.math.minimum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -2., 0., 0.], dtype=float32)>
```

Note that `minimum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) for `x` and `y`.

```
>>> x = tf.constant([-5., 0., 0., 0.])
>>> y = tf.constant([-3.])
>>> tf.math.minimum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -3., -3., -3.], dtype=float32)>
```

The reduction version of this elementwise operation is [`tf.math.reduce_min`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_min)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |