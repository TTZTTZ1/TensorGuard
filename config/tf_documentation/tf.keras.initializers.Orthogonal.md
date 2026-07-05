# tf.keras.initializers.Orthogonal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Orthogonal](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Orthogonal)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L628-L703) |

Initializer that generates an orthogonal matrix.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.OrthogonalInitializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Orthogonal), [`tf.keras.initializers.orthogonal`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Orthogonal)

```
tf.keras.initializers.Orthogonal(
    gain=1.0, seed=None
)
```

If the shape of the tensor to initialize is two-dimensional, it is
initialized with an orthogonal matrix obtained from the QR decomposition of
a matrix of random numbers drawn from a normal distribution. If the matrix
has fewer rows than columns then the output will have orthogonal rows.
Otherwise, the output will have orthogonal columns.

If the shape of the tensor to initialize is more than two-dimensional,
a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])`
is initialized, where `n` is the length of the shape vector.
The matrix is subsequently reshaped to give a tensor of the desired shape.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = keras.initializers.Orthogonal()
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = keras.initializers.Orthogonal()
>>> layer = keras.layers.Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `gain` | Multiplicative factor to apply to the orthogonal matrix. |
| `seed` | A Python integer. Used to make the behavior of the initializer deterministic. |

#### Reference:

* [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L701-L703)

```
get_config()
```

Returns the initializer's configuration as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L674-L699)

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