# tf.raw_ops.FlatMapDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FlatMapDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FlatMapDataset)

---

Creates a dataset that applies `f` to the outputs of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FlatMapDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FlatMapDataset)

```
tf.raw_ops.FlatMapDataset(
    input_dataset,
    other_arguments,
    f,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

Unlike MapDataset, the `f` in FlatMapDataset is expected to return a
Dataset variant, and FlatMapDataset will flatten successive results
into a single Dataset.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `other_arguments` | A list of `Tensor` objects. |
| `f` | A function decorated with @Defun. A function mapping elements of `input_dataset`, concatenated with `other_arguments`, to a Dataset variant that contains elements matching `output_types` and `output_shapes`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |