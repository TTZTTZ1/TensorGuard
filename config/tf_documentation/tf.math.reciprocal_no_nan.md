# tf.math.reciprocal_no_nan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reciprocal_no_nan](https://tensorflow.google.cn/api_docs/python/tf/math/reciprocal_no_nan)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5221-L5252) |

Performs a safe reciprocal operation, element wise.

```
tf.math.reciprocal_no_nan(
    x, name=None
)
```

If a particular element is zero, the reciprocal for that element is
also set to zero.

#### For example:

```
x = tf.constant([2.0, 0.5, 0, 1], dtype=tf.float32)
tf.math.reciprocal_no_nan(x)  # [ 0.5, 2, 0.0, 1.0 ]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of type `float16`, `float32`, `float64` `complex64` or `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of same shape and type as `x`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | x must be of a valid dtype. |