# tf.keras.initializers.LecunUniform

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/LecunUniform](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/LecunUniform)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L463-L509) |

Lecun uniform initializer.

Inherits From: [`VarianceScaling`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/VarianceScaling), [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.lecun_uniform`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/LecunUniform)

```
tf.keras.initializers.LecunUniform(
    seed=None
)
```

Draws samples from a uniform distribution within `[-limit, limit]`, where
`limit = sqrt(3 / fan_in)` (`fan_in` is the number of input units in the
weight tensor).

#### Examples:

```
>>> # Standalone usage:
>>> initializer = LecunUniform()
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = LecunUniform()
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |

#### Reference:

* [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L506-L509)

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