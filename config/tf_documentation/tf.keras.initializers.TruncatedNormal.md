# tf.keras.initializers.TruncatedNormal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/TruncatedNormal](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/TruncatedNormal)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L67-L124) |

Initializer that generates a truncated normal distribution.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.truncated_normal`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/TruncatedNormal)

```
tf.keras.initializers.TruncatedNormal(
    mean=0.0, stddev=0.05, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Customizing a Transformer Encoder](https://tensorflow.google.cn/tfmodels/nlp/customize_encoder) * [Fine-tuning a BERT model](https://tensorflow.google.cn/tfmodels/nlp/fine_tune_bert) |

The values generated are similar to values from a
`RandomNormal` initializer, except that values more
than two standard deviations from the mean are
discarded and re-drawn.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = TruncatedNormal(mean=0., stddev=1.)
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = TruncatedNormal(mean=0., stddev=1.)
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `mean` | A python scalar or a scalar keras tensor. Mean of the random values to generate. |
| `stddev` | A python scalar or a scalar keras tensor. Standard deviation of the random values to generate. |
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L122-L124)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L113-L120)

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