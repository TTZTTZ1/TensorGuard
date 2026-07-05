# tf.raw_ops.InfeedDequeue

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedDequeue](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedDequeue)

---

A placeholder op for a value that will be fed into the computation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.InfeedDequeue`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedDequeue)

```
tf.raw_ops.InfeedDequeue(
    dtype, shape, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of elements in the tensor. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The shape of the tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |