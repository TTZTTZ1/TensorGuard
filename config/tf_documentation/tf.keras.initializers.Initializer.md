# tf.keras.initializers.Initializer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Initializer](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/Initializer)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L4-L84) |

Initializer base class: all Keras initializers inherit from this class.

#### View aliases

**Main aliases**

[`tf.keras.initializers.Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

Initializers should implement a `__call__()` method with the following
signature:

```
def __call__(self, shape, dtype=None, **kwargs):
    # returns a tensor of shape `shape` and dtype `dtype`
    # containing values drawn from a distribution of your choice.
```

Optionally, you an also implement the method `get_config()` and the class
method `from_config` in order to support serialization -- just like with
any Keras object.

Here's a simple example: a random normal initializer.

```
class ExampleRandomNormal(Initializer):
    def __init__(self, mean, stddev):
        self.mean = mean
        self.stddev = stddev

    def __call__(self, shape, dtype=None, **kwargs):
        return keras.random.normal(
            shape, mean=self.mean, stddev=self.stddev, dtype=dtype
        )

    def get_config(self):  # To support serialization
        return {"mean": self.mean, "stddev": self.stddev}
```

Note that we don't have to implement `from_config()` in the example above
since the constructor arguments of the class the keys in the config returned
by `get_config()` are the same. In this case, the default `from_config()`
works fine.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/initializer.py#L44-L53)

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