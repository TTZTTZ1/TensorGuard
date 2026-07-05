# tf.logical_and

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/logical_and](https://tensorflow.google.cn/api_docs/python/tf/logical_and)

---

Returns the truth value of x AND y element-wise.

#### View aliases

**Main aliases**

[`tf.logical_and`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_and)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.logical_and`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_and), [`tf.compat.v1.math.logical_and`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_and)

```
tf.math.logical_and(
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
| * [Tutorial on Multi Armed Bandits in TF-Agents](https://tensorflow.google.cn/agents/tutorials/bandits_tutorial) |

Logical AND function.

Requires that `x` and `y` have the same shape or have
[broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
shapes. For example, `x` and `y` can be:

* Two single elements of type `bool`.
* One [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `bool` and one single `bool`, where the result will
  be calculated by applying logical AND with the single element to each
  element in the larger Tensor.
* Two [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical AND of the two input tensors.

You can also use the `&` operator instead.

| Usage | |
|  | |

```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_and(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>
>>> a & b
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_and(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
>>> c & x
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_and(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False, True])>
>>> y & z
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False, True])>
```

This op also supports broadcasting

```
>>> tf.logical_and([[True, False]], [[True], [False]])
<tf.Tensor: shape=(2, 2), dtype=bool, numpy=
  array([[ True, False],
         [False, False]])>
```

The reduction version of this elementwise operation is [`tf.math.reduce_all`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_all).

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