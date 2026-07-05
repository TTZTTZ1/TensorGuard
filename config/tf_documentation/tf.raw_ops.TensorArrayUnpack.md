# tf.raw_ops.TensorArrayUnpack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayUnpack](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayUnpack)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayUnpack`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayUnpack)

```
tf.raw_ops.TensorArrayUnpack(
    handle, value, flow_in, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `value` | A `Tensor`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |