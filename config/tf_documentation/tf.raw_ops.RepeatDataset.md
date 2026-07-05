# tf.raw_ops.RepeatDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RepeatDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RepeatDataset)

---

Creates a dataset that emits the outputs of `input_dataset` `count` times.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RepeatDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RepeatDataset)

```
tf.raw_ops.RepeatDataset(
    input_dataset,
    count,
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
| `count` | A `Tensor` of type `int64`. A scalar representing the number of times that `input_dataset` should be repeated. A value of `-1` indicates that it should be repeated infinitely. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |