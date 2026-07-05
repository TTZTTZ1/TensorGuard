# tf.raw_ops.IsVariableInitialized

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsVariableInitialized](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsVariableInitialized)

---

Checks whether a tensor has been initialized.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IsVariableInitialized`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsVariableInitialized)

```
tf.raw_ops.IsVariableInitialized(
    ref, name=None
)
```

Outputs boolean scalar indicating whether the tensor has been initialized.

| Args | |

|  |  |
| --- | --- |
| `ref` | A mutable `Tensor`. Should be from a `Variable` node. May be uninitialized. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |