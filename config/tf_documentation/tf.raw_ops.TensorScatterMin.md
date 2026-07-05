# tf.raw_ops.TensorScatterMin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorScatterMin](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorScatterMin)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorScatterMin`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorScatterMin)

```
tf.raw_ops.TensorScatterMin(
    tensor, indices, updates, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. Tensor to update. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `updates` | A `Tensor`. Must have the same type as `tensor`. Updates to scatter into output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `tensor`. | |