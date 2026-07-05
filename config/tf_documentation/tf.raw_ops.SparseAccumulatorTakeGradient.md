# tf.raw_ops.SparseAccumulatorTakeGradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorTakeGradient](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorTakeGradient)

---

Extracts the average sparse gradient in a SparseConditionalAccumulator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseAccumulatorTakeGradient`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorTakeGradient)

```
tf.raw_ops.SparseAccumulatorTakeGradient(
    handle, num_required, dtype, name=None
)
```

The op will blocks until sufficient (i.e., more than num\_required)
gradients have been accumulated. If the accumulator has already
aggregated more than num\_required gradients, it will return its
average of the accumulated gradients. Also automatically increments
the recorded global\_step in the accumulator by 1, and resets the
aggregate to 0.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a SparseConditionalAccumulator. |
| `num_required` | A `Tensor` of type `int32`. Number of gradients required before we return an aggregate. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.int32, tf.uint8, tf.int16, tf.int8, tf.complex64, tf.int64, tf.qint8, tf.quint8, tf.qint32, tf.bfloat16, tf.qint16, tf.quint16, tf.uint16, tf.complex128, tf.half, tf.uint32, tf.uint64`. The data type of accumulated gradients. Needs to correspond to the type of the accumulator. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (indices, values, shape). | |
| `indices` | A `Tensor` of type `int64`. |
| `values` | A `Tensor` of type `dtype`. |
| `shape` | A `Tensor` of type `int64`. |