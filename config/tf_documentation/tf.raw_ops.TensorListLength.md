# tf.raw_ops.TensorListLength

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListLength](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListLength)

---

Returns the number of tensors in the input tensor list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListLength`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListLength)

```
tf.raw_ops.TensorListLength(
    input_handle, name=None
)
```

input\_handle: the input list
length: the number of tensors in the list

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |