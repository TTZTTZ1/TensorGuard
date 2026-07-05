# tf.raw_ops.CollectivePermute

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectivePermute](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectivePermute)

---

An Op to permute tensors across replicated TPU instances.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectivePermute`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectivePermute)

```
tf.raw_ops.CollectivePermute(
    input, source_target_pairs, name=None
)
```

Each instance supplies its own input.

For example, suppose there are 4 TPU instances: `[A, B, C, D]`. Passing
source\_target\_pairs=`[[0,1],[1,2],[2,3],[3,0]]` gets the outputs:
`[D, A, B, C]`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. The local input to be permuted. Currently only supports float and bfloat16. |
| `source_target_pairs` | A `Tensor` of type `int32`. A tensor with shape [num\_pairs, 2]. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |