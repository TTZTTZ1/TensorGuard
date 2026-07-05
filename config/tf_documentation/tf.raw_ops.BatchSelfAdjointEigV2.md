# tf.raw_ops.BatchSelfAdjointEigV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSelfAdjointEigV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSelfAdjointEigV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BatchSelfAdjointEigV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSelfAdjointEigV2)

```
tf.raw_ops.BatchSelfAdjointEigV2(
    input, compute_v=True, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`. |
| `compute_v` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (e, v). | |
| `e` | A `Tensor`. Has the same type as `input`. |
| `v` | A `Tensor`. Has the same type as `input`. |