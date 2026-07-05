# tf.raw_ops.LoadDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoadDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoadDataset)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LoadDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoadDataset)

```
tf.raw_ops.LoadDataset(
    path,
    reader_func_other_args,
    output_types,
    output_shapes,
    reader_func,
    compression='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `path` | A `Tensor` of type `string`. |
| `reader_func_other_args` | A list of `Tensor` objects. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `reader_func` | A function decorated with @Defun. |
| `compression` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |