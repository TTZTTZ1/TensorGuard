# tf.raw_ops.TensorArraySplit

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySplit](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySplit)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArraySplit`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySplit)

```
tf.raw_ops.TensorArraySplit(
    handle, value, lengths, flow_in, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `value` | A `Tensor`. |
| `lengths` | A `Tensor` of type `int64`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |