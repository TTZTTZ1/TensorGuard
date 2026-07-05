# tf.raw_ops.SparseSegmentMean

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentMean](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentMean)

---

Computes the mean along sparse segments of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSegmentMean`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentMean)

```
tf.raw_ops.SparseSegmentMean(
    data, indices, segment_ids, sparse_gradient=False, name=None
)
```

See [`tf.sparse.segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/sparse/segment_sum) for usage examples.

Like `SegmentMean`, but `segment_ids` can have rank less than `data`'s first
dimension, selecting a subset of dimension 0, specified by `indices`.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Has same rank as `segment_ids`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Values should be sorted and can be repeated. |
| `sparse_gradient` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |