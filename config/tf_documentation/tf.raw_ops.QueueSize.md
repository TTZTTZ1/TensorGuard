# tf.raw_ops.QueueSize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSize)

---

Computes the number of elements in the given queue.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QueueSize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueSize)

```
tf.raw_ops.QueueSize(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a queue. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |