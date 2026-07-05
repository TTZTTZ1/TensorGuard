# tf.raw_ops.IteratorGetDevice

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetDevice](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetDevice)

---

Returns the name of the device on which `resource` has been placed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IteratorGetDevice`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetDevice)

```
tf.raw_ops.IteratorGetDevice(
    resource, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |