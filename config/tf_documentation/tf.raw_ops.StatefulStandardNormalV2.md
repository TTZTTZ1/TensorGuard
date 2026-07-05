# tf.raw_ops.StatefulStandardNormalV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormalV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormalV2)

---

Outputs random values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatefulStandardNormalV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormalV2)

```
tf.raw_ops.StatefulStandardNormalV2(
    resource,
    algorithm,
    shape,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

The generated values will have mean 0 and standard deviation 1.

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