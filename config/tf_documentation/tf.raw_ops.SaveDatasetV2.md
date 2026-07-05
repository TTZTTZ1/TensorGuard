# tf.raw_ops.SaveDatasetV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDatasetV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDatasetV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SaveDatasetV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDatasetV2)

```
tf.raw_ops.SaveDatasetV2(
    input_dataset,
    path,
    shard_func_other_args,
    shard_func,
    output_types,
    output_shapes,
    compression='',
    use_shard_func=True,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `path` | A `Tensor` of type `string`. |
| `shard_func_other_args` | A list of `Tensor` objects. |
| `shard_func` | A function decorated with @Defun. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `compression` | An optional `string`. Defaults to `""`. |
| `use_shard_func` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |