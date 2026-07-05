# tf.keras.layers.RandomContrast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomContrast](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomContrast)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/random_contrast.py#L6-L98) |

A preprocessing layer which randomly adjusts contrast during training.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RandomContrast(
    factor, seed=None, **kwargs
)
```

This layer will randomly adjust the contrast of an image or images
by a random factor. Contrast is adjusted independently
for each channel of each image during training.

For each channel, this layer computes the mean of the image pixels in the
channel and then adjusts each component `x` of each pixel to
`(x - mean) * contrast_factor + mean`.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
in integer or floating point dtype.
By default, the layer will output floats.

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

`(..., height, width, channels)`, in `"channels_last"` format.

| Args | |

|  |  |
| --- | --- |
| `factor` | a positive float represented as fraction of value, or a tuple of size 2 representing lower and upper bound. When represented as a single float, lower = upper. The contrast factor will be randomly picked between `[1.0 - lower, 1.0 + upper]`. For any pixel x in the channel, the output will be `(x - mean) * factor + mean` where `mean` is the mean value of the channel. |
| `seed` | Integer. Used to create a random seed. |

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