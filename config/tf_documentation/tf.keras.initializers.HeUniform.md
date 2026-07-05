# tf.keras.initializers.HeUniform

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/HeUniform](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/HeUniform)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L556-L597) |

He uniform variance scaling initializer.

Inherits From: [`VarianceScaling`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/VarianceScaling), [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.he_uniform`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/HeUniform)

```
tf.keras.initializers.HeUniform(
    seed=None
)
```

Draws samples from a uniform distribution within `[-limit, limit]`, where
`limit = sqrt(6 / fan_in)` (`fan_in` is the number of input units in the
weight tensor).

#### Examples:

```
>>> # Standalone usage:
>>> initializer = HeUniform()
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = HeUniform()
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |

#### Reference:

* [He et al., 2015](https://arxiv.org/abs/1502.01852)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L594-L597)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L273-L296)

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