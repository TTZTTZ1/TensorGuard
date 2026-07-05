# tf.raw_ops.BoostedTreesSerializeEnsemble

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesSerializeEnsemble](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesSerializeEnsemble)

---

Serializes the tree ensemble to a proto.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BoostedTreesSerializeEnsemble`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesSerializeEnsemble)

```
tf.raw_ops.BoostedTreesSerializeEnsemble(
    tree_ensemble_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `tree_ensemble_handle` | A `Tensor` of type `resource`. Handle to the tree ensemble. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (stamp\_token, tree\_ensemble\_serialized). | |
| `stamp_token` | A `Tensor` of type `int64`. |
| `tree_ensemble_serialized` | A `Tensor` of type `string`. |