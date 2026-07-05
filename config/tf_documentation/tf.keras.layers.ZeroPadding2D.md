# tf.keras.layers.ZeroPadding2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ZeroPadding2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ZeroPadding2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/zero_padding2d.py#L9-L119) |

Zero-padding layer for 2D input (e.g. picture).

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.ZeroPadding2D(
    padding=(1, 1), data_format=None, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Pruning for on-device inference w/ XNNPACK](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_for_on_device_inference) | * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

This layer can add rows and columns of zeros at the top, bottom, left and
right side of an image tensor.

#### Example:

```
>>> input_shape = (1, 1, 2, 2)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> x
[[[[0 1]
   [2 3]]]]
>>> y = keras.layers.ZeroPadding2D(padding=1)(x)
>>> y
[[[[0 0]
   [0 0]
   [0 0]
   [0 0]]
  [[0 0]
   [0 1]
   [2 3]
   [0 0]]
  [[0 0]
   [0 0]
   [0 0]
   [0 0]]]]
```

| Args | |

|  |  |
| --- | --- |
| `padding` | Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints. |

* If int: the same symmetric padding is applied to height and width.
* If tuple of 2 ints: interpreted as two different symmetric padding
  values for height and width:
  `(symmetric_height_pad, symmetric_width_pad)`.
* If tuple of 2 tuples of 2 ints: interpreted as
  `((top_pad, bottom_pad), (left_pad, right_pad))`.| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

| Input shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, height, width, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, height, width)`

| Output shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, padded_height, padded_width, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, padded_height, padded_width)`

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