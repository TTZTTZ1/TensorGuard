# tf.raw_ops.TensorListPopBack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPopBack](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPopBack)

---

Returns the last element of the input list as well as a list with all but that element.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListPopBack`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPopBack)

```
tf.raw_ops.TensorListPopBack(
    input_handle, element_shape, element_dtype, name=None
)
```

Fails if the list is empty.

input\_handle: the input list
tensor: the withdrawn last element of the list
element\_dtype: the type of elements in the list
element\_shape: the shape of the output tensor

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `element_shape` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_handle, tensor). | |
| `output_handle` | A `Tensor` of type `variant`. |
| `tensor` | A `Tensor` of type `element_dtype`. |