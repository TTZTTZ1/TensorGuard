# tf.raw_ops.StatefulStandardNormal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormal](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormal)

---

Outputs random values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatefulStandardNormal`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulStandardNormal)

```
tf.raw_ops.StatefulStandardNormal(
    resource,
    shape,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

This op is deprecated in favor of op 'StatefulStandardNormalV2'

The generated values will have mean 0 and standard deviation 1.

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. The handle of the resource variable that stores the state of the RNG. |
| `shape` | A `Tensor`. The shape of the output tensor. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Defaults to [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |