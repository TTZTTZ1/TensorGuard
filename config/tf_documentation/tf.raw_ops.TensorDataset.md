# tf.raw_ops.TensorDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorDataset)

---

Creates a dataset that emits `components` as a tuple of tensors once.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorDataset)

```
tf.raw_ops.TensorDataset(
    components, output_shapes, metadata='', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `components` | A list of `Tensor` objects. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |