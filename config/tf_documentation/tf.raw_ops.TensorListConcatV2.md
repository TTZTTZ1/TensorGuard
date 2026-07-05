# tf.raw_ops.TensorListConcatV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcatV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcatV2)

---

Concats all tensors in the list along the 0th dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListConcatV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcatV2)

```
tf.raw_ops.TensorListConcatV2(
    input_handle, element_shape, leading_dims, element_dtype, name=None
)
```

Requires that all tensors have the same shape except the first dimension.

input\_handle: The input list.
element\_shape: The shape of the uninitialized elements in the list. If the first
dimension is not -1, it is assumed that all list elements have the same
leading dim.
leading\_dims: The list of leading dims of uninitialized list elements. Used if
the leading dim of input\_handle.element\_shape or the element\_shape input arg
is not already set.
tensor: The concated result.
lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `element_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `leading_dims` | A `Tensor` of type `int64`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (tensor, lengths). | |
| `tensor` | A `Tensor` of type `element_dtype`. |
| `lengths` | A `Tensor` of type `int64`. |