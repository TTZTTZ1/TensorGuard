# tf.math.unsorted_segment_sum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum)

---

Computes the sum along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.unsorted_segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum), [`tf.compat.v1.unsorted_segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum)

```
tf.math.unsorted_segment_sum(
    data: Annotated[Any, tf.raw_ops.Any],
    segment_ids: Annotated[Any, tf.raw_ops.Any],
    num_segments: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

Computes a tensor such that
\(output[i] = \sum\_{j...} data[j...]\) where the sum is over tuples `j...` such
that `segment_ids[j...] == i`. Unlike `SegmentSum`, `segment_ids`
need not be sorted and need not cover all values in the full
range of valid values.

If the sum is empty for a given segment ID `i`, `output[i] = 0`.
If the given segment ID `i` is negative, the value is dropped and will not be
added to the sum of the segment.

`num_segments` should equal the number of distinct segment IDs.

**Caution:** On CPU, values in `segment_ids` are always validated to be less than
`num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
result in safe but unspecified behavior, which may include ignoring
out-of-bound indices or outputting a tensor with a 0 stored in the first
dimension of its shape if `num_segments` is 0.

![](https://tensorflow.google.cn/images/UnsortedSegmentSum.png)

```
>>> c = [[1,2,3,4], [5,6,7,8], [4,3,2,1]]
>>> tf.math.unsorted_segment_sum(c, [0, 1, 0], num_segments=2).numpy()
array([[5, 5, 5, 5],
       [5, 6, 7, 8]], dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. A tensor whose shape is a prefix of `data.shape`. The values must be less than `num_segments`. |

**Caution:** The values are always validated to be in range on CPU, never validated
on GPU.|  |  |
| --- | --- |
| `num_segments` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |