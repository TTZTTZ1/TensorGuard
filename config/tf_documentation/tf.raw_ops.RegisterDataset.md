# tf.raw_ops.RegisterDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegisterDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegisterDataset)

---

Registers a dataset with the tf.data service.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RegisterDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegisterDataset)

```
tf.raw_ops.RegisterDataset(
    dataset,
    address,
    protocol,
    external_state_policy,
    element_spec='',
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A `Tensor` of type `variant`. |
| `address` | A `Tensor` of type `string`. |
| `protocol` | A `Tensor` of type `string`. |
| `external_state_policy` | An `int`. |
| `element_spec` | An optional `string`. Defaults to `""`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |