# tf.math.xlog1py

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/xlog1py](https://tensorflow.google.cn/api_docs/python/tf/math/xlog1py)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5289-L5324) |

Compute x \* log1p(y).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.xlog1py`](https://tensorflow.google.cn/api_docs/python/tf/math/xlog1py)

```
tf.math.xlog1py(
    x, y, name=None
)
```

Given `x` and `y`, compute `x * log1p(y)`. This function safely returns
zero when `x = 0`, no matter what the value of `y` is.

#### Example:

```
>>> tf.math.xlog1py(0., 1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.>
>>> tf.math.xlog1py(1., 1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.6931472>
>>> tf.math.xlog1py(2., 2.)
<tf.Tensor: shape=(), dtype=float32, numpy=2.1972246>
>>> tf.math.xlog1py(0., -1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `half`, `float32`, `float64`, `complex64`, `complex128` |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `half`, `float32`, `float64`, `complex64`, `complex128` |
| `name` | A name for the operation (optional). |

| Returns | |
| `x * log1p(y)`. | |

## scipy compatibility

Equivalent to scipy.special.xlog1py