# tf.raw_ops.MergeV2Checkpoints

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeV2Checkpoints](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeV2Checkpoints)

---

V2 format specific: merges the metadata files of sharded checkpoints.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MergeV2Checkpoints`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeV2Checkpoints)

```
tf.raw_ops.MergeV2Checkpoints(
    checkpoint_prefixes,
    destination_prefix,
    delete_old_dirs=True,
    allow_missing_files=False,
    name=None
)
```

The

result is one logical checkpoint, with one physical metadata file and renamed
data files.

Intended for "grouping" multiple checkpoints in a sharded checkpoint setup.

If delete\_old\_dirs is true, attempts to delete recursively the dirname of each
path in the input checkpoint\_prefixes. This is useful when those paths are non
user-facing temporary locations.

If allow\_missing\_files is true, merges the checkpoint prefixes as long as
at least one file exists. Otherwise, if no files exist, an error will be thrown.
The default value for allow\_missing\_files is false.

| Args | |

|  |  |
| --- | --- |
| `checkpoint_prefixes` | A `Tensor` of type `string`. prefixes of V2 checkpoints to merge. |
| `destination_prefix` | A `Tensor` of type `string`. scalar. The desired final prefix. Allowed to be the same as one of the checkpoint\_prefixes. |
| `delete_old_dirs` | An optional `bool`. Defaults to `True`. see above. |
| `allow_missing_files` | An optional `bool`. Defaults to `False`. see above. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |