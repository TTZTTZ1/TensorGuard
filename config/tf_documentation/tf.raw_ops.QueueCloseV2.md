# tf.raw_ops.QueueCloseV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueCloseV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueCloseV2)

---

Closes the given queue.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QueueCloseV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QueueCloseV2)

```
tf.raw_ops.QueueCloseV2(
    handle, cancel_pending_enqueues=False, name=None
)
```

This operation signals that no more elements will be enqueued in the
given queue. Subsequent Enqueue(Many) operations will fail.
Subsequent Dequeue(Many) operations will continue to succeed if
sufficient elements remain in the queue. Subsequent Dequeue(Many)
operations that would block will fail immediately.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a queue. |
| `cancel_pending_enqueues` | An optional `bool`. Defaults to `False`. If true, all pending enqueue requests that are blocked on the given queue will be canceled. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |