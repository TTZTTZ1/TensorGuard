# tf.raw_ops.TensorListScatter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatter](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatter)

---

Creates a TensorList by indexing into a Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListScatter`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatter)

```
tf.raw_ops.TensorListScatter(
    tensor, indices, element_shape, name=None
)
```

Each member of the TensorList corresponds to one row of the input tensor,
specified by the given index (see [`tf.gather`](https://tensorflow.google.cn/api_docs/python/tf/gather)).

tensor: The input tensor.
indices: The indices used to index into the list.
element\_shape: The shape of the elements in the list (can be less specified than
the shape of the tensor).
output\_handle: The TensorList.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. |
| `indices` | A `Tensor` of type `int32`. |
| `element_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |