# tf.raw_ops.StatelessRandomUniformFullInt

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomUniformFullInt](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomUniformFullInt)

---

Outputs deterministic pseudorandom random integers from a uniform distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatelessRandomUniformFullInt`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomUniformFullInt)

```
tf.raw_ops.StatelessRandomUniformFullInt(
    shape,
    seed,
    dtype=tf.dtypes.uint64,
    name=None
)

tf.dtypes.uint64
```

The generated values are uniform integers covering the whole range of `dtype`.

The outputs are a deterministic function of `shape` and `seed`.

| Args | |

|  |  |
| --- | --- |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. The shape of the output tensor. |
| `seed` | A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint32`, `uint64`. 2 seeds (shape [2]). |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to [`tf.uint64`](https://tensorflow.google.cn/api_docs/python/tf#uint64). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |