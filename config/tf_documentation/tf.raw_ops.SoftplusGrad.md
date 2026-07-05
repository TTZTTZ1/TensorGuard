# tf.raw_ops.SoftplusGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftplusGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftplusGrad)

---

Computes softplus gradients for a softplus operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SoftplusGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftplusGrad)

```
tf.raw_ops.SoftplusGrad(
    gradients, features, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. The backpropagated gradients to the corresponding softplus operation. |
| `features` | A `Tensor`. Must have the same type as `gradients`. The features passed as input to the corresponding softplus operation. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `gradients`. | |