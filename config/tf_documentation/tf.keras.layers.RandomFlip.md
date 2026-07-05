# tf.keras.layers.RandomFlip

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomFlip](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RandomFlip)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/random_flip.py#L10-L97) |

A preprocessing layer which randomly flips images during training.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RandomFlip(
    mode=HORIZONTAL_AND_VERTICAL, seed=None, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Image segmentation](https://tensorflow.google.cn/tutorials/images/segmentation) * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Retraining an Image Classifier](https://tensorflow.google.cn/hub/tutorials/tf2_image_retraining) |

This layer will flip the images horizontally and or vertically based on the
`mode` attribute. During inference time, the output will be identical to
input. Call the layer with `training=True` to flip the input.
Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and
of integer or floating point dtype.
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
| `mode` | String indicating which flip mode to use. Can be `"horizontal"`, `"vertical"`, or `"horizontal_and_vertical"`. `"horizontal"` is a left-right flip and `"vertical"` is a top-bottom flip. Defaults to `"horizontal_and_vertical"` |
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