# tf.raw_ops.OptionsDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionsDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionsDataset)

---

Creates a dataset by attaching tf.data.Options to `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OptionsDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionsDataset)

```
tf.raw_ops.OptionsDataset(
    input_dataset,
    serialized_options,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `serialized_options` | A `string`. A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of serialized [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) protocol buffer. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |