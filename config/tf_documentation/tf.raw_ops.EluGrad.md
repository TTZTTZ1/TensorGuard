# tf.raw_ops.EluGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EluGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EluGrad)

---

Computes gradients for the exponential linear (Elu) operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.EluGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EluGrad)

```
tf.raw_ops.EluGrad(
    gradients, outputs, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. The backpropagated gradients to the corresponding Elu operation. |
| `outputs` | A `Tensor`. Must have the same type as `gradients`. The outputs of the corresponding Elu operation. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `gradients`. | |