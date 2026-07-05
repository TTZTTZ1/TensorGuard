# tf.raw_ops.MapDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MapDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MapDataset)

---

Creates a dataset that applies `f` to the outputs of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MapDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MapDataset)

```
tf.raw_ops.MapDataset(
    input_dataset,
    other_arguments,
    f,
    output_types,
    output_shapes,
    use_inter_op_parallelism=True,
    preserve_cardinality=False,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `other_arguments` | A list of `Tensor` objects. |
| `f` | A function decorated with @Defun. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `use_inter_op_parallelism` | An optional `bool`. Defaults to `True`. |
| `preserve_cardinality` | An optional `bool`. Defaults to `False`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |