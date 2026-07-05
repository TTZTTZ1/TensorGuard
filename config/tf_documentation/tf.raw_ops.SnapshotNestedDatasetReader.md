# tf.raw_ops.SnapshotNestedDatasetReader

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotNestedDatasetReader](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotNestedDatasetReader)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SnapshotNestedDatasetReader`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SnapshotNestedDatasetReader)

```
tf.raw_ops.SnapshotNestedDatasetReader(
    inputs, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of at least 1 `Tensor` objects with type `variant`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |