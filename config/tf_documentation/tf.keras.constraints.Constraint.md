# tf.keras.constraints.Constraint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints/Constraint)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L6-L77) |

Base class for weight constraints.

A `Constraint` instance works like a stateless function.
Users who subclass this
class should override the `__call__()` method, which takes a single
weight parameter and return a projected version of that parameter
(e.g. normalized or clipped). Constraints can be used with various Keras
layers via the `kernel_constraint` or `bias_constraint` arguments.

Here's a simple example of a non-negative weight constraint:

```
>>> class NonNegative(keras.constraints.Constraint):
... 
...  def __call__(self, w):
...    return w * ops.cast(ops.greater_equal(w, 0.), dtype=w.dtype)
```

```
>>> weight = ops.convert_to_tensor((-1.0, 1.0))
>>> NonNegative()(weight)
[0.,  1.]
```

#### Usage in a layer:

```
>>> keras.layers.Dense(4, kernel_constraint=NonNegative())
```

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/constraints/constraints.py#L33-L46)

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