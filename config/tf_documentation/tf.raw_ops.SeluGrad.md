# tf.raw_ops.SeluGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SeluGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SeluGrad)

---

Computes gradients for the scaled exponential linear (Selu) operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SeluGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SeluGrad)

```
tf.raw_ops.SeluGrad(
    gradients, outputs, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. The backpropagated gradients to the corresponding Selu operation. |
| `outputs` | A `Tensor`. Must have the same type as `gradients`. The outputs of the corresponding Selu operation. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `gradients`. | |