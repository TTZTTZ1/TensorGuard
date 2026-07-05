# tf.raw_ops.Softsign

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Softsign](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Softsign)

---

Computes softsign: `features / (abs(features) + 1)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Softsign`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Softsign)

```
tf.raw_ops.Softsign(
    features, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `features`. | |