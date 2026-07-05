# tf.raw_ops.ChooseFastestDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ChooseFastestDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ChooseFastestDataset)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ChooseFastestDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ChooseFastestDataset)

```
tf.raw_ops.ChooseFastestDataset(
    input_datasets, num_experiments, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_datasets` | A list of at least 2 `Tensor` objects with type `variant`. |
| `num_experiments` | An `int`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |