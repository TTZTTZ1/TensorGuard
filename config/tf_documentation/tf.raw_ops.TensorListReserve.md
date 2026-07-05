# tf.raw_ops.TensorListReserve

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListReserve](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListReserve)

---

List of the given size with empty elements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListReserve`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListReserve)

```
tf.raw_ops.TensorListReserve(
    element_shape, num_elements, element_dtype, name=None
)
```

element\_shape: the shape of the future elements of the list
num\_elements: the number of elements to reserve
handle: the output list
element\_dtype: the desired type of elements in the list.

| Args | |

|  |  |
| --- | --- |
| `element_shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. |
| `num_elements` | A `Tensor` of type `int32`. |
| `element_dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |