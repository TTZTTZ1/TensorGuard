# tf.raw_ops.AccumulateNV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulateNV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulateNV2)

---

Returns the element-wise sum of a list of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AccumulateNV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulateNV2)

```
tf.raw_ops.AccumulateNV2(
    inputs, shape, name=None
)
```

`tf.accumulate_n_v2` performs the same operation as [`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n), but does not
wait for all of its inputs to be ready before beginning to sum. This can
save memory if inputs are ready at different times, since minimum temporary
storage is proportional to the output size rather than the inputs size.

Unlike the original `accumulate_n`, `accumulate_n_v2` is differentiable.

Returns a `Tensor` of same shape and type as the elements of `inputs`.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. A list of `Tensor` objects, each with same shape and type. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Shape of elements of `inputs`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `inputs`. | |