# tf.train.get_checkpoint_state

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/get_checkpoint_state](https://tensorflow.google.cn/api_docs/python/tf/train/get_checkpoint_state)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/checkpoint/checkpoint_management.py#L250-L306) |

Returns CheckpointState proto from the "checkpoint" file.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.get_checkpoint_state`](https://tensorflow.google.cn/api_docs/python/tf/train/get_checkpoint_state)

```
tf.train.get_checkpoint_state(
    checkpoint_dir, latest_filename=None
)
```

If the "checkpoint" file contains a valid CheckpointState
proto, returns it.

| Args | |

|  |  |
| --- | --- |
| `checkpoint_dir` | The directory of checkpoints. |
| `latest_filename` | Optional name of the checkpoint file. Default to 'checkpoint'. |

| Returns | |
| A CheckpointState if the state was available, None otherwise. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the checkpoint read doesn't have model\_checkpoint\_path set. |