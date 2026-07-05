# tf.math.unsorted_segment_sqrt_n

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sqrt_n](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sqrt_n)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L4527-L4582) |

Computes the sum along segments of a tensor divided by the sqrt(N).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.unsorted_segment_sqrt_n`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sqrt_n), [`tf.compat.v1.unsorted_segment_sqrt_n`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sqrt_n)

```
tf.math.unsorted_segment_sqrt_n(
    data, segment_ids, num_segments, name=None
)
```

Read [the section on
segmentation](https://tensorflow.google.cn/versions/r2.0/api_docs/python/tf/math#about_segmentation)
for an explanation of segments.

This operator is similar to the [`tf.math.unsorted_segment_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/unsorted_segment_sum) operator.
Additionally to computing the sum over segments, it divides the results by
sqrt(N).

\(output\_i = 1/sqrt(N\_i) \sum\_{j...} data[j...]\) where the sum is over
tuples `j...` such that `segment_ids[j...] == i` with \N\_i\ being the
number of occurrences of id \i\.

If there is no entry for a given segment ID `i`, it outputs 0.

Note that this op only supports floating point and complex dtypes,
due to tf.sqrt only supporting these types.

If the given segment ID `i` is negative, the value is dropped and will not
be added to the sum of the segment.

**Caution:** On CPU, values in `segment_ids` are always validated to be less than
`num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
result in safe but unspecified behavior, which may include ignoring
out-of-bound indices or outputting a tensor with a 0 stored in the first
dimension of its shape if `num_segments` is 0.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor` with floating point or complex dtype. |
| `segment_ids` | An integer tensor whose shape is a prefix of `data.shape`. The values must be in the range `[0, num_segments)`. The values are always validated to be in range on CPU, never validated on GPU. |
| `num_segments` | An integer scalar `Tensor`. The number of distinct segment IDs. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has same shape as data, except for the first `segment_ids.rank` dimensions, which are replaced with a single dimension which has size `num_segments`. | |