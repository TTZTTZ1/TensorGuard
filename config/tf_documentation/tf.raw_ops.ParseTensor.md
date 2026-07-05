# tf.raw_ops.ParseTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseTensor)

---

Transforms a serialized tensorflow.TensorProto proto into a Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ParseTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseTensor)

```
tf.raw_ops.ParseTensor(
    serialized, out_type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `serialized` | A `Tensor` of type `string`. A scalar string containing a serialized TensorProto proto. |
| `out_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the serialized tensor. The provided type must match the type of the serialized tensor and no implicit conversion will take place. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |