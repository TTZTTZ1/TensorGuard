# tf.keras.layers.Convolution3D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Convolution3D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Convolution3D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/convolutional/conv3d.py#L5-L132) |

3D convolution layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Convolution3D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Conv3D)

```
tf.keras.layers.Conv3D(
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1, 1),
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs
)
```

This layer creates a convolution kernel that is convolved with the layer
input over a single spatial (or temporal) dimension to produce a tensor of
outputs. If `use_bias` is True, a bias vector is created and added to the
outputs. Finally, if `activation` is not `None`, it is applied to the
outputs as well.

| Args | |

|  |  |
| --- | --- |
| `filters` | int, the dimension of the output space (the number of filters in the convolution). |
| `kernel_size` | int or tuple/list of 3 integer, specifying the size of the convolution window. |
| `strides` | int or tuple/list of 3 integer, specifying the stride length of the convolution. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. |
| `groups` | A positive int specifying the number of groups in which the input is split along the channel axis. Each group is convolved separately with `filters // groups` filters. The output is the concatenation of all the `groups` results along the channel axis. Input channels and `filters` must both be divisible by `groups`. |
| `activation` | Activation function. If `None`, no activation is applied. |
| `use_bias` | bool, if `True`, bias will be added to the output. |
| `kernel_initializer` | Initializer for the convolution kernel. If `None`, the default initializer (`"glorot_uniform"`) will be used. |
| `bias_initializer` | Initializer for the bias vector. If `None`, the default initializer (`"zeros"`) will be used. |
| `kernel_regularizer` | Optional regularizer for the convolution kernel. |
| `bias_regularizer` | Optional regularizer for the bias vector. |
| `activity_regularizer` | Optional regularizer function for the output. |
| `kernel_constraint` | Optional projection function to be applied to the kernel after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `bias_constraint` | Optional projection function to be applied to the bias after being updated by an `Optimizer`. |

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
  `(batch_size, new_spatial_dim1, new_spatial_dim2, new_spatial_dim3,
  filters)`
* If `data_format="channels_first"`:
  5D tensor with shape:
  `(batch_size, filters, new_spatial_dim1, new_spatial_dim2,
  new_spatial_dim3)`

| Returns | |
| A 5D tensor representing `activation(conv3d(inputs, kernel) + bias)`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | when both `strides > 1` and `dilation_rate > 1`. |

#### Example:

```
>>> x = np.random.rand(4, 10, 10, 10, 128)
>>> y = keras.layers.Conv3D(32, 3, activation='relu')(x)
>>> print(y.shape)
(4, 8, 8, 8, 32)
```

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `kernel` |  |

|  |  |
| --- | --- |
| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `convolution_op`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/convolutional/base_conv.py#L232-L240)

```
convolution_op(
    inputs, kernel
)
```

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/convolutional/base_conv.py#L270-L304)

```
enable_lora(
    rank, a_initializer='he_uniform', b_initializer='zeros'
)
```

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