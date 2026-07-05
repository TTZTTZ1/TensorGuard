# tf.raw_ops.SnapshotDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetV2)

---

Creates a dataset that will write to / read from a snapshot.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SnapshotDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotDatasetV2)

```
tf.raw_ops.SnapshotDatasetV2(
    input_dataset,
    path,
    reader_func_other_args,
    shard_func_other_args,
    output_types,
    output_shapes,
    reader_func,
    shard_func,
    compression='',
    reader_prefix='',
    writer_prefix='',
    hash_valid=False,
    hash=0,
    metadata='',
    name=None
)
```

This dataset attempts to determine whether a valid snapshot exists at the
`snapshot_path`, and reads from the snapshot in lieu of using `input_dataset`.
If not, it will run the preprocessing pipeline as usual, and write out a
snapshot of the data processed for future use.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `path` | A `Tensor` of type `string`. The path we should write snapshots to / read snapshots from. |
| `reader_func_other_args` | A list of `Tensor` objects. |
| `shard_func_other_args` | A list of `Tensor` objects. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `reader_func` | A function decorated with @Defun. Optional. A function to control how to read data from snapshot shards. |
| `shard_func` | A function decorated with @Defun. Optional. A function to control how to shard data when writing a snapshot. |
| `compression` | An optional `string`. Defaults to `""`. The type of compression to be applied to the saved snapshot files. |
| `reader_prefix` | An optional `string`. Defaults to `""`. |
| `writer_prefix` | An optional `string`. Defaults to `""`. |
| `hash_valid` | An optional `bool`. Defaults to `False`. |
| `hash` | An optional `int`. Defaults to `0`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |