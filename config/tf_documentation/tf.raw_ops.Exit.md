# tf.raw_ops.Exit

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Exit](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Exit)

---

Exits the current frame to its parent frame.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Exit`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Exit)

```
tf.raw_ops.Exit(
    data, name=None
)
```

Exit makes its input `data` available to the parent frame.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. The tensor to be made available to the parent frame. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |