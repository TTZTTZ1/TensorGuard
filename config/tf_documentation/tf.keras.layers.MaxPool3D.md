# tf.keras.layers.MaxPool3D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool3D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool3D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/pooling/max_pooling3d.py#L5-L83) |

Max pooling operation for 3D data (spatial or spatio-temporal).

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.MaxPooling3D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool3D)

```
tf.keras.layers.MaxPool3D(
    pool_size=(2, 2, 2),
    strides=None,
    padding='valid',
    data_format=None,
    name=None,
    **kwargs
)
```

Downsamples the input along its spatial dimensions (depth, height, and
width) by taking the maximum value over an input window (of size defined by
`pool_size`) for each channel of the input. The window is shifted by
`strides` along each dimension.

| Args | |

|  |  |
| --- | --- |
| `pool_size` | int or tuple of 3 integers, factors by which to downscale (dim1, dim2, dim3). If only one integer is specified, the same window length will be used for all dimensions. |
| `strides` | int or tuple of 3 integers, or None. Strides values. If None, it will default to `pool_size`. If only one int is specified, the same stride size will be used for all dimensions. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

#### Input shape:

* If `data_format="channels_last"`:
  5D tensor with shape:
  `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
* If `data_format="channels_first"`:
  5D tensor with shape:
  `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

#### Output shape:

* If `data_format="channels_last"`:
  5D tensor with shape:
  `(batch_size, pooled_dim1, pooled_dim2, pooled_dim3, channels)`
* If `data_format="channels_first"`:
  5D tensor with shape:
  `(batch_size, channels, pooled_dim1, pooled_dim2, pooled_dim3)`

#### Example:

```
depth = 30
height = 30
width = 30
channels = 3

inputs = keras.layers.Input(shape=(depth, height, width, channels))
layer = keras.layers.MaxPooling3D(pool_size=3)
outputs = layer(inputs)  # Shape: (batch_size, 10, 10, 10, 3)
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