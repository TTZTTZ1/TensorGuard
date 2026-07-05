# tf.keras.layers.RandomTranslation

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomTranslation](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomTranslation)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/random_translation.py#L7-L251) |

A preprocessing layer which randomly translates images during training.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RandomTranslation(
    height_factor,
    width_factor,
    fill_mode='reflect',
    interpolation='bilinear',
    seed=None,
    fill_value=0.0,
    data_format=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Retraining an Image Classifier](https://tensorflow.google.cn/hub/tutorials/tf2_image_retraining) |

This layer will apply random translations to each image during training,
filling empty space according to `fill_mode`.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
of integer or floating point dtype. By default, the layer will output
floats.

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
| `height_factor` | a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for shifting vertically. A negative value means shifting image up, while a positive value means shifting image down. When represented as a single positive float, this value is used for both the upper and lower bound. For instance, `height_factor=(-0.2, 0.3)` results in an output shifted by a random amount in the range `[-20%, +30%]`. `height_factor=0.2` results in an output height shifted by a random amount in the range `[-20%, +20%]`. |
| `width_factor` | a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for shifting horizontally. A negative value means shifting image left, while a positive value means shifting image right. When represented as a single positive float, this value is used for both the upper and lower bound. For instance, `width_factor=(-0.2, 0.3)` results in an output shifted left by 20%, and shifted right by 30%. `width_factor=0.2` results in an output height shifted left or right by 20%. |
| `fill_mode` | Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`. |

* `"reflect"`: `(d c b a | a b c d | d c b a)`
  The input is extended by reflecting about the edge of the last
  pixel.
* `"constant"`: `(k k k k | a b c d | k k k k)`
  The input is extended by filling all values beyond
  the edge with the same constant value k specified by
  `fill_value`.
* `"wrap"`: `(a b c d | a b c d | a b c d)`
  The input is extended by wrapping around to the opposite edge.
* `"nearest"`: `(a a a a | a b c d | d d d d)`
  The input is extended by the nearest pixel.
  Note that when using torch backend, `"reflect"` is redirected to
  `"mirror"` `(c d c b | a b c d | c b a b)` because torch does not
  support `"reflect"`.
  Note that torch backend does not support `"wrap"`.| `interpolation` | Interpolation mode. Supported values: `"nearest"`, `"bilinear"`. |
  | `seed` | Integer. Used to create a random seed. |
  | `fill_value` | a float represents the value to be filled outside the boundaries when `fill_mode="constant"`. |
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