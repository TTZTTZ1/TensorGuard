# tf.minimum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/minimum](https://tensorflow.google.cn/api_docs/python/tf/minimum)

---

Returns the min of x and y (i.e. x < y ? x : y) element-wise.

#### View aliases

**Main aliases**

[`tf.minimum`](https://tensorflow.google.cn/api_docs/python/tf/math/minimum)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.minimum`](https://tensorflow.google.cn/api_docs/python/tf/math/minimum)

```
tf.math.minimum(
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
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) | * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Neural machine translation with a Transformer and Keras](https://tensorflow.google.cn/text/tutorials/transformer) |

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