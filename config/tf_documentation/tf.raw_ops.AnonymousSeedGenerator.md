# tf.raw_ops.AnonymousSeedGenerator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousSeedGenerator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousSeedGenerator)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AnonymousSeedGenerator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousSeedGenerator)

```
tf.raw_ops.AnonymousSeedGenerator(
    seed, seed2, reshuffle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `seed` | A `Tensor` of type `int64`. |
| `seed2` | A `Tensor` of type `int64`. |
| `reshuffle` | A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (handle, deleter). | |
| `handle` | A `Tensor` of type `resource`. |
| `deleter` | A `Tensor` of type `variant`. |