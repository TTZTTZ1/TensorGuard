# tf.raw_ops.TensorArrayReadV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayReadV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayReadV2)

---

Deprecated.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorArrayReadV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorArrayReadV2)

```
tf.raw_ops.TensorArrayReadV2(
    handle, index, flow_in, dtype, name=None
)
```

Use TensorArrayReadV3

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `string`. |
| `index` | A `Tensor` of type `int32`. |
| `flow_in` | A `Tensor` of type `float32`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |