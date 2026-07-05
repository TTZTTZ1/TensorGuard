# tf.raw_ops.StatelessRandomGetAlg

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetAlg](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetAlg)

---

Picks the best counter-based RNG algorithm based on device.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatelessRandomGetAlg`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetAlg)

```
tf.raw_ops.StatelessRandomGetAlg(
    name=None
)
```

This op picks the best counter-based RNG algorithm based on device.

| Args | |

|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |