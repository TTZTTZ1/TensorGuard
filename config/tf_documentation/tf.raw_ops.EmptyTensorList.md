# tf.raw_ops.EmptyTensorList

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EmptyTensorList](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EmptyTensorList)

---

Creates and returns an empty tensor list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.EmptyTensorList`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EmptyTensorList)

```
tf.raw_ops.EmptyTensorList(
    element_shape, max_num_elements, element_dtype, name=None
)
```

All list elements must be tensors of dtype element\_dtype and shape compatible
with element\_shape.

handle: an empty tensor list.
element\_dtype: the type of elements in the list.
element\_shape: a shape compatible with that of elements in the list.

| Args | |

|  |  |
| --- | --- |
| `element_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `max_num_elements` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |