# tf.raw_ops.CollectiveBcastRecvV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastRecvV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastRecvV2)

---

Receives a tensor value broadcast from another device.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveBcastRecvV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveBcastRecvV2)

```
tf.raw_ops.CollectiveBcastRecvV2(
    group_size,
    group_key,
    instance_key,
    shape,
    T,
    communication_hint='auto',
    timeout_seconds=0,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `group_size` | A `Tensor` of type `int32`. |
| `group_key` | A `Tensor` of type `int32`. |
| `instance_key` | A `Tensor` of type `int32`. |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `T` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.bool, tf.float32, tf.half, tf.float64, tf.int32, tf.int64`. |
| `communication_hint` | An optional `string`. Defaults to `"auto"`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `T`. | |