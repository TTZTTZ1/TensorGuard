# tf.raw_ops.DeleteIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteIterator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteIterator)

---

A container for an iterator resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DeleteIterator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeleteIterator)

```
tf.raw_ops.DeleteIterator(
    handle, deleter, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. A handle to the iterator to delete. |
| `deleter` | A `Tensor` of type `variant`. A variant deleter. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |