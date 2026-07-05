# tf.math.unsorted_segment_min

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_min](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_min)

---

Computes the minimum along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.unsorted_segment_min`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_min), [`tf.compat.v1.unsorted_segment_min`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_min)

```
tf.math.unsorted_segment_min(
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

This operator is similar to [`tf.math.unsorted_segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum),
Instead of computing the sum over segments, it computes the minimum such that:

\(output\_i = \min\_{j...} data\_[j...]\) where min is over tuples `j...` such
that `segment_ids[j...] == i`.

If the minimum is empty for a given segment ID `i`, it outputs the largest
possible value for the specific numeric type,
`output[i] = numeric_limits<T>::max()`.

#### For example:

```
>>> c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])
>>> tf.math.unsorted_segment_min(c, tf.constant([0, 1, 0]), num_segments=2).numpy()
array([[1, 2, 2, 1],
       [5, 6, 7, 8]], dtype=int32)
```

If the given segment ID `i` is negative, then the corresponding value is
dropped, and will not be included in the result.

**Caution:** On CPU, values in `segment_ids` are always validated to be less than
`num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
result in safe but unspecified behavior, which may include ignoring
out-of-bound indices or outputting a tensor with a 0 stored in the first
dimension of its shape if `num_segments` is 0.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A tensor whose shape is a prefix of `data.shape`. The values must be less than `num_segments`. |

**Caution:** The values are always validated to be in range on CPU, never validated
on GPU.|  |  |
| --- | --- |
| `num_segments` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |