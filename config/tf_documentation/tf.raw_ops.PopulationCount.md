# tf.raw_ops.PopulationCount

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PopulationCount](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PopulationCount)

---

Computes element-wise population count (a.k.a. popcount, bitsum, bitcount).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.PopulationCount`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PopulationCount)

```
tf.raw_ops.PopulationCount(
    x, name=None
)
```

For each entry in `x`, calculates the number of `1` (on) bits in the binary
representation of that entry.

**Note:** It is more efficient to first [`tf.bitcast`](https://tensorflow.google.cn/api_docs/python/tf/bitcast) your tensors into
`int32` or `int64` and perform the bitcount on the result, than to feed in
8- or 16-bit inputs and then aggregate the resulting counts.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `uint8`. | |