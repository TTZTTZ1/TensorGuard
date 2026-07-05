# tf.keras.layers.Convolution3DTranspose

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Convolution3DTranspose](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Convolution3DTranspose)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/convolutional/conv3d_transpose.py#L5-L136) |

3D transposed convolution layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Convolution3DTranspose`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Conv3DTranspose)

```
tf.keras.layers.Conv3DTranspose(
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1, 1),
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

The need for transposed convolutions generally arise from the desire to use
a transformation going in the opposite direction of a normal convolution,
i.e., from something that has the shape of the output of some convolution
to something that has the shape of its input while maintaining a
connectivity pattern that is compatible with said convolution.

| Args | |

|  |  |
| --- | --- |
| `filters` | int, the dimension of the output space (the number of filters in the transposed convolution). |
| `kernel_size` | int or tuple/list of 1 integer, specifying the size of the transposed convolution window. |
| `strides` | int or tuple/list of 1 integer, specifying the stride length of the transposed convolution. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 1 integers, specifying the dilation rate to use for dilated transposed convolution. |
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

#### References:

* [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285v1)
* [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)

#### Example:

```
>>> x = np.random.rand(4, 10, 8, 12, 128)
>>> y = keras.layers.Conv3DTranspose(32, 2, 2, activation='relu')(x)
>>> print(y.shape)
(4, 20, 16, 24, 32)
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