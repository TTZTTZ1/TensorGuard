# tf.tensor_scatter_nd_max

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_max](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_max)

---

Apply a sparse update to a tensor taking the element-wise maximum.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.tensor_scatter_nd_max`](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_max)

```
tf.tensor_scatter_nd_max(
    tensor: Annotated[Any, TV_TensorScatterMax_T],
    indices: Annotated[Any, TV_TensorScatterMax_Tindices],
    updates: Annotated[Any, TV_TensorScatterMax_T],
    name=None
) -> Annotated[Any, TV_TensorScatterMax_T]
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Introduction to tensor slicing](https://tensorflow.google.cn/guide/tensor_slicing) |

Returns a new tensor copied from `tensor` whose values are element-wise maximum between
tensor and updates according to the indices.

```
>>> tensor = [0, 0, 0, 0, 0, 0, 0, 0]
>>> indices = [[1], [4], [5]]
>>> updates = [1, -1, 1]
>>> tf.tensor_scatter_nd_max(tensor, indices, updates).numpy()
array([0, 1, 0, 0, 0, 1, 0, 0], dtype=int32)
```

Refer to [`tf.tensor_scatter_nd_update`](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_update) for more details.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. Tensor to update. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `updates` | A `Tensor`. Must have the same type as `tensor`. Updates to scatter into output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `tensor`. | |