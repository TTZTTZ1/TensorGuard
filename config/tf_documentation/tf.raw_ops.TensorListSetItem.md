# tf.raw_ops.TensorListSetItem

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListSetItem](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListSetItem)

---

Sets the index-th position of the list to contain the given tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListSetItem`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListSetItem)

```
tf.raw_ops.TensorListSetItem(
    input_handle, index, item, resize_if_index_out_of_bounds=False, name=None
)
```

input\_handle: the list
index: the position in the list to which the tensor will be assigned
item: the element to be assigned to that position
output\_handle: the new list, with the element in the proper position

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `index` | A `Tensor` of type `int32`. |
| `item` | A `Tensor`. |
| `resize_if_index_out_of_bounds` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |