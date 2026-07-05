# tf.keras.initializers.VarianceScaling

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/VarianceScaling](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/VarianceScaling)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L188-L305) |

Initializer that adapts its scale to the shape of its input tensors.

Inherits From: [`Initializer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.variance_scaling`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/VarianceScaling)

```
tf.keras.initializers.VarianceScaling(
    scale=1.0,
    mode='fan_in',
    distribution='truncated_normal',
    seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Train a Deep Q Network with TF-Agents](https://tensorflow.google.cn/agents/tutorials/1_dqn_tutorial) * [Networks](https://tensorflow.google.cn/agents/tutorials/8_networks_tutorial) |

With `distribution="truncated_normal" or "untruncated_normal"`, samples are
drawn from a truncated/untruncated normal distribution with a mean of zero
and a standard deviation (after truncation, if used) `stddev = sqrt(scale /
n)`, where `n` is:

* number of input units in the weight tensor, if `mode="fan_in"`
* number of output units, if `mode="fan_out"`
* average of the numbers of input and output units, if `mode="fan_avg"`

With `distribution="uniform"`, samples are drawn from a uniform distribution
within `[-limit, limit]`, where `limit = sqrt(3 * scale / n)`.

#### Examples:

```
>>> # Standalone usage:
>>> initializer = VarianceScaling(
    scale=0.1, mode='fan_in', distribution='uniform')
>>> values = initializer(shape=(2, 2))
```

```
>>> # Usage in a Keras layer:
>>> initializer = VarianceScaling(
    scale=0.1, mode='fan_in', distribution='uniform')
>>> layer = Dense(3, kernel_initializer=initializer)
```

| Args | |

|  |  |
| --- | --- |
| `scale` | Scaling factor (positive float). |
| `mode` | One of `"fan_in"`, `"fan_out"`, `"fan_avg"`. |
| `distribution` | Random distribution to use. One of `"truncated_normal"`, `"untruncated_normal"`, or `"uniform"`. |
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/random_initializers.py#L298-L305)

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