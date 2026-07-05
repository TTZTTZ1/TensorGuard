# tf.raw_ops.TensorListGather

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGather](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGather)

---

Creates a Tensor by indexing into the TensorList.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListGather`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGather)

```
tf.raw_ops.TensorListGather(
    input_handle, indices, element_shape, element_dtype, name=None
)
```

Each row in the produced Tensor corresponds to the element in the TensorList
specified by the given index (see [`tf.gather`](https://tensorflow.google.cn/api_docs/python/tf/gather)).

input\_handle: The input tensor list.
indices: The indices used to index into the list.
values: The tensor.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `indices` | A `Tensor` of type `int32`. |
| `element_shape` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `element_dtype`. | |