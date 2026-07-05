# tf.floor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/floor](https://tensorflow.google.cn/api_docs/python/tf/floor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5593-L5616) |

Returns element-wise largest integer not greater than x.

#### View aliases

**Main aliases**

[`tf.floor`](https://tensorflow.google.cn/api_docs/python/tf/math/floor)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.floor`](https://tensorflow.google.cn/api_docs/python/tf/math/floor)

```
tf.math.floor(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) |

Both input range is `(-inf, inf)` and the
output range consists of all integer values.

#### For example:

```
>>> x = tf.constant([1.3324, -1.5, 5.555, -2.532, 0.99, float("inf")])
>>> tf.floor(x).numpy()
array([ 1., -2.,  5., -3.,  0., inf], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as x. | |