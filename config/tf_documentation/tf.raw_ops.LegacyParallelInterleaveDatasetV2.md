# tf.raw_ops.LegacyParallelInterleaveDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LegacyParallelInterleaveDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LegacyParallelInterleaveDatasetV2)

---

Creates a dataset that applies `f` to the outputs of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LegacyParallelInterleaveDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LegacyParallelInterleaveDatasetV2)

```
tf.raw_ops.LegacyParallelInterleaveDatasetV2(
    input_dataset,
    other_arguments,
    cycle_length,
    block_length,
    buffer_output_elements,
    prefetch_input_elements,
    f,
    output_types,
    output_shapes,
    deterministic='default',
    metadata='',
    name=None
)
```

The resulting dataset is similar to the `InterleaveDataset`, with the exception
that if retrieving the next value from a dataset would cause the requester to
block, it will skip that input dataset. This dataset is especially useful
when loading data from a variable-latency datastores (e.g. HDFS, GCS), as it
allows the training step to proceed so long as some data is available.

!! WARNING !! This dataset is not deterministic!

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `other_arguments` | A list of `Tensor` objects. |
| `cycle_length` | A `Tensor` of type `int64`. |
| `block_length` | A `Tensor` of type `int64`. |
| `buffer_output_elements` | A `Tensor` of type `int64`. |
| `prefetch_input_elements` | A `Tensor` of type `int64`. |
| `f` | A function decorated with @Defun. A function mapping elements of `input_dataset`, concatenated with `other_arguments`, to a Dataset variant that contains elements matching `output_types` and `output_shapes`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `deterministic` | An optional `string`. Defaults to `"default"`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |