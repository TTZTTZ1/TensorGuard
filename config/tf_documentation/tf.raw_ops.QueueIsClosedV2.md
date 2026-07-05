# tf.raw_ops.QueueIsClosedV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueIsClosedV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueIsClosedV2)

---

Returns true if queue is closed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QueueIsClosedV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueIsClosedV2)

```
tf.raw_ops.QueueIsClosedV2(
    handle, name=None
)
```

This operation returns true if the queue is closed and false if the queue
is open.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a queue. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |