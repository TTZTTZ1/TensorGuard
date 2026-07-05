# tf.saved_model.experimental.VariablePolicy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/VariablePolicy](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/VariablePolicy)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/saved_model/save_options.py#L27-L90) |

Enum defining options for variable handling when saving.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.saved_model.experimental.VariablePolicy`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/VariablePolicy)

NONE
No policy applied: Distributed variables are saved as one variable, with no
device attached.

SAVE\_VARIABLE\_DEVICES
When saving variables, also save their device assignment.
This is useful if one wants to hardcode devices in saved models, but it also
makes them non-portable if soft device placement is disabled (more details
in [`tf.config.set_soft_device_placement`](https://tensorflow.google.cn/api_docs/python/tf/config/set_soft_device_placement)). This is currently not
fully supported by [`saved_model.load`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load), and is mainly intended to be used
when one will be reading the saved model at a lower API level. In the
example below, the graph saved by the call to [`saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save) will have
the variable devices correctly specified:

```
  exported = tf.train.Checkpoint()
  with tf.device('/GPU:0'):
    exported.x_gpu = tf.Variable(1.0)
  with tf.device('/CPU:0'):
    exported.x_cpu = tf.Variable(1.0)
  tf.saved_model.save(exported, export_dir,
      options = tf.saved_model.SaveOptions(
          experimental_variable_policy=
            tf.saved_model.experimental.VariablePolicy.SAVE_VARIABLE_DEVICES))
```

Distributed variables are still saved as one variable under this policy.

EXPAND\_DISTRIBUTED\_VARIABLES
Distributed variables will be saved with information about their components,
allowing for their restoration on load. Also, the saved graph will contain
references to those variables. This is useful when one wants to use the
model for training in environments where the original distribution strategy
is not available.

| Class Variables | |

|  |  |
| --- | --- |
| EXPAND\_DISTRIBUTED\_VARIABLES | `<VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES: 'expand_distributed_variables'>` |
| NONE | `<VariablePolicy.NONE: None>` |
| SAVE\_VARIABLE\_DEVICES | `<VariablePolicy.SAVE_VARIABLE_DEVICES: 'save_variable_devices'>` |