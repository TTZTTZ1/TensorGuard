# tf.keras.initializers.Identity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Identity](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Identity)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L108-L153) |

Initializer that generates the identity matrix.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.IdentityInitializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Identity), [`tf.keras.initializers.identity`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Identity)

```
tf.keras.initializers.Identity(
    gain=1.0
)
```

Only usable for generating 2D matrices.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = Identity()
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = Identity()
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `gain` | Multiplicative factor to apply to the identity matrix. |

## Methods

### `clone`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L83-L84)

```
clone()
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L63-L81)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L55-L61)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L137-L153)

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
| `dtype` | Optional dtype of the tensor. Only numeric or boolean dtypes are supported. If not specified, [`keras.backend.floatx()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/floatx) is used, which default to `float32` unless you configured it otherwise (via [`keras.backend.set_floatx(float_dtype)`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_floatx)). |