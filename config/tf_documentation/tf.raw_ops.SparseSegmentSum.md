# tf.raw_ops.SparseSegmentSum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSum](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSum)

---

Computes the sum along sparse segments of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSegmentSum`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSum)

```
tf.raw_ops.SparseSegmentSum(
    data, indices, segment_ids, sparse_gradient=False, name=None
)
```

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

Like `SegmentSum`, but `segment_ids` can have rank less than `data`'s first
dimension, selecting a subset of dimension 0, specified by `indices`.

#### For example:

```
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])

# Select two rows, one segment.
tf.sparse_segment_sum(c, tf.constant([0, 1]), tf.constant([0, 0]))
# => [[0 0 0 0]]

# Select two rows, two segment.
tf.sparse_segment_sum(c, tf.constant([0, 1]), tf.constant([0, 1]))
# => [[ 1  2  3  4]
#     [-1 -2 -3 -4]]

# Select all rows, two segments.
tf.sparse_segment_sum(c, tf.constant([0, 1, 2]), tf.constant([0, 0, 1]))
# => [[0 0 0 0]
#     [5 6 7 8]]

# Which is equivalent to:
tf.segment_sum(c, tf.constant([0, 0, 1]))
```

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Has same rank as `segment_ids`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor. Values should be sorted and can be repeated. |
| `sparse_gradient` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |