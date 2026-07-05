# tf.raw_ops.SparseSegmentSqrtN

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtN](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtN)

---

Computes the sum along sparse segments of a tensor divided by the sqrt of N.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSegmentSqrtN`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtN)

```
tf.raw_ops.SparseSegmentSqrtN(
    data, indices, segment_ids, sparse_gradient=False, name=None
)
```

N is the size of the segment being reduced.

See [`tf.sparse.segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/sparse/segment_sum) for usage examples.

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