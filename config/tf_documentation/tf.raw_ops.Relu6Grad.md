# tf.raw_ops.Relu6Grad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Relu6Grad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Relu6Grad)

---

Computes rectified linear 6 gradients for a Relu6 operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Relu6Grad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Relu6Grad)

```
tf.raw_ops.Relu6Grad(
    gradients, features, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. The backpropagated gradients to the corresponding Relu6 operation. |
| `features` | A `Tensor`. Must have the same type as `gradients`. The features passed as input to the corresponding Relu6 operation, or its output; using either one produces the same result. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `gradients`. | |