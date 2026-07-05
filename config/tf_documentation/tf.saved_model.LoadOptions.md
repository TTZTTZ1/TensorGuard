# tf.saved_model.LoadOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/LoadOptions](https://tensorflow.google.cn/api_docs/python/tf/saved_model/LoadOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/saved_model/load_options.py#L21-L125) |

Options for loading a SavedModel.

```
tf.saved_model.LoadOptions(
    allow_partial_checkpoint=False,
    experimental_io_device=None,
    experimental_skip_checkpoint=False,
    experimental_variable_policy=None,
    experimental_load_function_aliases=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Save and load a model using a distribution strategy](https://tensorflow.google.cn/tutorials/distribute/save_and_load) |

This function may be used in the `options` argument in functions that
load a SavedModel ([`tf.saved_model.load`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load), [`tf.keras.models.load_model`](https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model)).

| Args | |

|  |  |
| --- | --- |
| `allow_partial_checkpoint` | bool. Defaults to `False`. When enabled, allows the SavedModel checkpoint to not entirely match the loaded object. |
| `experimental_io_device` | string. Applies in a distributed setting. Tensorflow device to use to access the filesystem. If `None` (default) then for each variable the filesystem is accessed from the CPU:0 device of the host where that variable is assigned. If specified, the filesystem is instead accessed from that device for all variables. This is for example useful if you want to load from a local directory, such as "/tmp" when running in a distributed setting. In that case pass a device for the host where the "/tmp" directory is accessible. |
| `experimental_skip_checkpoint` | bool. Defaults to `False`. If set to `True`, checkpoints will not be restored. Note that this in the majority of cases will generate an unusable model. |
| `experimental_variable_policy` | string. The policy to apply to variables when loading. This is either a [`saved_model.experimental.VariablePolicy`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/VariablePolicy) enum instance or one of its value strings (case is not important). See that enum documentation for details. A value of `None` corresponds to the default policy. |
| `experimental_load_function_aliases` | bool. Defaults to `False`. If set to `True`, a `function_aliases` attribute will be added to the loaded SavedModel object. |

| Attributes | |

|  |  |
| --- | --- |
| `allow_partial_checkpoint` |  |

|  |  |
| --- | --- |
| `experimental_io_device` |  |

|  |  |
| --- | --- |
| `experimental_load_function_aliases` |  |

|  |  |
| --- | --- |
| `experimental_skip_checkpoint` |  |

|  |  |
| --- | --- |
| `experimental_variable_policy` |  |