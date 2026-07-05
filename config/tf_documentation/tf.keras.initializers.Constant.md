# tf.keras.initializers.Constant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Constant](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Constant)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L8-L45) |

Initializer that generates tensors with constant values.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.constant`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Constant)

```
tf.keras.initializers.Constant(
    value=0.0
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Classification on imbalanced data](https://tensorflow.google.cn/tutorials/structured_data/imbalanced_data) * [Train a Deep Q Network with TF-Agents](https://tensorflow.google.cn/agents/tutorials/1_dqn_tutorial) |

Only scalar values are allowed.
The constant value provided must be convertible to the dtype requested
when calling the initializer.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = Constant(10.)
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = Constant(10.)
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `value` | A Python scalar. |

## Methods

### `clone`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L83-L84)

```
clone()
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L42-L45)

```
@classmethod
from_config(
    config
)
```

Instantiates an initializer from a configuration dictionary.

#### Example:

```
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, the output of `get_config()`. |

| Returns | |
| An `Initializer` instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L39-L40)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L33-L37)

```
__call__(
    shape, dtype=None
)
```

Returns a tensor object initialized as specified by the initializer.

| Args | |

|  |  |
| --- | --- |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. |