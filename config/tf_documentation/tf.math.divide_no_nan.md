# tf.math.divide_no_nan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/divide_no_nan](https://tensorflow.google.cn/api_docs/python/tf/math/divide_no_nan)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1520-L1572) |

Computes a safe divide which returns 0 if `y` (denominator) is zero.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.div_no_nan`](https://tensorflow.google.cn/api_docs/python/tf/math/divide_no_nan)

```
tf.math.divide_no_nan(
    x, y, name=None
)
```

#### For example:

```
>>> tf.constant(3.0) / 0.0
<tf.Tensor: shape=(), dtype=float32, numpy=inf>
>>> tf.math.divide_no_nan(3.0, 0.0)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
```

Note that 0 is returned if `y` is 0 even if `x` is nonfinite:

```
>>> tf.math.divide_no_nan(np.nan, 0.0)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of a floating or integer dtype. |
| `y` | A `Tensor` with the same dtype as `x` and a compatible shape. |
| `name` | A name for the operation (optional). |

| Returns | |
| The element-wise quotient as in [`tf.math.divide(x, y)`](https://tensorflow.google.cn/api_docs/python/tf/math/divide), except that division by zero produces `0.0`, not `nan`. | |