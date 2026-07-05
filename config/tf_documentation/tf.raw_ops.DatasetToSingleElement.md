# tf.raw_ops.DatasetToSingleElement

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetToSingleElement](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetToSingleElement)

---

Outputs the single element from the given dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DatasetToSingleElement`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetToSingleElement)

```
tf.raw_ops.DatasetToSingleElement(
    dataset, output_types, output_shapes, metadata='', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A `Tensor` of type `variant`. A handle to a dataset that contains a single element. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `output_types`. | |