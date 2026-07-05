# tf.keras.regularizers.Regularizer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/Regularizer](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/Regularizer)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L8-L165) |

Regularizer base class.

#### View aliases

**Main aliases**

[`tf.keras.regularizers.Regularizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Regularizer)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Regularizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Regularizer)

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) |

Regularizers allow you to apply penalties on layer parameters or layer
activity during optimization. These penalties are summed into the loss
function that the network optimizes.

Regularization penalties are applied on a per-layer basis. The exact API
will depend on the layer, but many layers (e.g. `Dense`, `Conv1D`, `Conv2D`
and `Conv3D`) have a unified API.

These layers expose 3 keyword arguments:

* `kernel_regularizer`: Regularizer to apply a penalty on the layer's kernel
* `bias_regularizer`: Regularizer to apply a penalty on the layer's bias
* `activity_regularizer`: Regularizer to apply a penalty on the layer's
  output

All layers (including custom layers) expose `activity_regularizer` as a
settable property, whether or not it is in the constructor arguments.

The value returned by the `activity_regularizer` is divided by the input
batch size so that the relative weighting between the weight regularizers
and the activity regularizers does not change with the batch size.

You can access a layer's regularization penalties by calling `layer.losses`
after calling the layer on inputs.

## Example

```
>>> layer = Dense(
...     5, input_dim=5,
...     kernel_initializer='ones',
...     kernel_regularizer=L1(0.01),
...     activity_regularizer=L2(0.01))
>>> tensor = ops.ones(shape=(5, 5)) * 2.0
>>> out = layer(tensor)
```

```
>>> # The kernel regularization term is 0.25
>>> # The activity regularization term (after dividing by the batch size)
>>> # is 5
>>> ops.sum(layer.losses)
5.25
```

## Available penalties

```
L1(0.3)  # L1 Regularization Penalty
L2(0.1)  # L2 Regularization Penalty
L1L2(l1=0.01, l2=0.01)  # L1 + L2 penalties
```

## Directly calling a regularizer

Compute a regularization loss on a tensor by directly calling a regularizer
as if it is a one-argument function.

E.g.

```
>>> regularizer = L2(2.)
>>> tensor = ops.ones(shape=(5, 5))
>>> regularizer(tensor)
50.0
```

## Developing new regularizers

Any function that takes in a weight matrix and returns a scalar
tensor can be used as a regularizer, e.g.:

```
>>> def l1_reg(weight_matrix):
...    return 0.01 * ops.sum(ops.absolute(weight_matrix))
... 
>>> layer = Dense(5, input_dim=5,
...     kernel_initializer='ones', kernel_regularizer=l1_reg)
>>> tensor = ops.ones(shape=(5, 5))
>>> out = layer(tensor)
>>> layer.losses
0.25
```

Alternatively, you can write your custom regularizers in an
object-oriented way by extending this regularizer base class, e.g.:

```
>>> class L2Regularizer(Regularizer):
...   def __init__(self, l2=0.):
...     self.l2 = l2
... 
...   def __call__(self, x):
...     return self.l2 * ops.sum(ops.square(x))
... 
...   def get_config(self):
...     return {'l2': float(self.l2)}
... 
>>> layer = Dense(
...   5, input_dim=5, kernel_initializer='ones',
...   kernel_regularizer=L2Regularizer(l2=0.5))
```

```
>>> tensor = ops.ones(shape=(5, 5))
>>> out = layer(tensor)
>>> layer.losses
12.5
```

### A note on serialization and deserialization:

Registering the regularizers as serializable is optional if you are just
training and executing models, exporting to and from SavedModels, or saving
and loading weight checkpoints.

Registration is required for saving and
loading models to HDF5 format, Keras model cloning, some visualization
utilities, and exporting models to and from JSON. If using this
functionality, you must make sure any python process running your model has
also defined and registered your custom regularizer.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L147-L165)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L123-L125)

```
__call__(
    x
)
```

Compute a regularization penalty from an input tensor.