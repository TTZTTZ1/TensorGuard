# tf.math.not_equal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/not_equal](https://tensorflow.google.cn/api_docs/python/tf/math/not_equal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1821-L1855) |

Returns the truth value of (x != y) element-wise.

#### View aliases

**Main aliases**

[`tf.not_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/not_equal)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.not_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/not_equal), [`tf.compat.v1.not_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/not_equal)

```
tf.math.not_equal(
    x, y, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) * [Unicode strings](https://tensorflow.google.cn/text/guide/unicode) | * [Tutorial on Multi Armed Bandits in TF-Agents](https://tensorflow.google.cn/agents/tutorials/bandits_tutorial) |

Performs a [broadcast](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
arguments and then an element-wise inequality comparison, returning a Tensor
of boolean values.

#### For example:

```
>>> x = tf.constant([2, 4])
>>> y = tf.constant(2)
>>> tf.math.not_equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
```

```
>>> x = tf.constant([2, 4])
>>> y = tf.constant([2, 4])
>>> tf.math.not_equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  False])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type bool with the same size as that of x or y. | |

| Raises | |
| [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError): If shapes of arguments are incompatible | |