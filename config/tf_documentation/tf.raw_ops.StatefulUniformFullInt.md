# tf.raw_ops.StatefulUniformFullInt

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulUniformFullInt](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulUniformFullInt)

---

Outputs random integers from a uniform distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StatefulUniformFullInt`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StatefulUniformFullInt)

```
tf.raw_ops.StatefulUniformFullInt(
    resource,
    algorithm,
    shape,
    dtype=tf.dtypes.uint64,
    name=None
)

tf.dtypes.uint64
```

The generated values are uniform integers covering the whole range of `dtype`.

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. The handle of the resource variable that stores the state of the RNG. |
| `algorithm` | A `Tensor` of type `int64`. The RNG algorithm. |
| `shape` | A `Tensor`. The shape of the output tensor. |
| `dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Defaults to [`tf.uint64`](https://tensorflow.google.cn/api_docs/python/tf#uint64). The type of the output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |