# tf.train.list_variables

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/list_variables](https://tensorflow.google.cn/api_docs/python/tf/train/list_variables)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/checkpoint_utils.py#L117-L147) |

Lists the checkpoint keys and shapes of variables in a checkpoint.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.list_variables`](https://tensorflow.google.cn/api_docs/python/tf/train/list_variables)

```
tf.train.list_variables(
    ckpt_dir_or_file
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) | * [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://tensorflow.google.cn/recommenders/examples/tpu_embedding_layer) |

Checkpoint keys are paths in a checkpoint graph.

#### Example usage:

```
import tensorflow as tf
import os
ckpt_directory = "/tmp/training_checkpoints/ckpt"
ckpt = tf.train.Checkpoint(optimizer=optimizer, model=model)
manager = tf.train.CheckpointManager(ckpt, ckpt_directory, max_to_keep=3)
train_and_checkpoint(model, manager)
tf.train.list_variables(manager.latest_checkpoint)
```

| Args | |

|  |  |
| --- | --- |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint. |

| Returns | |
| List of tuples `(key, shape)`. | |