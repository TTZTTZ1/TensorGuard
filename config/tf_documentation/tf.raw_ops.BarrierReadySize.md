# tf.raw_ops.BarrierReadySize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierReadySize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierReadySize)

---

Computes the number of complete elements in the given barrier.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BarrierReadySize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierReadySize)

```
tf.raw_ops.BarrierReadySize(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a barrier. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |