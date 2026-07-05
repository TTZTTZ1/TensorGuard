# tf.math.erfinv

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/erfinv](https://tensorflow.google.cn/api_docs/python/tf/math/erfinv)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5327-L5343) |

Compute inverse error function.

```
tf.math.erfinv(
    x, name=None
)
```

Given `x`, compute the inverse error function of `x`. This function
is the inverse of [`tf.math.erf`](https://tensorflow.google.cn/api_docs/python/tf/math/erf).

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor` with type `float` or `double`. |
| `name` | A name for the operation (optional). |

| Returns | |
| Inverse error function of `x`. | |