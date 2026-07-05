# tf.raw_ops.DeleteSessionTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteSessionTensor](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteSessionTensor)

---

Delete the tensor specified by its handle in the session.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DeleteSessionTensor`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteSessionTensor)

```
tf.raw_ops.DeleteSessionTensor(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `string`. The handle for a tensor stored in the session state. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |