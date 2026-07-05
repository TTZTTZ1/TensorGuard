# tf.keras.layers.SpatialDropout2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SpatialDropout2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SpatialDropout2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/regularization/spatial_dropout.py#L71-L130) |

Spatial 2D version of Dropout.

Inherits From: [`Dropout`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dropout), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.SpatialDropout2D(
    rate, data_format=None, seed=None, name=None, dtype=None
)
```

This version performs the same function as Dropout, however, it drops
entire 2D feature maps instead of individual elements. If adjacent pixels
within feature maps are strongly correlated (as is normally the case in
early convolution layers) then regular dropout will not regularize the
activations and will otherwise just result in an effective learning rate
decrease. In this case, `SpatialDropout2D` will help promote independence
between feature maps and should be used instead.

| Args | |

|  |  |
| --- | --- |
| `rate` | Float between 0 and 1. Fraction of the input units to drop. |
| `data_format` | `"channels_first"` or `"channels_last"`. In `"channels_first"` mode, the channels dimension (the depth) is at index 1, in `"channels_last"` mode is it at index 3. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | A 4D tensor. |
| `training` | Python boolean indicating whether the layer should behave in training mode (applying dropout) or in inference mode (pass-through). |

| Input shape | |
| 4D tensor with shape: `(samples, channels, rows, cols)` if data\_format='channels\_first' or 4D tensor with shape: `(samples, rows, cols, channels)` if data\_format='channels\_last'. | |

Output shape: Same as input.

#### Reference:

* [Tompson et al., 2014](https://arxiv.org/abs/1411.4280)

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