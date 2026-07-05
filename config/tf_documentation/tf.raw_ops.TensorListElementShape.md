# tf.raw_ops.TensorListElementShape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListElementShape](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListElementShape)

---

The shape of the elements of the given list, as a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListElementShape`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListElementShape)

```
tf.raw_ops.TensorListElementShape(
    input_handle, shape_type, name=None
)
```

input\_handle: the list
element\_shape: the shape of elements of the list

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `shape_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `shape_type`. | |