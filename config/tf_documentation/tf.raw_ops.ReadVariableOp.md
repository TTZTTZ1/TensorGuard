# tf.raw_ops.ReadVariableOp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReadVariableOp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReadVariableOp)

---

Reads the value of a variable.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ReadVariableOp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ReadVariableOp)

```
tf.raw_ops.ReadVariableOp(
    resource, dtype, name=None
)
```

The tensor returned by this operation is immutable.

The value returned by this operation is guaranteed to be influenced by all the
writes on which this operation depends directly or indirectly, and to not be
influenced by any of the writes which depend directly or indirectly on this
operation.

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. handle to the resource in which to store the variable. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). the dtype of the value. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |