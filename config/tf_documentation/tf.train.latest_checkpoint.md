# tf.train.latest_checkpoint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/latest_checkpoint](https://tensorflow.google.cn/api_docs/python/tf/train/latest_checkpoint)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/checkpoint/checkpoint_management.py#L328-L365) |

Finds the filename of latest saved checkpoint file.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.latest_checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/latest_checkpoint)

```
tf.train.latest_checkpoint(
    checkpoint_dir, latest_filename=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating model checkpoints](https://tensorflow.google.cn/guide/migrate/migrating_checkpoints) * [Training checkpoints](https://tensorflow.google.cn/guide/checkpoint) * [Estimators](https://tensorflow.google.cn/guide/estimator) | * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Multi-worker training with Keras](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_keras) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) |

Gets the checkpoint state given the provided checkpoint\_dir and looks for a
corresponding TensorFlow 2 (preferred) or TensorFlow 1.x checkpoint path.
The latest\_filename argument is only applicable if you are saving checkpoint
using [`v1.train.Saver.save`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/train/Saver#save)

See the [Training Checkpoints
Guide](https://tensorflow.google.cn/guide/checkpoint) for more details and
examples.`

| Args | |

|  |  |
| --- | --- |
| `checkpoint_dir` | Directory where the variables were saved. |
| `latest_filename` | Optional name for the protocol buffer file that contains the list of most recent checkpoint filenames. See the corresponding argument to [`v1.train.Saver.save`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/train/Saver#save). |

| Returns | |
| The full path to the latest checkpoint or `None` if no checkpoint was found. | |