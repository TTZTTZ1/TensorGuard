# tf.train.load_checkpoint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/load_checkpoint](https://tensorflow.google.cn/api_docs/python/tf/train/load_checkpoint)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/checkpoint_utils.py#L46-L80) |

Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.load_checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/load_checkpoint)

```
tf.train.load_checkpoint(
    ckpt_dir_or_file
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Migrating model checkpoints](https://tensorflow.google.cn/guide/migrate/migrating_checkpoints) * [Training checkpoints](https://tensorflow.google.cn/guide/checkpoint) * [Migrate the fault tolerance mechanism](https://tensorflow.google.cn/guide/migrate/fault_tolerance) |

If `ckpt_dir_or_file` resolves to a directory with multiple checkpoints,
reader for the latest checkpoint is returned.

#### Example usage:

```
import tensorflow as tf
a = tf.Variable(1.0)
b = tf.Variable(2.0)
ckpt = tf.train.Checkpoint(var_list={'a': a, 'b': b})
ckpt_path = ckpt.save('tmp-ckpt')
reader= tf.train.load_checkpoint(ckpt_path)
print(reader.get_tensor('var_list/a/.ATTRIBUTES/VARIABLE_VALUE'))  # 1.0
```

| Args | |

|  |  |
| --- | --- |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint file. |

| Returns | |
| `CheckpointReader` object. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `ckpt_dir_or_file` resolves to a directory with no checkpoints. |