# tf.raw_ops.StatelessRandomPoisson

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomPoisson](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomPoisson)

---

Outputs deterministic pseudorandom random numbers from a Poisson distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatelessRandomPoisson`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomPoisson)

```
tf.raw_ops.StatelessRandomPoisson(
    shape, seed, lam, dtype, name=None
)
```

Outputs random values from a Poisson distribution.

The outputs are a deterministic function of `shape`, `seed`, and `lam`.

| Args | |

|  |  |
| --- | --- |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. The shape of the output tensor. |
| `seed` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 2 seeds (shape [2]). |
| `lam` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`. The rate of the Poisson distribution. Shape must match the rightmost dimensions of `shape`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.half, tf.float32, tf.float64, tf.int32, tf.int64`. The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |