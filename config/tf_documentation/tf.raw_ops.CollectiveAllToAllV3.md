# tf.raw_ops.CollectiveAllToAllV3

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveAllToAllV3](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveAllToAllV3)

---

Mutually exchanges multiple tensors of identical type and shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveAllToAllV3`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveAllToAllV3)

```
tf.raw_ops.CollectiveAllToAllV3(
    input, communicator, group_assignment, timeout_seconds=0, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`. |
| `communicator` | A `Tensor` of type `resource`. |
| `group_assignment` | A `Tensor` of type `int32`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |