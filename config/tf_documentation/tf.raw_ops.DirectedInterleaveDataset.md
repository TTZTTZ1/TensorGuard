# tf.raw_ops.DirectedInterleaveDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DirectedInterleaveDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DirectedInterleaveDataset)

---

A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DirectedInterleaveDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DirectedInterleaveDataset)

```
tf.raw_ops.DirectedInterleaveDataset(
    selector_input_dataset,
    data_input_datasets,
    output_types,
    output_shapes,
    stop_on_empty_dataset=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `selector_input_dataset` | A `Tensor` of type `variant`. A dataset of scalar `DT_INT64` elements that determines which of the `N` data inputs should produce the next output element. |
| `data_input_datasets` | A list of at least 1 `Tensor` objects with type `variant`. `N` datasets with the same type that will be interleaved according to the values of `selector_input_dataset`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `stop_on_empty_dataset` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |