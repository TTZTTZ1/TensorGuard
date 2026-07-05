# tf.raw_ops.TensorListPushBack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPushBack](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPushBack)

---

Returns a list which has the passed-in `Tensor` as last element and the other elements of the given list in `input_handle`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListPushBack`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListPushBack)

```
tf.raw_ops.TensorListPushBack(
    input_handle, tensor, name=None
)
```

tensor: The tensor to put on the list.
input\_handle: The old list.
output\_handle: A list with the elements of the old list followed by tensor.
element\_dtype: the type of elements in the list.
element\_shape: a shape compatible with that of elements in the list.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `tensor` | A `Tensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |