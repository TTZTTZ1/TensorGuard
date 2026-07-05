# tf.raw_ops.VarIsInitializedOp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarIsInitializedOp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarIsInitializedOp)

---

Checks whether a resource handle-based variable has been initialized.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.VarIsInitializedOp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarIsInitializedOp)

```
tf.raw_ops.VarIsInitializedOp(
    resource, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. the input resource handle. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |