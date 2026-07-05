# tf.keras.layers.GlobalMaxPool2D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GlobalMaxPool2D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GlobalMaxPool2D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/pooling/global_max_pooling2d.py#L6-L68) |

Global max pooling operation for 2D data.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.GlobalMaxPooling2D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GlobalMaxPool2D)

```
tf.keras.layers.GlobalMaxPool2D(
    data_format=None, keepdims=False, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Customizing what happens in `fit()`](https://tensorflow.google.cn/guide/keras/customizing_what_happens_in_fit) |

| Args | |

|  |  |
| --- | --- |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, features, height, weight)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `keepdims` | A boolean, whether to keep the temporal dimension or not. If `keepdims` is `False` (default), the rank of the tensor is reduced for spatial dimensions. If `keepdims` is `True`, the spatial dimension are retained with length 1. The behavior is the same as for [`tf.reduce_mean`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_mean) or `np.mean`. |

#### Input shape:

* If `data_format='channels_last'`:
  4D tensor with shape:
  `(batch_size, height, width, channels)`
* If `data_format='channels_first'`:
  4D tensor with shape:
  `(batch_size, channels, height, width)`

#### Output shape:

* If `keepdims=False`:
  2D tensor with shape `(batch_size, channels)`.
* If `keepdims=True`:
  + If `data_format="channels_last"`:
    4D tensor with shape `(batch_size, 1, 1, channels)`
  + If `data_format="channels_first"`:
    4D tensor with shape `(batch_size, channels, 1, 1)`

#### Example:

```
>>> x = np.random.rand(2, 4, 5, 3)
>>> y = keras.layers.GlobalMaxPooling2D()(x)
>>> y.shape
(2, 3)
```

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