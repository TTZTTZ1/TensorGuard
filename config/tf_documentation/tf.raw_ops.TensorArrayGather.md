# tf.raw_ops.TensorArrayGather

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGather](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGather)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayGather`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGather)

```
tf.raw_ops.TensorArrayGather(
    handle, indices, flow_in, dtype, element_shape=None, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `indices` | A `Tensor` of type `int32`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |