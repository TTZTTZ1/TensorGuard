# tf.raw_ops.SkipDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SkipDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SkipDataset)

---

Creates a dataset that skips `count` elements from the `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SkipDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SkipDataset)

```
tf.raw_ops.SkipDataset(
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
| `count` | A `Tensor` of type `int64`. A scalar representing the number of elements from the `input_dataset` that should be skipped. If count is -1, skips everything. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |