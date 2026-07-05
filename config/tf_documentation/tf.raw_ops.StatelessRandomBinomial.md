# tf.raw_ops.StatelessRandomBinomial

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomBinomial](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomBinomial)

---

Outputs deterministic pseudorandom random numbers from a binomial distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatelessRandomBinomial`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatelessRandomBinomial)

```
tf.raw_ops.StatelessRandomBinomial(
    shape,
    seed,
    counts,
    probs,
    dtype=tf.dtypes.int64,
    name=None
)

tf.dtypes.int64
```

Outputs random values from a binomial distribution.

The outputs are a deterministic function of `shape`, `seed`, `counts`, and `probs`.

| Args | |

|  |  |
| --- | --- |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. The shape of the output tensor. |
| `seed` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 2 seeds (shape [2]). |
| `counts` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`. The counts of the binomial distribution. Must be broadcastable with `probs`, and broadcastable with the rightmost dimensions of `shape`. |
| `probs` | A `Tensor`. Must have the same type as `counts`. The probability of success for the binomial distribution. Must be broadcastable with `counts` and broadcastable with the rightmost dimensions of `shape`. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.half, tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |