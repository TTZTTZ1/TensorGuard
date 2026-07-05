# tf.raw_ops.Xdivy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xdivy](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xdivy)

---

Returns 0 if x == 0, and x / y otherwise, elementwise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Xdivy`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Xdivy)

```
tf.raw_ops.Xdivy(
    x, y, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |