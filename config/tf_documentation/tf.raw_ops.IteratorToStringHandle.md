# tf.raw_ops.IteratorToStringHandle

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorToStringHandle](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorToStringHandle)

---

Converts the given `resource_handle` representing an iterator to a string.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IteratorToStringHandle`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorToStringHandle)

```
tf.raw_ops.IteratorToStringHandle(
    resource_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `resource_handle` | A `Tensor` of type `resource`. A handle to an iterator resource. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |