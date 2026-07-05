# tf.raw_ops.StatelessRandomGetKeyCounter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetKeyCounter](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetKeyCounter)

---

Scrambles seed into key and counter, using the best algorithm based on device.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatelessRandomGetKeyCounter`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomGetKeyCounter)

```
tf.raw_ops.StatelessRandomGetKeyCounter(
    seed, name=None
)
```

This op scrambles a shape-[2] seed into a key and a counter, both needed by counter-based RNG algorithms. The scrambing uses the best algorithm based on device. The scrambling is opaque but approximately satisfies the property that different seed results in different key/counter pair (which will in turn result in different random numbers).

| Args | |

|  |  |
| --- | --- |
| `seed` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 2 seeds (shape [2]). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (key, counter). | |
| `key` | A `Tensor` of type `uint64`. |
| `counter` | A `Tensor` of type `uint64`. |