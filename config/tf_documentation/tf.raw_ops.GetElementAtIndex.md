# tf.raw_ops.GetElementAtIndex

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetElementAtIndex](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetElementAtIndex)

---

Gets the element at the specified index in a dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GetElementAtIndex`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetElementAtIndex)

```
tf.raw_ops.GetElementAtIndex(
    dataset, index, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A `Tensor` of type `variant`. |
| `index` | A `Tensor` of type `int64`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `output_types`. | |