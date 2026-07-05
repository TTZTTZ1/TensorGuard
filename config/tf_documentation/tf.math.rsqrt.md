# tf.math.rsqrt

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/rsqrt](https://tensorflow.google.cn/api_docs/python/tf/math/rsqrt)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5537-L5559) |

Computes reciprocal of square root of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.rsqrt`](https://tensorflow.google.cn/api_docs/python/tf/math/rsqrt)

```
tf.math.rsqrt(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Neural machine translation with a Transformer and Keras](https://tensorflow.google.cn/text/tutorials/transformer) |

#### For example:

```
>>> x = tf.constant([2., 0., -2.])
>>> tf.math.rsqrt(x)
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([0.707, inf, nan], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Has the same type as `x`. | |