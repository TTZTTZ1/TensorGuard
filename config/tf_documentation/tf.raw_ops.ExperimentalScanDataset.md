# tf.raw_ops.ExperimentalScanDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalScanDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalScanDataset)

---

Creates a dataset successively reduces `f` over the elements of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ExperimentalScanDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalScanDataset)

```
tf.raw_ops.ExperimentalScanDataset(
    input_dataset,
    initial_state,
    other_arguments,
    f,
    output_types,
    output_shapes,
    preserve_cardinality=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `initial_state` | A list of `Tensor` objects. |
| `other_arguments` | A list of `Tensor` objects. |
| `f` | A function decorated with @Defun. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `preserve_cardinality` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |