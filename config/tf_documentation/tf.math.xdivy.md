# tf.math.xdivy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/xdivy](https://tensorflow.google.cn/api_docs/python/tf/math/xdivy)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5255-L5286) |

Computes `x / y`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.xdivy`](https://tensorflow.google.cn/api_docs/python/tf/math/xdivy)

```
tf.math.xdivy(
    x, y, name=None
)
```

Given `x` and `y`, computes `x / y`. This function safely returns
zero when `x = 0`, no matter what the value of `y` is.

#### Example:

```
>>> tf.math.xdivy(1., 2.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.5>
>>> tf.math.xdivy(0., 1.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
>>> tf.math.xdivy(0., 0.)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
>>> tf.math.xdivy(1., 0.)
<tf.Tensor: shape=(), dtype=float32, numpy=inf>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `half`, `float32`, `float64`, `complex64`, `complex128` |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `half`, `float32`, `float64`, `complex64`, `complex128` |
| `name` | A name for the operation (optional). |

| Returns | |
| `x / y`. | |