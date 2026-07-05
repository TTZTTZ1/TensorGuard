# tf.raw_ops.TensorArraySizeV3

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySizeV3](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySizeV3)

---

Get the current size of the TensorArray.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArraySizeV3`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArraySizeV3)

```
tf.raw_ops.TensorArraySizeV3(
    handle, flow_in, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a TensorArray (output of TensorArray or TensorArrayGrad). |
| `flow_in` | A `Tensor` of type `float32`. A float scalar that enforces proper chaining of operations. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |