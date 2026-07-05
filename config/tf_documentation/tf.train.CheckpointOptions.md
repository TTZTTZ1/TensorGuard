# tf.train.CheckpointOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/CheckpointOptions](https://tensorflow.google.cn/api_docs/python/tf/train/CheckpointOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/checkpoint/checkpoint_options.py#L25-L128) |

Options for constructing a Checkpoint.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.CheckpointOptions`](https://tensorflow.google.cn/api_docs/python/tf/train/CheckpointOptions)

```
tf.train.CheckpointOptions(
    experimental_io_device=None,
    experimental_enable_async_checkpoint=False,
    experimental_write_callbacks=None,
    enable_async=False,
    experimental_skip_slot_variables=False,
    experimental_sharding_callback=None
)
```

Used as the `options` argument to either [`tf.train.Checkpoint.save()`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint#save) or
[`tf.train.Checkpoint.restore()`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint#restore) methods to adjust how variables are
saved/restored.

Example: Run IO ops on "localhost" while saving a checkpoint:

```
step = tf.Variable(0, name="step")
checkpoint = tf.train.Checkpoint(step=step)
options = tf.train.CheckpointOptions(experimental_io_device="/job:localhost")
checkpoint.save("/tmp/ckpt", options=options)
```

| Args | |

|  |  |
| --- | --- |
| `experimental_io_device` | string. Applies in a distributed setting. Tensorflow device to use to access the filesystem. If `None` (default) then for each variable the filesystem is accessed from the CPU:0 device of the host where that variable is assigned. If specified, the filesystem is instead accessed from that device for all variables. This is for example useful if you want to save to a local directory, such as "/tmp" when running in a distributed setting. In that case pass a device for the host where the "/tmp" directory is accessible. |
| `experimental_enable_async_checkpoint` | bool Type. Deprecated, please use the enable\_async option. |
| `experimental_write_callbacks` | List[Callable]. A list of callback functions that will be executed after each saving event finishes (i.e. after `save()` or `write()`). For async checkpoint, the callbacks will be executed only after the async thread finishes saving. The return values of the callback(s) will be ignored. The callback(s) can optionally take the `save_path` (the result of `save()` or `write()`) as an argument. The callbacks will be executed in the same order of this list after the checkpoint has been written. |
| `enable_async` | bool Type. Indicates whether async checkpointing is enabled. Default is False, i.e., no async checkpoint. Async checkpoint moves the checkpoint file writing off the main thread, so that the model can continue to train while the checkpoing file writing runs in the background. Async checkpoint reduces TPU device idle cycles and speeds up model training process, while memory consumption may increase. |
| `experimental_skip_slot_variables` | bool Type. If true, ignores slot variables during restore. Context: TPU Embedding layers for Serving do not properly restore slot variables. This option is a way to omit restoring slot variables which are not required for Serving usecase anyways.(b/315912101) |
| `experimental_sharding_callback` | [`tf.train.experimental.ShardingCallback`](https://tensorflow.google.cn/api_docs/python/tf/train/experimental/ShardingCallback). A pre-made or custom callback that determines how checkpoints are sharded on disk. Pre-made callback options are `tf.train.experimental.ShardByDevicePolicy` and [`tf.train.experimental.MaxShardSizePolicy`](https://tensorflow.google.cn/api_docs/python/tf/train/experimental/MaxShardSizePolicy). You may also write a custom callback, see [`tf.train.experimental.ShardingCallback`](https://tensorflow.google.cn/api_docs/python/tf/train/experimental/ShardingCallback). |

| Attributes | |

|  |  |
| --- | --- |
| `enable_async` |  |

|  |  |
| --- | --- |
| `experimental_enable_async_checkpoint` |  |

|  |  |
| --- | --- |
| `experimental_io_device` |  |

|  |  |
| --- | --- |
| `experimental_sharding_callback` |  |

|  |  |
| --- | --- |
| `experimental_skip_slot_variables` |  |

|  |  |
| --- | --- |
| `experimental_write_callbacks` |  |