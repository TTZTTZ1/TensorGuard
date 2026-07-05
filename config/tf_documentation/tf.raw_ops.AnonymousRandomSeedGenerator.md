# tf.raw_ops.AnonymousRandomSeedGenerator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousRandomSeedGenerator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousRandomSeedGenerator)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AnonymousRandomSeedGenerator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousRandomSeedGenerator)

```
tf.raw_ops.AnonymousRandomSeedGenerator(
    seed, seed2, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `seed` | A `Tensor` of type `int64`. |
| `seed2` | A `Tensor` of type `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (handle, deleter). | |
| `handle` | A `Tensor` of type `resource`. |
| `deleter` | A `Tensor` of type `variant`. |