# tf.raw_ops.ExperimentalLatencyStatsDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalLatencyStatsDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalLatencyStatsDataset)

---

Records the latency of producing `input_dataset` elements in a StatsAggregator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ExperimentalLatencyStatsDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalLatencyStatsDataset)

```
tf.raw_ops.ExperimentalLatencyStatsDataset(
    input_dataset, tag, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `tag` | A `Tensor` of type `string`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |