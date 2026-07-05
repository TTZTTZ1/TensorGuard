# tf.raw_ops.VariableV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableV2)

---

Holds state in the form of a tensor that persists across steps.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.VariableV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableV2)

```
tf.raw_ops.VariableV2(
    shape, dtype, container='', shared_name='', name=None
)
```

Outputs a ref to the tensor state so it may be read or modified.

about sharing states in tensorflow.

| Args | |

|  |  |
| --- | --- |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The shape of the variable tensor. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of elements in the variable tensor. |
| `container` | An optional `string`. Defaults to `""`. If non-empty, this variable is placed in the given container. Otherwise, a default container is used. |
| `shared_name` | An optional `string`. Defaults to `""`. If non-empty, this variable is named in the given bucket with this shared\_name. Otherwise, the node name is used instead. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor` of type `dtype`. | |