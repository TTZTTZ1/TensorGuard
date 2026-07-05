# tf.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsBoostedTreesQuantileStreamResourceInitialized](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsBoostedTreesQuantileStreamResourceInitialized)

---

Checks whether a quantile stream has been initialized.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsBoostedTreesQuantileStreamResourceInitialized)

```
tf.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized(
    quantile_stream_resource_handle, name=None
)
```

An Op that checks if quantile stream resource is initialized.

| Args | |

|  |  |
| --- | --- |
| `quantile_stream_resource_handle` | A `Tensor` of type `resource`. resource; The reference to quantile stream resource handle. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |