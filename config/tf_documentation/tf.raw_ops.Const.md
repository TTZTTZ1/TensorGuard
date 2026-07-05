# tf.raw_ops.Const

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Const](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Const)

---

Returns a constant tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Const`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Const)

```
tf.raw_ops.Const(
    value, dtype, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `value` | A `tf.TensorProto`. Attr `value` is the tensor to return. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |