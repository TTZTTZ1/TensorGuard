# tf.raw_ops.ParallelBatchDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParallelBatchDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParallelBatchDataset)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ParallelBatchDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParallelBatchDataset)

```
tf.raw_ops.ParallelBatchDataset(
    input_dataset,
    batch_size,
    num_parallel_calls,
    drop_remainder,
    output_types,
    output_shapes,
    parallel_copy=False,
    deterministic='default',
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `batch_size` | A `Tensor` of type `int64`. |
| `num_parallel_calls` | A `Tensor` of type `int64`. |
| `drop_remainder` | A `Tensor` of type `bool`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `parallel_copy` | An optional `bool`. Defaults to `False`. |
| `deterministic` | An optional `string`. Defaults to `"default"`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |