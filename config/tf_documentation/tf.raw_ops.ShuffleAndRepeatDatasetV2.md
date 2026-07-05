# tf.raw_ops.ShuffleAndRepeatDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleAndRepeatDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleAndRepeatDatasetV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShuffleAndRepeatDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleAndRepeatDatasetV2)

```
tf.raw_ops.ShuffleAndRepeatDatasetV2(
    input_dataset,
    buffer_size,
    seed,
    seed2,
    count,
    seed_generator,
    output_types,
    output_shapes,
    reshuffle_each_iteration=True,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `buffer_size` | A `Tensor` of type `int64`. |
| `seed` | A `Tensor` of type `int64`. |
| `seed2` | A `Tensor` of type `int64`. |
| `count` | A `Tensor` of type `int64`. |
| `seed_generator` | A `Tensor` of type `resource`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `reshuffle_each_iteration` | An optional `bool`. Defaults to `True`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |