# tf.raw_ops.OptimizeDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptimizeDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptimizeDatasetV2)

---

Creates a dataset by applying related optimizations to `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OptimizeDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptimizeDatasetV2)

```
tf.raw_ops.OptimizeDatasetV2(
    input_dataset,
    optimizations_enabled,
    optimizations_disabled,
    optimizations_default,
    output_types,
    output_shapes,
    optimization_configs=[],
    name=None
)
```

Creates a dataset by applying related optimizations to `input_dataset`.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `optimizations_enabled` | A `Tensor` of type `string`. A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) vector [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) identifying user enabled optimizations. |
| `optimizations_disabled` | A `Tensor` of type `string`. A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) vector [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) identifying user disabled optimizations. |
| `optimizations_default` | A `Tensor` of type `string`. A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) vector [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) identifying optimizations by default. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `optimization_configs` | An optional list of `strings`. Defaults to `[]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |