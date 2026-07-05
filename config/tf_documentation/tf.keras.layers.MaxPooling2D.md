# tf.keras.layers.MaxPooling2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPooling2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPooling2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/pooling/max_pooling2d.py#L5-L107) |

Max pooling operation for 2D spatial data.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.MaxPooling2D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool2D)

```
tf.keras.layers.MaxPool2D(
    pool_size=(2, 2),
    strides=None,
    padding='valid',
    data_format=None,
    name=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Sparse weights using structural pruning](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Load and preprocess images](https://tensorflow.google.cn/tutorials/load_data/images) * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Convolutional Neural Network (CNN)](https://tensorflow.google.cn/tutorials/images/cnn) |

Downsamples the input along its spatial dimensions (height and width)
by taking the maximum value over an input window
(of size defined by `pool_size`) for each channel of the input.
The window is shifted by `strides` along each dimension.

The resulting output when using the `"valid"` padding option has a spatial
shape (number of rows or columns) of:
`output_shape = math.floor((input_shape - pool_size) / strides) + 1`
(when `input_shape >= pool_size`)

The resulting output shape when using the `"same"` padding option is:
`output_shape = math.floor((input_shape - 1) / strides) + 1`

| Args | |

|  |  |
| --- | --- |
| `pool_size` | int or tuple of 2 integers, factors by which to downscale (dim1, dim2). If only one integer is specified, the same window length will be used for all dimensions. |
| `strides` | int or tuple of 2 integers, or None. Strides values. If None, it will default to `pool_size`. If only one int is specified, the same stride size will be used for all dimensions. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

#### Input shape:

* If `data_format="channels_last"`:
  4D tensor with shape `(batch_size, height, width, channels)`.
* If `data_format="channels_first"`:
  4D tensor with shape `(batch_size, channels, height, width)`.

#### Output shape:

* If `data_format="channels_last"`:
  4D tensor with shape
  `(batch_size, pooled_height, pooled_width, channels)`.
* If `data_format="channels_first"`:
  4D tensor with shape
  `(batch_size, channels, pooled_height, pooled_width)`.

#### Examples:

`strides=(1, 1)` and `padding="valid"`:

```
>>> x = np.array([[1., 2., 3.],
...               [4., 5., 6.],
...               [7., 8., 9.]])
>>> x = np.reshape(x, [1, 3, 3, 1])
>>> max_pool_2d = keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(1, 1), padding="valid")
>>> max_pool_2d(x)
```

`strides=(2, 2)` and `padding="valid"`:

```
>>> x = np.array([[1., 2., 3., 4.],
...               [5., 6., 7., 8.],
...               [9., 10., 11., 12.]])
>>> x = np.reshape(x, [1, 3, 4, 1])
>>> max_pool_2d = keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(2, 2), padding="valid")
>>> max_pool_2d(x)
```

`stride=(1, 1)` and `padding="same"`:

```
>>> x = np.array([[1., 2., 3.],
...               [4., 5., 6.],
...               [7., 8., 9.]])
>>> x = np.reshape(x, [1, 3, 3, 1])
>>> max_pool_2d = keras.layers.MaxPooling2D(pool_size=(2, 2),
...    strides=(1, 1), padding="same")
>>> max_pool_2d(x)
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