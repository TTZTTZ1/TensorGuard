# tf.raw_ops.AllToAll

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AllToAll](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AllToAll)

---

An Op to exchange data across TPU replicas.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AllToAll`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AllToAll)

```
tf.raw_ops.AllToAll(
    input,
    group_assignment,
    concat_dimension,
    split_dimension,
    split_count,
    name=None
)
```

On each replica, the input is split into `split_count` blocks along
`split_dimension` and send to the other replicas given group\_assignment. After
receiving `split_count` - 1 blocks from other replicas, we concatenate the
blocks along `concat_dimension` as the output.

For example, suppose there are 2 TPU replicas:
replica 0 receives input: `[[A, B]]`
replica 1 receives input: `[[C, D]]`

group\_assignment=`[[0, 1]]`
concat\_dimension=0
split\_dimension=1
split\_count=2

replica 0's output: `[[A], [C]]`
replica 1's output: `[[B], [D]]`

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`. The local input to the sum. |
| `group_assignment` | A `Tensor` of type `int32`. An int32 tensor with shape [num\_groups, num\_replicas\_per\_group]. `group_assignment[i]` represents the replica ids in the ith subgroup. |
| `concat_dimension` | An `int`. The dimension number to concatenate. |
| `split_dimension` | An `int`. The dimension number to split. |
| `split_count` | An `int`. The number of splits, this number must equal to the sub-group size(group\_assignment.get\_shape()[1]) |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |