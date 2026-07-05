# tf.raw_ops.StatefulRandomBinomial

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulRandomBinomial](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulRandomBinomial)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatefulRandomBinomial`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulRandomBinomial)

```
tf.raw_ops.StatefulRandomBinomial(
    resource,
    algorithm,
    shape,
    counts,
    probs,
    dtype=tf.dtypes.int64,
    name=None
)

tf.dtypes.int64
```

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. |
| `algorithm` | A `Tensor` of type `int64`. |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `counts` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`. |
| `probs` | A `Tensor`. Must have the same type as `counts`. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.half, tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |