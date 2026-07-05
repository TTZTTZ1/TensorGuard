# tf.raw_ops.TensorListConcat

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcat](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcat)

---

Concats all tensors in the list along the 0th dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListConcat`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListConcat)

```
tf.raw_ops.TensorListConcat(
    input_handle, element_dtype, element_shape=None, name=None
)
```

Requires that all tensors have the same shape except the first dimension.

input\_handle: The input list.
tensor: The concated result.
lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (tensor, lengths). | |
| `tensor` | A `Tensor` of type `element_dtype`. |
| `lengths` | A `Tensor` of type `int64`. |