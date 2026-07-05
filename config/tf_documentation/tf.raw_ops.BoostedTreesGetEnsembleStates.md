# tf.raw_ops.BoostedTreesGetEnsembleStates

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesGetEnsembleStates](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesGetEnsembleStates)

---

Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BoostedTreesGetEnsembleStates`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BoostedTreesGetEnsembleStates)

```
tf.raw_ops.BoostedTreesGetEnsembleStates(
    tree_ensemble_handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `tree_ensemble_handle` | A `Tensor` of type `resource`. Handle to the tree ensemble. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (stamp\_token, num\_trees, num\_finalized\_trees, num\_attempted\_layers, last\_layer\_nodes\_range). | |
| `stamp_token` | A `Tensor` of type `int64`. |
| `num_trees` | A `Tensor` of type `int32`. |
| `num_finalized_trees` | A `Tensor` of type `int32`. |
| `num_attempted_layers` | A `Tensor` of type `int32`. |
| `last_layer_nodes_range` | A `Tensor` of type `int32`. |