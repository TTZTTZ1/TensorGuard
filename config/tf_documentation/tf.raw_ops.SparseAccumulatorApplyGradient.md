# tf.raw_ops.SparseAccumulatorApplyGradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorApplyGradient](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorApplyGradient)

---

Applies a sparse gradient to a given accumulator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseAccumulatorApplyGradient`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseAccumulatorApplyGradient)

```
tf.raw_ops.SparseAccumulatorApplyGradient(
    handle,
    local_step,
    gradient_indices,
    gradient_values,
    gradient_shape,
    has_known_shape,
    name=None
)
```

Does not add if local\_step is smaller than the accumulator's
global\_step.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a accumulator. |
| `local_step` | A `Tensor` of type `int64`. The local\_step value at which the sparse gradient was computed. |
| `gradient_indices` | A `Tensor` of type `int64`. Indices of the sparse gradient to be accumulated. Must be a vector. |
| `gradient_values` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Values are the non-zero slices of the gradient, and must have the same first dimension as indices, i.e., the nnz represented by indices and values must be consistent. |
| `gradient_shape` | A `Tensor` of type `int64`. Shape of the sparse gradient to be accumulated. |
| `has_known_shape` | A `bool`. Boolean indicating whether gradient\_shape is unknown, in which case the input is ignored during validation. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |