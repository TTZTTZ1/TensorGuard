# tf.raw_ops.RetrieveTPUEmbeddingProximalYogiParameters

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalYogiParameters](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalYogiParameters)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RetrieveTPUEmbeddingProximalYogiParameters`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalYogiParameters)

```
tf.raw_ops.RetrieveTPUEmbeddingProximalYogiParameters(
    num_shards,
    shard_id,
    table_id=-1,
    table_name='',
    config='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `num_shards` | An `int`. |
| `shard_id` | An `int`. |
| `table_id` | An optional `int`. Defaults to `-1`. |
| `table_name` | An optional `string`. Defaults to `""`. |
| `config` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (parameters, v, m). | |
| `parameters` | A `Tensor` of type `float32`. |
| `v` | A `Tensor` of type `float32`. |
| `m` | A `Tensor` of type `float32`. |