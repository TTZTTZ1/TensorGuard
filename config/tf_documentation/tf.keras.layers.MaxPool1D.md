# tf.keras.layers.MaxPool1D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool1D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool1D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/pooling/max_pooling1d.py#L5-L91) |

Max pooling operation for 1D temporal data.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.MaxPooling1D`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/MaxPool1D)

```
tf.keras.layers.MaxPool1D(
    pool_size=2,
    strides=None,
    padding='valid',
    data_format=None,
    name=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Using Counterfactual Logit Pairing with Keras](https://tensorflow.google.cn/responsible_ai/model_remediation/counterfactual/guide/counterfactual_keras) | * [Wiki Talk Comments Toxicity Prediction](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

Downsamples the input representation by taking the maximum value over a
spatial window of size `pool_size`. The window is shifted by `strides`.

The resulting output when using the `"valid"` padding option has a shape of:
`output_shape = (input_shape - pool_size + 1) / strides)`.

The resulting output shape when using the `"same"` padding option is:
`output_shape = input_shape / strides`

| Args | |

|  |  |
| --- | --- |
| `pool_size` | int, size of the max pooling window. |
| `strides` | int or None. Specifies how much the pooling window moves for each pooling step. If None, it will default to `pool_size`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

#### Input shape:

* If `data_format="channels_last"`:
  3D tensor with shape `(batch_size, steps, features)`.
* If `data_format="channels_first"`:
  3D tensor with shape `(batch_size, features, steps)`.

#### Output shape:

* If `data_format="channels_last"`:
  3D tensor with shape `(batch_size, downsampled_steps, features)`.
* If `data_format="channels_first"`:
  3D tensor with shape `(batch_size, features, downsampled_steps)`.

#### Examples:

`strides=1` and `padding="valid"`:

```
>>> x = np.array([1., 2., 3., 4., 5.])
>>> x = np.reshape(x, [1, 5, 1])
>>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2,
...    strides=1, padding="valid")
>>> max_pool_1d(x)
```

`strides=2` and `padding="valid"`:

```
>>> x = np.array([1., 2., 3., 4., 5.])
>>> x = np.reshape(x, [1, 5, 1])
>>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2,
...    strides=2, padding="valid")
>>> max_pool_1d(x)
```

`strides=1` and `padding="same"`:

```
>>> x = np.array([1., 2., 3., 4., 5.])
>>> x = np.reshape(x, [1, 5, 1])
>>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2,
...    strides=1, padding="same")
>>> max_pool_1d(x)
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