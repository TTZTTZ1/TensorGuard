# tf.raw_ops.TensorListGetItem

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGetItem](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGetItem)

---

Returns the item in the list with the given index.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListGetItem`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListGetItem)

```
tf.raw_ops.TensorListGetItem(
    input_handle, index, element_shape, element_dtype, name=None
)
```

input\_handle: the list
index: the position in the list from which an element will be retrieved
item: the element at that position

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `index` | A `Tensor` of type `int32`. |
| `element_shape` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `element_dtype`. | |