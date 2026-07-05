# tf.raw_ops.BoostedTreesFlushQuantileSummaries

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesFlushQuantileSummaries](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesFlushQuantileSummaries)

---

Flush the quantile summaries from each quantile stream resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BoostedTreesFlushQuantileSummaries`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesFlushQuantileSummaries)

```
tf.raw_ops.BoostedTreesFlushQuantileSummaries(
    quantile_stream_resource_handle, num_features, name=None
)
```

An op that outputs a list of quantile summaries of a quantile stream resource.
Each summary Tensor is rank 2, containing summaries (value, weight, min\_rank,
max\_rank) for a single feature.

| Args | |

|  |  |
| --- | --- |
| `quantile_stream_resource_handle` | A `Tensor` of type `resource`. resource handle referring to a QuantileStreamResource. |
| `num_features` | An `int` that is `>= 0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `num_features` `Tensor` objects with type `float32`. | |