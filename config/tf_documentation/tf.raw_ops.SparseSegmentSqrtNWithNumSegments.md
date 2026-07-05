# tf.raw_ops.SparseSegmentSqrtNWithNumSegments

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtNWithNumSegments](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtNWithNumSegments)

---

Computes the sum along sparse segments of a tensor divided by the sqrt of N.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSegmentSqrtNWithNumSegments`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSqrtNWithNumSegments)

```
tf.raw_ops.SparseSegmentSqrtNWithNumSegments(
    data, indices, segment_ids, num_segments, sparse_gradient=False, name=None
)
```

N is the size of the segment being reduced.

Like `SparseSegmentSqrtN`, but allows missing ids in `segment_ids`. If an id is
missing, the `output` tensor at that position will be zeroed.

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Has same rank as `segment_ids`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Values should be sorted and can be repeated. |
| `num_segments` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Should equal the number of distinct segment IDs. |
| `sparse_gradient` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |