# tf.raw_ops.ExperimentalUnbatchDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalUnbatchDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalUnbatchDataset)

---

A dataset that splits the elements of its input into multiple elements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ExperimentalUnbatchDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalUnbatchDataset)

```
tf.raw_ops.ExperimentalUnbatchDataset(
    input_dataset, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |