# tf.raw_ops.GetSessionTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetSessionTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetSessionTensor)

---

Get the value of the tensor specified by its handle.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GetSessionTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetSessionTensor)

```
tf.raw_ops.GetSessionTensor(
    handle, dtype, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `string`. The handle for a tensor stored in the session state. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the output value. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |