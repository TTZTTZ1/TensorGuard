# tf.keras.constraints.MinMaxNorm

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/MinMaxNorm](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/MinMaxNorm)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L160-L213) |

MinMaxNorm weight constraint.

Inherits From: [`Constraint`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint)

#### View aliases

**Main aliases**

[`tf.keras.constraints.min_max_norm`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/MinMaxNorm)

```
tf.keras.constraints.MinMaxNorm(
    min_value=0.0, max_value=1.0, rate=1.0, axis=0
)
```

Constrains the weights incident to each hidden unit
to have the norm between a lower bound and an upper bound.

| Args | |

|  |  |
| --- | --- |
| `min_value` | the minimum norm for the incoming weights. |
| `max_value` | the maximum norm for the incoming weights. |
| `rate` | rate for enforcing the constraint: weights will be rescaled to yield `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`. Effectively, this means that rate=1.0 stands for strict enforcement of the constraint, while rate<1.0 means that weights will be rescaled at each step to slowly move towards a value inside the desired interval. |
| `axis` | integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`. |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L59-L77)

```
@classmethod
from_config(
    config
)
```

Instantiates a weight constraint from a configuration dictionary.

#### Example:

```
constraint = UnitNorm()
config = constraint.get_config()
constraint = UnitNorm.from_config(config)
```

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, the output of `get_config()`. |

| Returns | |
| A [`keras.constraints.Constraint`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint) instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L207-L213)

```
get_config()
```

Returns a Python dict of the object config.

A constraint config is a Python dictionary (JSON-serializable) that can
be used to reinstantiate the same object.

| Returns | |
| Python dict containing the configuration of the constraint object. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L198-L205)

```
__call__(
    w
)
```

Applies the constraint to the input weight variable.

By default, the inputs weight variable is not modified.
Users should override this method to implement their own projection
function.

| Args | |

|  |  |
| --- | --- |
| `w` | Input weight variable. |

| Returns | |
| Projected variable (by default, returns unmodified inputs). | |