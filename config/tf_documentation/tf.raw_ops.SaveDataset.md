# tf.raw_ops.SaveDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDataset)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SaveDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SaveDataset)

```
tf.raw_ops.SaveDataset(
    input_dataset,
    path,
    shard_func_other_args,
    shard_func,
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
| `compression` | An optional `string`. Defaults to `""`. |
| `use_shard_func` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |