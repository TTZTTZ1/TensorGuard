# tf.keras.layers.Cropping2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Cropping2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Cropping2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/cropping2d.py#L8-L224) |

Cropping layer for 2D input (e.g. picture).

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Cropping2D(
    cropping=((0, 0), (0, 0)), data_format=None, **kwargs
)
```

It crops along spatial dimensions, i.e. height and width.

#### Example:

```
>>> input_shape = (2, 28, 28, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> y = keras.layers.Cropping2D(cropping=((2, 2), (4, 4)))(x)
>>> y.shape
(2, 24, 20, 3)
```

| Args | |

|  |  |
| --- | --- |
| `cropping` | Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints. |

* If int: the same symmetric cropping is applied to height and
  width.
* If tuple of 2 ints: interpreted as two different symmetric
  cropping values for height and width:
  `(symmetric_height_crop, symmetric_width_crop)`.
* If tuple of 2 tuples of 2 ints: interpreted as
  `((top_crop, bottom_crop), (left_crop, right_crop))`.| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

| Input shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, height, width, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, height, width)`

| Output shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, cropped_height, cropped_width, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, cropped_height, cropped_width)`

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