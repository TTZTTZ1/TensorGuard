# tf.raw_ops.ResourceGatherNd

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceGatherNd](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceGatherNd)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceGatherNd`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceGatherNd)

```
tf.raw_ops.ResourceGatherNd(
    resource, indices, dtype, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |