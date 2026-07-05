# tf.raw_ops.TensorListScatterIntoExistingList

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatterIntoExistingList](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatterIntoExistingList)

---

Scatters tensor at indices in an input list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListScatterIntoExistingList`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListScatterIntoExistingList)

```
tf.raw_ops.TensorListScatterIntoExistingList(
    input_handle, tensor, indices, name=None
)
```

Each member of the TensorList corresponds to one row of the input tensor,
specified by the given index (see [`tf.gather`](https://tensorflow.google.cn/api_docs/python/tf/gather)).

input\_handle: The list to scatter into.
tensor: The input tensor.
indices: The indices used to index into the list.
output\_handle: The TensorList.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `tensor` | A `Tensor`. |
| `indices` | A `Tensor` of type `int32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |