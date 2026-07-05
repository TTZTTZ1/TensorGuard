# tf.raw_ops.Variable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Variable](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Variable)

---

Use VariableV2 instead.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Variable`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Variable)

```
tf.raw_ops.Variable(
    shape, dtype, container='', shared_name='', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `container` | An optional `string`. Defaults to `""`. |
| `shared_name` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor` of type `dtype`. | |