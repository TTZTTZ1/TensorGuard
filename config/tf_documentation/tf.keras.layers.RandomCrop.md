# tf.keras.layers.RandomCrop

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomCrop](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomCrop)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/random_crop.py#L8-L173) |

A preprocessing layer which randomly crops images during training.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RandomCrop(
    height, width, seed=None, data_format=None, name=None, **kwargs
)
```

During training, this layer will randomly choose a location to crop images
down to a target size. The layer will crop all the images in the same batch
to the same cropping location.

At inference time, and during training if an input image is smaller than the
target size, the input will be resized and cropped so as to return the
largest possible window in the image that matches the target aspect ratio.
If you need to apply random cropping at inference time, set `training` to
True when calling the layer.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
of integer or floating point dtype. By default, the layer will output
floats.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Input shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., height, width, channels)`, in `"channels_last"` format.

| Output shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., target_height, target_width, channels)`.

| Args | |

|  |  |
| --- | --- |
| `height` | Integer, the height of the output shape. |
| `width` | Integer, the width of the output shape. |
| `seed` | Integer. Used to create a random seed. |
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