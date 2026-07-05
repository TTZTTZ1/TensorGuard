# tf.train.load_variable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/load_variable](https://tensorflow.google.cn/api_docs/python/tf/train/load_variable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/checkpoint_utils.py#L83-L114) |

Returns the tensor value of the given variable in the checkpoint.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.load_variable`](https://tensorflow.google.cn/api_docs/python/tf/train/load_variable)

```
tf.train.load_variable(
    ckpt_dir_or_file, name
)
```

When the variable name is unknown, you can use [`tf.train.list_variables`](https://tensorflow.google.cn/api_docs/python/tf/train/list_variables) to
inspect all the variable names.

#### Example usage:

```
import tensorflow as tf
a = tf.Variable(1.0)
b = tf.Variable(2.0)
ckpt = tf.train.Checkpoint(var_list={'a': a, 'b': b})
ckpt_path = ckpt.save('tmp-ckpt')
var= tf.train.load_variable(
    ckpt_path, 'var_list/a/.ATTRIBUTES/VARIABLE_VALUE')
print(var)  # 1.0
```

| Args | |

|  |  |
| --- | --- |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint. |
| `name` | Name of the variable to return. |

| Returns | |
| A numpy `ndarray` with a copy of the value of this variable. | |