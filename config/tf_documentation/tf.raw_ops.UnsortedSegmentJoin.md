# tf.raw_ops.UnsortedSegmentJoin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnsortedSegmentJoin](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnsortedSegmentJoin)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.UnsortedSegmentJoin`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnsortedSegmentJoin)

```
tf.raw_ops.UnsortedSegmentJoin(
    inputs, segment_ids, num_segments, separator='', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A `Tensor` of type `string`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `num_segments` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `separator` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |