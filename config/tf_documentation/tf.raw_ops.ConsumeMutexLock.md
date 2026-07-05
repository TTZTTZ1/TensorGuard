# tf.raw_ops.ConsumeMutexLock

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConsumeMutexLock](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConsumeMutexLock)

---

This op consumes a lock created by `MutexLock`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ConsumeMutexLock`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConsumeMutexLock)

```
tf.raw_ops.ConsumeMutexLock(
    mutex_lock, name=None
)
```

This op exists to consume a tensor created by `MutexLock` (other than
direct control dependencies). It should be the only that consumes the tensor,
and will raise an error if it is not. Its only purpose is to keep the
mutex lock tensor alive until it is consumed by this op.

**Note:** This operation must run on the same device as its input. This may
be enforced via the `colocate_with` mechanism.

| Args | |

|  |  |
| --- | --- |
| `mutex_lock` | A `Tensor` of type `variant`. A tensor returned by `MutexLock`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |