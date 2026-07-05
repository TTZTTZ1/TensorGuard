# tf.raw_ops.DatasetFromGraph

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetFromGraph](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetFromGraph)

---

Creates a dataset from the given `graph_def`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DatasetFromGraph`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetFromGraph)

```
tf.raw_ops.DatasetFromGraph(
    graph_def, name=None
)
```

Creates a dataset from the provided `graph_def`.

| Args | |

|  |  |
| --- | --- |
| `graph_def` | A `Tensor` of type `string`. The graph representation of the dataset (as serialized GraphDef). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |