# tf.tensor_scatter_nd_min

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_min](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_min)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.tensor_scatter_nd_min`](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_min)

```
tf.tensor_scatter_nd_min(
    tensor: Annotated[Any, TV_TensorScatterMin_T],
    indices: Annotated[Any, TV_TensorScatterMin_Tindices],
    updates: Annotated[Any, TV_TensorScatterMin_T],
    name=None
) -> Annotated[Any, TV_TensorScatterMin_T]
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Introduction to tensor slicing](https://tensorflow.google.cn/guide/tensor_slicing) |

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. Tensor to update. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `updates` | A `Tensor`. Must have the same type as `tensor`. Updates to scatter into output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `tensor`. | |