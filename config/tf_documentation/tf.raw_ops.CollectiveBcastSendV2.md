# tf.raw_ops.CollectiveBcastSendV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastSendV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastSendV2)

---

Broadcasts a tensor value to one or more other devices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveBcastSendV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastSendV2)

```
tf.raw_ops.CollectiveBcastSendV2(
    input,
    group_size,
    group_key,
    instance_key,
    communication_hint='auto',
    timeout_seconds=0,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bool`, `float32`, `half`, `float64`, `int32`, `int64`. |
| `group_size` | A `Tensor` of type `int32`. |
| `group_key` | A `Tensor` of type `int32`. |
| `instance_key` | A `Tensor` of type `int32`. |
| `communication_hint` | An optional `string`. Defaults to `"auto"`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |