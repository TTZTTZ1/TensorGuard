# tf.math.is_strictly_increasing

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/is_strictly_increasing](https://tensorflow.google.cn/api_docs/python/tf/math/is_strictly_increasing)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L2030-L2069) |

Returns `True` if `x` is strictly increasing.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_strictly_increasing`](https://tensorflow.google.cn/api_docs/python/tf/math/is_strictly_increasing), [`tf.compat.v1.is_strictly_increasing`](https://tensorflow.google.cn/api_docs/python/tf/math/is_strictly_increasing), [`tf.compat.v1.math.is_strictly_increasing`](https://tensorflow.google.cn/api_docs/python/tf/math/is_strictly_increasing)

```
tf.math.is_strictly_increasing(
    x, name=None
)
```

Elements of `x` are compared in row-major order. The tensor `[x[0],...]`
is strictly increasing if for every adjacent pair we have `x[i] < x[i+1]`.
If `x` has less than two elements, it is trivially strictly increasing.

See also: `is_non_decreasing`

```
>>> x1 = tf.constant([1.0, 2.0, 3.0])
>>> tf.math.is_strictly_increasing(x1)
<tf.Tensor: shape=(), dtype=bool, numpy=True>
>>> x2 = tf.constant([3.0, 1.0, 2.0])
>>> tf.math.is_strictly_increasing(x2)
<tf.Tensor: shape=(), dtype=bool, numpy=False>
```

| Args | |

|  |  |
| --- | --- |
| `x` | Numeric `Tensor`. |
| `name` | A name for this operation (optional). Defaults to "is\_strictly\_increasing" |

| Returns | |
| Boolean `Tensor`, equal to `True` iff `x` is strictly increasing. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `x` is not a numeric tensor. |