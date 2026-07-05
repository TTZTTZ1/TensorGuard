# tf.raw_ops.TensorArrayWrite

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWrite](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWrite)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayWrite`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWrite)

```
tf.raw_ops.TensorArrayWrite(
    handle, index, value, flow_in, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `index` | A `Tensor` of type `int32`. |
| `value` | A `Tensor`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |