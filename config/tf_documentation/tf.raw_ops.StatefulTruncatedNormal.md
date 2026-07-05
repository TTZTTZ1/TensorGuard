# tf.raw_ops.StatefulTruncatedNormal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulTruncatedNormal](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulTruncatedNormal)

---

Outputs random values from a truncated normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatefulTruncatedNormal`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulTruncatedNormal)

```
tf.raw_ops.StatefulTruncatedNormal(
    resource,
    algorithm,
    shape,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

The generated values follow a normal distribution with mean 0 and standard
deviation 1, except that values whose magnitude is more than 2 standard
deviations from the mean are dropped and re-picked.

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. The handle of the resource variable that stores the state of the RNG. |
| `algorithm` | A `Tensor` of type `int64`. The RNG algorithm. |
| `shape` | A `Tensor`. The shape of the output tensor. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Defaults to [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |