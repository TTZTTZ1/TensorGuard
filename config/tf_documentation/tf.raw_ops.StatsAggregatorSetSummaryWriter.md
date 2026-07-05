# tf.raw_ops.StatsAggregatorSetSummaryWriter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatsAggregatorSetSummaryWriter](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatsAggregatorSetSummaryWriter)

---

Set a summary\_writer\_interface to record statistics using given stats\_aggregator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatsAggregatorSetSummaryWriter`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatsAggregatorSetSummaryWriter)

```
tf.raw_ops.StatsAggregatorSetSummaryWriter(
    stats_aggregator, summary, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `stats_aggregator` | A `Tensor` of type `resource`. |
| `summary` | A `Tensor` of type `resource`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |