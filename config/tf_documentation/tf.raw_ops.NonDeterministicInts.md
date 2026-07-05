# tf.raw_ops.NonDeterministicInts

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonDeterministicInts](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonDeterministicInts)

---

Non-deterministically generates some integers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NonDeterministicInts`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonDeterministicInts)

```
tf.raw_ops.NonDeterministicInts(
    shape,
    dtype=tf.dtypes.int64,
    name=None
)

tf.dtypes.int64
```

This op may use some OS-provided source of non-determinism (e.g. an RNG), so each execution will give different results.

| Args | |

|  |  |
| --- | --- |
| `shape` | A `Tensor`. The shape of the output tensor. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |