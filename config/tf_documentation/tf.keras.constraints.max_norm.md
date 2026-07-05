# tf.keras.constraints.max_norm

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/max_norm](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/max_norm)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L80-L116) |

MaxNorm weight constraint.

Inherits From: [`Constraint`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint)

#### View aliases

**Main aliases**

[`tf.keras.constraints.max_norm`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/MaxNorm)

```
tf.keras.constraints.MaxNorm(
    max_value=2, axis=0
)
```

Constrains the weights incident to each hidden unit
to have a norm less than or equal to a desired value.

Also available via the shortcut function [`keras.constraints.max_norm`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/MaxNorm).

| Args | |

|  |  |
| --- | --- |
| `max_value` | the maximum norm value for the incoming weights. |
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L115-L116)

```
get_config()
```

Returns a Python dict of the object config.

A constraint config is a Python dictionary (JSON-serializable) that can
be used to reinstantiate the same object.

| Returns | |
| Python dict containing the configuration of the constraint object. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L109-L113)

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