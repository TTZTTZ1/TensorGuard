# tf.raw_ops.QueueSizeV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSizeV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSizeV2)

---

Computes the number of elements in the given queue.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QueueSizeV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSizeV2)

```
tf.raw_ops.QueueSizeV2(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a queue. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |