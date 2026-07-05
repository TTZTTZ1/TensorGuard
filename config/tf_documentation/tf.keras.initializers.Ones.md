# tf.keras.initializers.Ones

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Ones](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Ones)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L77-L105) |

Initializer that generates tensors initialized to 1.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.ones`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Ones)

Also available via the shortcut function `ones`.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = Ones()
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = Ones()
>>> layer = Dense(3, kernel_initializer=initializer)
```

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/constant_initializers.py#L94-L105)

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