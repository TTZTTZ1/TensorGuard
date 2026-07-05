# tf.raw_ops.SerializeTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeTensor)

---

Transforms a Tensor into a serialized TensorProto proto.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SerializeTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SerializeTensor)

```
tf.raw_ops.SerializeTensor(
    tensor, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. A Tensor of type `T`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |