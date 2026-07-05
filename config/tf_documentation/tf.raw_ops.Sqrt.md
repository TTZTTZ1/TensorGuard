# tf.raw_ops.Sqrt

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Sqrt](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Sqrt)

---

Computes square root of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Sqrt`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Sqrt)

```
tf.raw_ops.Sqrt(
    x, name=None
)
```

I.e., \(y = \sqrt{x} = x^{1/2}\).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |