# tf.raw_ops.RefNextIteration

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefNextIteration](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefNextIteration)

---

Makes its input available to the next iteration.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RefNextIteration`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefNextIteration)

```
tf.raw_ops.RefNextIteration(
    data, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `data` | A mutable `Tensor`. The tensor to be made available to the next iteration. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor`. Has the same type as `data`. | |