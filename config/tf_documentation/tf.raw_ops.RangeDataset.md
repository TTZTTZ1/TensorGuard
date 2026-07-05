# tf.raw_ops.RangeDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RangeDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RangeDataset)

---

Creates a dataset with a range of values. Corresponds to python's xrange.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RangeDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RangeDataset)

```
tf.raw_ops.RangeDataset(
    start,
    stop,
    step,
    output_types,
    output_shapes,
    metadata='',
    replicate_on_split=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `start` | A `Tensor` of type `int64`. corresponds to start in python's xrange(). |
| `stop` | A `Tensor` of type `int64`. corresponds to stop in python's xrange(). |
| `step` | A `Tensor` of type `int64`. corresponds to step in python's xrange(). |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `replicate_on_split` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |