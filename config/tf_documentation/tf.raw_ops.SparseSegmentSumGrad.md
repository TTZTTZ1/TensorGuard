# tf.raw_ops.SparseSegmentSumGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSumGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSumGrad)

---

Computes gradients for SparseSegmentSum.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSegmentSumGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSegmentSumGrad)

```
tf.raw_ops.SparseSegmentSumGrad(
    grad, indices, segment_ids, output_dim0, name=None
)
```

Returns tensor "output" with same shape as grad, except for dimension 0 whose
value is output\_dim0.

| Args | |

|  |  |
| --- | --- |
| `grad` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. gradient propagated to the SparseSegmentSum op. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. indices passed to the corresponding SparseSegmentSum op. |
| `segment_ids` | A `Tensor`. Must be one of the following types: `int32`, `int64`. segment\_ids passed to the corresponding SparseSegmentSum op. |
| `output_dim0` | A `Tensor` of type `int32`. dimension 0 of "data" passed to SparseSegmentSum op. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `grad`. | |