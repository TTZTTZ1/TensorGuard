# tf.raw_ops.IgnoreErrorsDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgnoreErrorsDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgnoreErrorsDataset)

---

Creates a dataset that contains the elements of `input_dataset` ignoring errors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IgnoreErrorsDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IgnoreErrorsDataset)

```
tf.raw_ops.IgnoreErrorsDataset(
    input_dataset, output_types, output_shapes, log_warning=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `log_warning` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |