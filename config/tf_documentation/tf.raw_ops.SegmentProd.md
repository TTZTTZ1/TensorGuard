# tf.raw_ops.SegmentProd

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SegmentProd](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SegmentProd)

---

Computes the product along segments of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SegmentProd`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SegmentProd)

```
tf.raw_ops.SegmentProd(
    data, segment_ids, name=None
)
```

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

Computes a tensor such that
\(output\_i = \prod\_j data\_j\) where the product is over `j` such
that `segment_ids[j] == i`.

If the product is empty for a given segment ID `i`, `output[i] = 1`.

**Caution:** On CPU, values in `segment_ids` are always validated to be sorted,
and an error is thrown for indices that are not increasing. On GPU, this
does not throw an error for unsorted indices. On GPU, out-of-order indices
result in safe but unspecified behavior, which may include treating
out-of-order indices as the same as a smaller following index.

![](https://tensorflow.google.cn/images/SegmentProd.png)

#### For example:

```
>>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
>>> tf.math.segment_prod(c, tf.constant([0, 0, 1])).numpy()
array([[4, 6, 6, 4],
       [5, 6, 7, 8]], dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A 1-D tensor whose size is equal to the size of `data`'s first dimension. Values should be sorted and can be repeated. |

**Caution:** The values are always validated to be sorted on CPU, never validated
on GPU.|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |