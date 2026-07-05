# tf.keras.constraints.NonNeg

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/NonNeg](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/NonNeg)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L119-L125) |

Constrains the weights to be non-negative.

Inherits From: [`Constraint`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint)

#### View aliases

**Main aliases**

[`tf.keras.constraints.non_neg`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/NonNeg)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L48-L57)

```
get_config()
```

Returns a Python dict of the object config.

A constraint config is a Python dictionary (JSON-serializable) that can
be used to reinstantiate the same object.

| Returns | |
| Python dict containing the configuration of the constraint object. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L123-L125)

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