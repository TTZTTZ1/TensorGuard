# tf.raw_ops.TensorListStack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListStack](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListStack)

---

Stacks all tensors in the list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListStack`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListStack)

```
tf.raw_ops.TensorListStack(
    input_handle, element_shape, element_dtype, num_elements=-1, name=None
)
```

Requires that all tensors have the same shape.

input\_handle: the input list
tensor: the gathered result
num\_elements: optional. If not -1, the number of elements in the list.

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `element_shape` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `num_elements` | An optional `int`. Defaults to `-1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `element_dtype`. | |