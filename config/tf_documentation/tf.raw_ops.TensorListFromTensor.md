# tf.raw_ops.TensorListFromTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListFromTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListFromTensor)

---

Creates a TensorList which, when stacked, has the value of `tensor`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListFromTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListFromTensor)

```
tf.raw_ops.TensorListFromTensor(
    tensor, element_shape, name=None
)
```

Each tensor in the result list corresponds to one row of the input tensor.

tensor: The input tensor.
output\_handle: The list.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. |
| `element_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |