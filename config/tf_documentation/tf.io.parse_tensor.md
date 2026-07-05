# tf.io.parse_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor](https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor)

---

Transforms a serialized tensorflow.TensorProto proto into a Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.io.parse_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor), [`tf.compat.v1.parse_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor)

```
tf.io.parse_tensor(
    serialized: Annotated[Any, _atypes.String],
    out_type: TV_ParseTensor_out_type,
    name=None
) -> Annotated[Any, TV_ParseTensor_out_type]
```

| Args | |

|  |  |
| --- | --- |
| `serialized` | A `Tensor` of type `string`. A scalar string containing a serialized TensorProto proto. |
| `out_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the serialized tensor. The provided type must match the type of the serialized tensor and no implicit conversion will take place. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |