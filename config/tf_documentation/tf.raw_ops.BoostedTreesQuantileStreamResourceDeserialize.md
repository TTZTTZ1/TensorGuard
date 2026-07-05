# tf.raw_ops.BoostedTreesQuantileStreamResourceDeserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceDeserialize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceDeserialize)

---

Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BoostedTreesQuantileStreamResourceDeserialize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesQuantileStreamResourceDeserialize)

```
tf.raw_ops.BoostedTreesQuantileStreamResourceDeserialize(
    quantile_stream_resource_handle, bucket_boundaries, name=None
)
```

An op that deserializes bucket boundaries and are boundaries ready flag into current QuantileAccumulator.

| Args | |

|  |  |
| --- | --- |
| `quantile_stream_resource_handle` | A `Tensor` of type `resource`. resource handle referring to a QuantileStreamResource. |
| `bucket_boundaries` | A list of at least 1 `Tensor` objects with type `float32`. float; List of Rank 1 Tensors each containing the bucket boundaries for a feature. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |