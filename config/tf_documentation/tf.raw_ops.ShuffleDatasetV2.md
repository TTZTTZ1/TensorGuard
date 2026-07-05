# tf.raw_ops.ShuffleDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDatasetV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShuffleDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDatasetV2)

```
tf.raw_ops.ShuffleDatasetV2(
    input_dataset,
    buffer_size,
    seed_generator,
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
| `buffer_size` | A `Tensor` of type `int64`. |
| `seed_generator` | A `Tensor` of type `resource`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |