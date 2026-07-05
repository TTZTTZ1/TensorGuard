# tf.keras.layers.UpSampling2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/UpSampling2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/UpSampling2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/up_sampling2d.py#L9-L169) |

Upsampling layer for 2D inputs.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.UpSampling2D(
    size=(2, 2), data_format=None, interpolation='nearest', **kwargs
)
```

The implementation uses interpolative resizing, given the resize method
(specified by the `interpolation` argument). Use `interpolation=nearest`
to repeat the rows and columns of the data.

#### Example:

```
>>> input_shape = (2, 2, 1, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> print(x)
[[[[ 0  1  2]]
  [[ 3  4  5]]]
 [[[ 6  7  8]]
  [[ 9 10 11]]]]
>>> y = keras.layers.UpSampling2D(size=(1, 2))(x)
>>> print(y)
[[[[ 0  1  2]
   [ 0  1  2]]
  [[ 3  4  5]
   [ 3  4  5]]]
 [[[ 6  7  8]
   [ 6  7  8]]
  [[ 9 10 11]
   [ 9 10 11]]]]
```

| Args | |

|  |  |
| --- | --- |
| `size` | Int, or tuple of 2 integers. The upsampling factors for rows and columns. |
| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists) else `"channels_last"`. Defaults to `"channels_last"`. |
| `interpolation` | A string, one of `"bicubic"`, `"bilinear"`, `"lanczos3"`, `"lanczos5"`, `"nearest"`. |

| Input shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, rows, cols, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, rows, cols)`

| Output shape | |
| 4D tensor with shape: | |

* If `data_format` is `"channels_last"`:
  `(batch_size, upsampled_rows, upsampled_cols, channels)`
* If `data_format` is `"channels_first"`:
  `(batch_size, channels, upsampled_rows, upsampled_cols)`

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