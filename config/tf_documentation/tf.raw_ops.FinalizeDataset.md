# tf.raw_ops.FinalizeDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FinalizeDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FinalizeDataset)

---

Creates a dataset by applying [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) to `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FinalizeDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FinalizeDataset)

```
tf.raw_ops.FinalizeDataset(
    input_dataset,
    output_types,
    output_shapes,
    has_captured_ref=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `has_captured_ref` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |