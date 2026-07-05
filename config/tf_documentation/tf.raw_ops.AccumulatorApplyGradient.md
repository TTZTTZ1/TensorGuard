# tf.raw_ops.AccumulatorApplyGradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorApplyGradient](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorApplyGradient)

---

Applies a gradient to a given accumulator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AccumulatorApplyGradient`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorApplyGradient)

```
tf.raw_ops.AccumulatorApplyGradient(
    handle, local_step, gradient, name=None
)
```

Does not add if local\_step is lesser than the accumulator's global\_step.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a accumulator. |
| `local_step` | A `Tensor` of type `int64`. The local\_step value at which the gradient was computed. |
| `gradient` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. A tensor of the gradient to be accumulated. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |