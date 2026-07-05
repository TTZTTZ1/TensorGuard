# tf.raw_ops.StackPush

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPush](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPush)

---

Deprecated, use StackPushV2.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StackPush`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPush)

```
tf.raw_ops.StackPush(
    handle, elem, swap_memory=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `elem` | A `Tensor`. |
| `swap_memory` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `elem`. | |