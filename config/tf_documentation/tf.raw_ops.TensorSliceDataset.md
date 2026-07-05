# tf.raw_ops.TensorSliceDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSliceDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSliceDataset)

---

Creates a dataset that emits each dim-0 slice of `components` once.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorSliceDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSliceDataset)

```
tf.raw_ops.TensorSliceDataset(
    components,
    output_shapes,
    is_files=False,
    metadata='',
    replicate_on_split=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `components` | A list of `Tensor` objects. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `is_files` | An optional `bool`. Defaults to `False`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `replicate_on_split` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |