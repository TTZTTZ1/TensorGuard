# tf.keras.layers.Rescaling

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Rescaling](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Rescaling)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/rescaling.py#L6-L63) |

A preprocessing layer which rescales input values to a new range.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Rescaling(
    scale, offset=0.0, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Load and preprocess images](https://tensorflow.google.cn/tutorials/load_data/images) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Transfer learning with TensorFlow Hub](https://tensorflow.google.cn/tutorials/images/transfer_learning_with_hub) |

This layer rescales every value of an input (often an image) by multiplying
by `scale` and adding `offset`.

#### For instance:

1. To rescale an input in the `[0, 255]` range
   to be in the `[0, 1]` range, you would pass `scale=1./255`.
2. To rescale an input in the `[0, 255]` range to be in the `[-1, 1]` range,
   you would pass `scale=1./127.5, offset=-1`.

The rescaling is applied both during training and inference. Inputs can be
of integer or floating point dtype, and by default the layer will output
floats.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Args | |

|  |  |
| --- | --- |
| `scale` | Float, the scale to apply to the inputs. |
| `offset` | Float, the offset to apply to the inputs. |
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