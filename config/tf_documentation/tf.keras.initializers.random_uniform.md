# tf.keras.initializers.random_uniform

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/random_uniform](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/random_uniform)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L127-L185) |

Random uniform initializer.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.random_uniform`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/RandomUniform)

```
tf.keras.initializers.RandomUniform(
    minval=-0.05, maxval=0.05, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Train a Deep Q Network with TF-Agents](https://tensorflow.google.cn/agents/tutorials/1_dqn_tutorial) * [Networks](https://tensorflow.google.cn/agents/tutorials/8_networks_tutorial) |

Draws samples from a uniform distribution for given parameters.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = RandomUniform(minval=0.0, maxval=1.0)
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = RandomUniform(minval=0.0, maxval=1.0)
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `minval` | A python scalar or a scalar keras tensor. Lower bound of the range of random values to generate (inclusive). |
| `maxval` | A python scalar or a scalar keras tensor. Upper bound of the range of random values to generate (exclusive). |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L179-L185)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L170-L177)

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