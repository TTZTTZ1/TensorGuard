# tf.raw_ops.TensorArrayConcatV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayConcatV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayConcatV2)

---

Deprecated.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayConcatV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayConcatV2)

```
tf.raw_ops.TensorArrayConcatV2(
    handle, flow_in, dtype, element_shape_except0=None, name=None
)
```

Use TensorArrayConcatV3

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `string`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `element_shape_except0` | An optional [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Defaults to `None`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (value, lengths). | |
| `value` | A `Tensor` of type `dtype`. |
| `lengths` | A `Tensor` of type `int64`. |