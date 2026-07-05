# tf.raw_ops.ReciprocalGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReciprocalGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReciprocalGrad)

---

Computes the gradient for the inverse of `x` wrt its input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReciprocalGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReciprocalGrad)

```
tf.raw_ops.ReciprocalGrad(
    y, dy, name=None
)
```

Specifically, `grad = -dy * y*y`, where `y = 1/x`, and `dy`
is the corresponding input gradient.

| Args | |

|  |  |
| --- | --- |
| `y` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `dy` | A `Tensor`. Must have the same type as `y`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `y`. | |