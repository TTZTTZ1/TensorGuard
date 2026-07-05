# tf.raw_ops.BoostedTreesDeserializeEnsemble

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesDeserializeEnsemble](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesDeserializeEnsemble)

---

Deserializes a serialized tree ensemble config and replaces current tree

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BoostedTreesDeserializeEnsemble`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesDeserializeEnsemble)

```
tf.raw_ops.BoostedTreesDeserializeEnsemble(
    tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name=None
)
```

ensemble.

| Args | |

|  |  |
| --- | --- |
| `tree_ensemble_handle` | A `Tensor` of type `resource`. Handle to the tree ensemble. |
| `stamp_token` | A `Tensor` of type `int64`. Token to use as the new value of the resource stamp. |
| `tree_ensemble_serialized` | A `Tensor` of type `string`. Serialized proto of the ensemble. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |