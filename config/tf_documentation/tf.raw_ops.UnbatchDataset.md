# tf.raw_ops.UnbatchDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchDataset)

---

A dataset that splits the elements of its input into multiple elements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.UnbatchDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchDataset)

```
tf.raw_ops.UnbatchDataset(
    input_dataset,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |