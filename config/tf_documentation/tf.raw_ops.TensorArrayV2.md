# tf.raw_ops.TensorArrayV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayV2)

---

Deprecated.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayV2)

```
tf.raw_ops.TensorArrayV2(
    size,
    dtype,
    element_shape=None,
    dynamic_size=False,
    clear_after_read=True,
    tensor_array_name='',
    name=None
)
```

Use TensorArrayV3

| Args | |

|  |  |
| --- | --- |
| `size` | A `Tensor` of type `int32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `dynamic_size` | An optional `bool`. Defaults to `False`. |
| `clear_after_read` | An optional `bool`. Defaults to `True`. |
| `tensor_array_name` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |