# tf.raw_ops.EnsureShape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnsureShape](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnsureShape)

---

Ensures that the tensor's shape matches the expected shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.EnsureShape`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnsureShape)

```
tf.raw_ops.EnsureShape(
    input, shape, name=None
)
```

Raises an error if the input tensor's shape does not match the specified shape.
Returns the input tensor otherwise.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. A tensor, whose shape is to be validated. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The expected (possibly partially specified) shape of the input tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |