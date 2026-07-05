# tf.divide

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/divide](https://tensorflow.google.cn/api_docs/python/tf/divide)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L440-L472) |

Computes Python style division of `x` by `y`.

#### View aliases

**Main aliases**

[`tf.divide`](https://tensorflow.google.cn/api_docs/python/tf/math/divide)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.divide`](https://tensorflow.google.cn/api_docs/python/tf/math/divide)

```
tf.math.divide(
    x, y, name=None
)
```

#### For example:

```
>>> x = tf.constant([16, 12, 11])
>>> y = tf.constant([4, 6, 2])
>>> tf.divide(x,y)
<tf.Tensor: shape=(3,), dtype=float64,
numpy=array([4. , 2. , 5.5])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` |
| `y` | A `Tensor` |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` with same shape as input | |