# tf.raw_ops.WorkerHeartbeat

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WorkerHeartbeat](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WorkerHeartbeat)

---

Worker heartbeat op.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.WorkerHeartbeat`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WorkerHeartbeat)

```
tf.raw_ops.WorkerHeartbeat(
    request, name=None
)
```

Heartbeats may be sent periodically to indicate the coordinator is still active,
to retrieve the current worker status and to expedite shutdown when necessary.

| Args | |

|  |  |
| --- | --- |
| `request` | A `Tensor` of type `string`. A string tensor containing a serialized WorkerHeartbeatRequest |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |