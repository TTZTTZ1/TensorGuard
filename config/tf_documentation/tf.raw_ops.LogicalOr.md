# tf.raw_ops.LogicalOr

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalOr](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalOr)

---

Returns the truth value of x OR y element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LogicalOr`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalOr)

```
tf.raw_ops.LogicalOr(
    x, y, name=None
)
```

Logical OR function.

Requires that `x` and `y` have the same shape or have
[broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
shapes. For example, `x` and `y` can be:

* Two single elements of type `bool`.
* One [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `bool` and one single `bool`, where the result will
  be calculated by applying logical OR with the single element to each
  element in the larger Tensor.
* Two [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical OR of the two input tensors.

You can also use the `|` operator instead.

| Usage | |
|  | |

```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_or(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
>>> a | b
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
```

```
>>> c = tf.constant([False])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_or(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>
>>> c | x
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_or(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>
>>> y | z
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>
```

This op also supports broadcasting

```
>>> tf.logical_or([[True, False]], [[True], [False]])
<tf.Tensor: shape=(2, 2), dtype=bool, numpy=
array([[ True,  True],
     [ True, False]])>
```

The reduction version of this elementwise operation is [`tf.math.reduce_any`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_any).

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type bool. |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type bool. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type bool with the shape that `x` and `y` broadcast to. | |

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of type `bool`. |
| `y` | A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |