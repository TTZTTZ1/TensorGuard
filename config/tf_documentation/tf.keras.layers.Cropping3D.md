# tf.keras.layers.Cropping3D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Cropping3D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Cropping3D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/cropping3d.py#L8-L284) |

Cropping layer for 3D data (e.g. spatial or spatio-temporal).

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Cropping3D(
    cropping=((1, 1), (1, 1), (1, 1)), data_format=None, **kwargs
)
```

#### Example:

```
>>> input_shape = (2, 28, 28, 10, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> y = keras.layers.Cropping3D(cropping=(2, 4, 2))(x)
>>> y.shape
(2, 24, 20, 6, 3)
```

| Args | |

|  |  |
| --- | --- |
| `cropping` | Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints. |

* If int: the same symmetric cropping is applied to depth, height,
  and width.
* If tuple of 3 ints: interpreted as three different symmetric
  cropping values for depth, height, and width:
  `(symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop)`.
* If tuple of 3 tuples of 2 ints: interpreted as
  `((left_dim1_crop, right_dim1_crop), (left_dim2_crop,
  right_dim2_crop), (left_dim3_crop, right_dim3_crop))`.| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

| Input shape | |
| 5D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, first_axis_to_crop, second_axis_to_crop,
  third_axis_to_crop, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, first_axis_to_crop, second_axis_to_crop,
  third_axis_to_crop)`

| Output shape | |
| 5D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, first_cropped_axis, second_cropped_axis,
  third_cropped_axis, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, first_cropped_axis, second_cropped_axis,
  third_cropped_axis)`

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