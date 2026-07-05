# tf.raw_ops.CheckNumericsV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CheckNumericsV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CheckNumericsV2)

---

Checks a tensor for NaN, -Inf and +Inf values.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CheckNumericsV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CheckNumericsV2)

```
tf.raw_ops.CheckNumericsV2(
    tensor, message, name=None
)
```

When run, reports an `InvalidArgument` error if `tensor` has any values
that are not a number (NaN) or infinity (Inf). Otherwise, returns the input
tensor. Unlike CheckNumerics (V1), CheckNumericsV2 distinguishes -Inf and +Inf
in the errors it throws.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `message` | A `string`. Prefix of the error message. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `tensor`. | |