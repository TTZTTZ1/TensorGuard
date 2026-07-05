# tf.keras.layers.SeparableConvolution2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SeparableConvolution2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SeparableConvolution2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/convolutional/separable_conv2d.py#L5-L142) |

2D separable convolution layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.SeparableConvolution2D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SeparableConv2D)

```
tf.keras.layers.SeparableConv2D(
    filters,
    kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1),
    depth_multiplier=1,
    activation=None,
    use_bias=True,
    depthwise_initializer='glorot_uniform',
    pointwise_initializer='glorot_uniform',
    bias_initializer='zeros',
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    **kwargs
)
```

This layer performs a depthwise convolution that acts separately on
channels, followed by a pointwise convolution that mixes channels.
If `use_bias` is True and a bias initializer is provided,
it adds a bias vector to the output. It then optionally applies an
activation function to produce the final output.

| Args | |

|  |  |
| --- | --- |
| `filters` | int, the dimensionality of the output space (i.e. the number of filters in the pointwise convolution). |
| `kernel_size` | int or tuple/list of 2 integers, specifying the size of the depthwise convolution window. |
| `strides` | int or tuple/list of 2 integers, specifying the stride length of the depthwise convolution. If only one int is specified, the same stride size will be used for all dimensions. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. If only one int is specified, the same dilation rate will be used for all dimensions. |
| `depth_multiplier` | The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `input_channel * depth_multiplier`. |
| `activation` | Activation function. If `None`, no activation is applied. |
| `use_bias` | bool, if `True`, bias will be added to the output. |
| `depthwise_initializer` | An initializer for the depthwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used. |
| `pointwise_initializer` | An initializer for the pointwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used. |
| `bias_initializer` | An initializer for the bias vector. If None, the default initializer ('"zeros"') will be used. |
| `depthwise_regularizer` | Optional regularizer for the depthwise convolution kernel. |
| `pointwise_regularizer` | Optional regularizer for the pointwise convolution kernel. |
| `bias_regularizer` | Optional regularizer for the bias vector. |
| `activity_regularizer` | Optional regularizer function for the output. |
| `depthwise_constraint` | Optional projection function to be applied to the depthwise kernel after being updated by an `Optimizer` (e.g. used for norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). |
| `pointwise_constraint` | Optional projection function to be applied to the pointwise kernel after being updated by an `Optimizer`. |
| `bias_constraint` | Optional projection function to be applied to the bias after being updated by an `Optimizer`. |

#### Input shape:

* If `data_format="channels_last"`:
  A 4D tensor with shape: `(batch_size, height, width, channels)`
* If `data_format="channels_first"`:
  A 4D tensor with shape: `(batch_size, channels, height, width)`

#### Output shape:

* If `data_format="channels_last"`:
  A 4D tensor with shape: `(batch_size, new_height, new_width, filters)`
* If `data_format="channels_first"`:
  A 4D tensor with shape: `(batch_size, filters, new_height, new_width)`

| Returns | |
| A 4D tensor representing `activation(separable_conv2d(inputs, kernel) + bias)`. | |

#### Example:

```
>>> x = np.random.rand(4, 10, 10, 12)
>>> y = keras.layers.SeparableConv2D(3, 4, 3, 2, activation='relu')(x)
>>> print(y.shape)
(4, 4, 4, 4)
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