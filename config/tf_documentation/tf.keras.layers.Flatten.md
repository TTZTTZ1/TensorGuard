# tf.keras.layers.Flatten

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Flatten](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Flatten)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/flatten.py#L11-L80) |

Flattens the input. Does not affect the batch size.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Flatten(
    data_format=None, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Migrate checkpoint saving](https://tensorflow.google.cn/guide/migrate/checkpoint_saver) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) |

**Note:** If inputs are shaped `(batch,)` without a feature axis, then
flattening adds an extra channel dimension and output shape is `(batch, 1)`.

| Args | |

|  |  |
| --- | --- |
| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, ..., channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, ...)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

#### Example:

```
>>> x = keras.Input(shape=(10, 64))
>>> y = keras.layers.Flatten()(x)
>>> y.shape
(None, 640)
```

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L191-L213)

```
@classmethod
from_config(
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```