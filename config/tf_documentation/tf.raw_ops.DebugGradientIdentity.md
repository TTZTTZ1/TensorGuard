# tf.raw_ops.DebugGradientIdentity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugGradientIdentity](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugGradientIdentity)

---

Identity op for gradient debugging.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DebugGradientIdentity`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugGradientIdentity)

```
tf.raw_ops.DebugGradientIdentity(
    input, name=None
)
```

This op is hidden from public in Python. It is used by TensorFlow Debugger to
register gradient tensors for gradient debugging.
This op operates on non-reference-type tensors.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |