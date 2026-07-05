# tf.raw_ops.RetrieveTPUEmbeddingProximalAdagradParameters

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParameters](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParameters)

---

Retrieve proximal Adagrad embedding parameters.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RetrieveTPUEmbeddingProximalAdagradParameters`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParameters)

```
tf.raw_ops.RetrieveTPUEmbeddingProximalAdagradParameters(
    num_shards,
    shard_id,
    table_id=-1,
    table_name='',
    config='',
    name=None
)
```

An op that retrieves optimization parameters from embedding to host
memory. Must be preceded by a ConfigureTPUEmbeddingHost op that sets up
the correct embedding table configuration. For example, this op is
used to retrieve updated parameters before saving a checkpoint.

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
| A tuple of `Tensor` objects (parameters, accumulators). | |
| `parameters` | A `Tensor` of type `float32`. |
| `accumulators` | A `Tensor` of type `float32`. |