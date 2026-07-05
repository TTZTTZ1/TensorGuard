# tf.raw_ops.Log

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Log](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Log)

---

Computes natural logarithm of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Log`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Log)

```
tf.raw_ops.Log(
    x, name=None
)
```

I.e., \(y = \log\_e x\).

#### Example:

```
>>> x = tf.constant([0, 0.5, 1, 5])
>>> tf.math.log(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([      -inf, -0.6931472,  0.       ,  1.609438 ], dtype=float32)>
```

See: <https://en.wikipedia.org/wiki/Logarithm>

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |