# tf.raw_ops.TensorArrayWriteV3

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWriteV3](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWriteV3)

---

Push an element onto the tensor\_array.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayWriteV3`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayWriteV3)

```
tf.raw_ops.TensorArrayWriteV3(
    handle, index, value, flow_in, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a TensorArray. |
| `index` | A `Tensor` of type `int32`. The position to write to inside the TensorArray. |
| `value` | A `Tensor`. The tensor to write to the TensorArray. |
| `flow_in` | A `Tensor` of type `float32`. A float scalar that enforces proper chaining of operations. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |