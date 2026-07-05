# tf.keras.regularizers.L1

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L1](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L1)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L213-L239) |

A regularizer that applies a L1 regularization penalty.

Inherits From: [`Regularizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Regularizer)

#### View aliases

**Main aliases**

[`tf.keras.regularizers.l1`](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L1)

```
tf.keras.regularizers.L1(
    l1=0.01
)
```

The L1 regularization penalty is computed as:
`loss = l1 * reduce_sum(abs(x))`

L1 may be passed to a layer as a string identifier:

```
>>> dense = Dense(3, kernel_regularizer='l1')
```

In this case, the default value used is `l1=0.01`.

| Arguments | |

|  |  |
| --- | --- |
| `l1` | float, L1 regularization factor. |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L127-L145)

```
@classmethod
from_config(
    config
)
```

Creates a regularizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same regularizer from the config
dictionary.

This method is used by Keras `model_to_estimator`, saving and
loading models to HDF5 formats, Keras model cloning, some visualization
utilities, and exporting models to and from JSON.

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A regularizer instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L238-L239)

```
get_config()
```

Returns the config of the regularizer.

An regularizer config is a Python dictionary (serializable)
containing all configuration parameters of the regularizer.
The same regularizer can be reinstantiated later
(without any saved state) from this configuration.

This method is optional if you are just training and executing models,
exporting to and from SavedModels, or using weight checkpoints.

This method is required for Keras `model_to_estimator`, saving and
loading models to HDF5 formats, Keras model cloning, some visualization
utilities, and exporting models to and from JSON.

| Returns | |
| Python dictionary. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L235-L236)

```
__call__(
    x
)
```

Compute a regularization penalty from an input tensor.