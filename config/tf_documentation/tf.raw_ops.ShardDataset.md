# tf.raw_ops.ShardDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardDataset)

---

Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShardDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShardDataset)

```
tf.raw_ops.ShardDataset(
    input_dataset,
    num_shards,
    index,
    output_types,
    output_shapes,
    require_non_empty=False,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `num_shards` | A `Tensor` of type `int64`. An integer representing the number of shards operating in parallel. |
| `index` | A `Tensor` of type `int64`. An integer representing the current worker index. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `require_non_empty` | An optional `bool`. Defaults to `False`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |