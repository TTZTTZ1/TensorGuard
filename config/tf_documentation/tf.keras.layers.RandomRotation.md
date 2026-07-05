# tf.keras.layers.RandomRotation

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomRotation](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomRotation)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/random_rotation.py#L9-L254) |

A preprocessing layer which randomly rotates images during training.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RandomRotation(
    factor,
    fill_mode='reflect',
    interpolation='bilinear',
    seed=None,
    fill_value=0.0,
    value_range=(0, 255),
    data_format=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Retraining an Image Classifier](https://tensorflow.google.cn/hub/tutorials/tf2_image_retraining) |

This layer will apply random rotations to each image, filling empty space
according to `fill_mode`.

By default, random rotations are only applied during training.
At inference time, the layer does nothing. If you need to apply random
rotations at inference time, pass `training=True` when calling the layer.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
of integer or floating point dtype.
By default, the layer will output floats.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Input shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., height, width, channels)`, in `"channels_last"` format

| Output shape | |

|  |  |
| --- | --- |
| `3D` | `unbatched) or 4D (batched) tensor with shape` |

`(..., height, width, channels)`, in `"channels_last"` format

| Args | |

|  |  |
| --- | --- |
| `factor` | a float represented as fraction of 2 Pi, or a tuple of size 2 representing lower and upper bound for rotating clockwise and counter-clockwise. A positive values means rotating counter clock-wise, while a negative value means clock-wise. When represented as a single float, this value is used for both the upper and lower bound. For instance, `factor=(-0.2, 0.3)` results in an output rotation by a random amount in the range `[-20% * 2pi, 30% * 2pi]`. `factor=0.2` results in an output rotating by a random amount in the range `[-20% * 2pi, 20% * 2pi]`. |
| `fill_mode` | Points outside the boundaries of the input are filled according to the given mode (one of `{"constant", "reflect", "wrap", "nearest"}`). |

* *reflect*: `(d c b a | a b c d | d c b a)`
  The input is extended by reflecting about
  the edge of the last pixel.
* *constant*: `(k k k k | a b c d | k k k k)`
  The input is extended by
  filling all values beyond the edge with
  the same constant value k = 0.
* *wrap*: `(a b c d | a b c d | a b c d)` The input is extended by
  wrapping around to the opposite edge.
* *nearest*: `(a a a a | a b c d | d d d d)`
  The input is extended by the nearest pixel.| `interpolation` | Interpolation mode. Supported values: `"nearest"`, `"bilinear"`. |
  | `seed` | Integer. Used to create a random seed. |
  | `fill_value` | a float represents the value to be filled outside the boundaries when `fill_mode="constant"`. |

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