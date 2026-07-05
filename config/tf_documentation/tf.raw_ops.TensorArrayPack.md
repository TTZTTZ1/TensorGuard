# tf.raw_ops.TensorArrayPack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayPack](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayPack)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayPack`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayPack)

```
tf.raw_ops.TensorArrayPack(
    handle, flow_in, dtype, element_shape=None, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |