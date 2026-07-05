# tf.keras.layers.TimeDistributed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/TimeDistributed](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/TimeDistributed)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/time_distributed.py#L10-L115) |

This wrapper allows to apply a layer to every temporal slice of an input.

Inherits From: [`Wrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Wrapper), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.TimeDistributed(
    layer, **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Load video data](https://tensorflow.google.cn/tutorials/load_data/video) |

Every input should be at least 3D, and the dimension of index one of the
first input will be considered to be the temporal dimension.

Consider a batch of 32 video samples, where each sample is a 128x128 RGB
image with `channels_last` data format, across 10 timesteps.
The batch input shape is `(32, 10, 128, 128, 3)`.

You can then use `TimeDistributed` to apply the same `Conv2D` layer to each
of the 10 timesteps, independently:

```
>>> inputs = layers.Input(shape=(10, 128, 128, 3), batch_size=32)
>>> conv_2d_layer = layers.Conv2D(64, (3, 3))
>>> outputs = layers.TimeDistributed(conv_2d_layer)(inputs)
>>> outputs.shape
(32, 10, 126, 126, 64)
```

Because `TimeDistributed` applies the same instance of `Conv2D` to each of
the timestamps, the same set of weights are used at each timestamp.

| Args | |

|  |  |
| --- | --- |
| `layer` | a [`keras.layers.Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer) instance. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | Input tensor of shape (batch, time, ...) or nested tensors, and each of which has shape (batch, time, ...). |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the wrapped layer (only if the layer supports this argument). |
| `mask` | Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked. This argument is passed to the wrapped layer (only if the layer supports this argument). |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/wrapper.py#L41-L47)

```
@classmethod
from_config(
    config, custom_objects=None
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