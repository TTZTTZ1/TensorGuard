# tf.raw_ops.ShardedFilename

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardedFilename](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardedFilename)

---

Generate a sharded filename.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShardedFilename`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardedFilename)

```
tf.raw_ops.ShardedFilename(
    basename, shard, num_shards, name=None
)
```

The filename is printf formatted as

%s-%05d-of-%05d, basename, shard, num\_shards.

| Args | |

|  |  |
| --- | --- |
| `basename` | A `Tensor` of type `string`. |
| `shard` | A `Tensor` of type `int32`. |
| `num_shards` | A `Tensor` of type `int32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |