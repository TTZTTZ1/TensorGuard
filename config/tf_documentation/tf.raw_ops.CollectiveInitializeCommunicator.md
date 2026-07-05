# tf.raw_ops.CollectiveInitializeCommunicator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveInitializeCommunicator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveInitializeCommunicator)

---

Initializes a group for collective operations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveInitializeCommunicator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveInitializeCommunicator)

```
tf.raw_ops.CollectiveInitializeCommunicator(
    group_key,
    rank,
    group_size,
    communication_hint='auto',
    timeout_seconds=0,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `group_key` | A `Tensor` of type `int32`. |
| `rank` | A `Tensor` of type `int32`. |
| `group_size` | A `Tensor` of type `int32`. |
| `communication_hint` | An optional `string`. Defaults to `"auto"`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |