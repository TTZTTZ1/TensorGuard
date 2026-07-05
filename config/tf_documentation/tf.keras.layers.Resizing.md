# tf.keras.layers.Resizing

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Resizing](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Resizing)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/resizing.py#L6-L127) |

A preprocessing layer which resizes images.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Resizing(
    height,
    width,
    interpolation='bilinear',
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode='constant',
    fill_value=0.0,
    data_format=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

This layer resizes an image input to a target height and width. The input
should be a 4D (batched) or 3D (unbatched) tensor in `"channels_last"`
format. Input pixel values can be of any range
(e.g. `[0., 1.)` or `[0, 255]`).

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

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Args | |

|  |  |
| --- | --- |
| `height` | Integer, the height of the output shape. |
| `width` | Integer, the width of the output shape. |
| `interpolation` | String, the interpolation method. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"lanczos3"`, `"lanczos5"`. Defaults to `"bilinear"`. |
| `crop_to_aspect_ratio` | If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved. |
| `pad_to_aspect_ratio` | If `True`, pad the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be evenly padded on the short side. |
| `fill_mode` | When using `pad_to_aspect_ratio=True`, padded areas are filled according to the given mode. Only `"constant"` is supported at this time (fill with constant value, equal to `fill_value`). |
| `fill_value` | Float. Padding value to use when `pad_to_aspect_ratio=True`. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

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