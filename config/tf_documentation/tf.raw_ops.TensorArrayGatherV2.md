# tf.raw_ops.TensorArrayGatherV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGatherV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGatherV2)

---

Deprecated.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayGatherV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayGatherV2)

```
tf.raw_ops.TensorArrayGatherV2(
    handle, indices, flow_in, dtype, element_shape=None, name=None
)
```

Use TensorArrayGatherV3

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `string`. |
| `indices` | A `Tensor` of type `int32`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |