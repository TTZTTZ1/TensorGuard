# tf.raw_ops.GuaranteeConst

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GuaranteeConst](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GuaranteeConst)

---

Gives a guarantee to the TF runtime that the input tensor is a constant.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GuaranteeConst`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GuaranteeConst)

```
tf.raw_ops.GuaranteeConst(
    input, name=None
)
```

The runtime is then free to make optimizations based on this.

Only accepts value typed tensors as inputs and rejects resource variable handles
as input.

Returns the input tensor without modification.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |