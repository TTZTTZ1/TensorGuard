# tf.raw_ops.SnapshotDatasetReader

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetReader](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetReader)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SnapshotDatasetReader`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetReader)

```
tf.raw_ops.SnapshotDatasetReader(
    shard_dir,
    start_index,
    output_types,
    output_shapes,
    version,
    compression='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `shard_dir` | A `Tensor` of type `string`. |
| `start_index` | A `Tensor` of type `int64`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `version` | An `int`. |
| `compression` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |