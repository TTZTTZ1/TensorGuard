# tf.raw_ops.NextIteration

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextIteration](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextIteration)

---

Makes its input available to the next iteration.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NextIteration`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextIteration)

```
tf.raw_ops.NextIteration(
    data, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. The tensor to be made available to the next iteration. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `data`. | |