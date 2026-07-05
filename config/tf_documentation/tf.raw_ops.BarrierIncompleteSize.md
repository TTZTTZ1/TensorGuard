# tf.raw_ops.BarrierIncompleteSize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierIncompleteSize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierIncompleteSize)

---

Computes the number of incomplete elements in the given barrier.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BarrierIncompleteSize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierIncompleteSize)

```
tf.raw_ops.BarrierIncompleteSize(
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