# tf.math.erfcinv

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/erfcinv](https://tensorflow.google.cn/api_docs/python/tf/math/erfcinv)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5362-L5389) |

Computes the inverse of complementary error function.

```
tf.math.erfcinv(
    x, name=None
)
```

Given `x`, compute the inverse complementary error function of `x`.
This function is the inverse of [`tf.math.erfc`](https://tensorflow.google.cn/api_docs/python/tf/math/erfc), and is defined on
`[0, 2]`.

```
>>> tf.math.erfcinv([0., 0.2, 1., 1.5, 2.])
<tf.Tensor: shape=(5,), dtype=float32, numpy=
array([       inf,  0.9061935, -0.       , -0.4769363,       -inf],
      dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor` with type `float` or `double`. |
| `name` | A name for the operation (optional). |

| Returns | |
| Inverse complementary error function of `x`. | |

## numpy compatibility

Equivalent to scipy.special.erfcinv