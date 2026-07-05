# tf.keras.layers.CenterCrop

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/CenterCrop](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/CenterCrop)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/center_crop.py#L7-L144) |

A preprocessing layer which crops images.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.CenterCrop(
    height, width, data_format=None, **kwargs
)
```

This layers crops the central portion of the images to a target size. If an
image is smaller than the target size, it will be resized and cropped
so as to return the largest possible window in the image that matches
the target aspect ratio.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`).

| Input shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., height, width, channels)`, in `"channels_last"` format,
or `(..., channels, height, width)`, in `"channels_first"` format.

| Output shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., target_height, target_width, channels)`,
or `(..., channels, target_height, target_width)`,
in `"channels_first"` format.

If the input height/width is even and the target height/width is odd (or
inversely), the input image is left-padded by 1 pixel.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Args | |

|  |  |
| --- | --- |
| `height` | Integer, the height of the output shape. |
| `width` | Integer, the width of the output shape. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

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