# tf.keras.optimizers.schedules.PiecewiseConstantDecay

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L187-L301) |

A `LearningRateSchedule` that uses a piecewise constant decay schedule.

Inherits From: [`LearningRateSchedule`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

```
tf.keras.optimizers.schedules.PiecewiseConstantDecay(
    boundaries, values, name='PiecewiseConstant'
)
```

The function returns a 1-arg callable to compute the piecewise constant
when passed the current optimizer step. This can be useful for changing the
learning rate value across different invocations of optimizer functions.

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5
for the next 10000 steps, and 0.1 for any additional steps.

```
step = ops.array(0)
boundaries = [100000, 110000]
values = [1.0, 0.5, 0.1]
learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(
    boundaries, values)

# Later, whenever we perform an optimization step, we pass in the step.
learning_rate = learning_rate_fn(step)
```

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Optimizer)
as the learning rate. The learning rate schedule is also serializable and
deserializable using [`keras.optimizers.schedules.serialize`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/serialize) and
[`keras.optimizers.schedules.deserialize`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/deserialize).

| Args | |

|  |  |
| --- | --- |
| `boundaries` | A list of Python numbers with strictly increasing entries, and with all elements having the same type as the optimizer step. |
| `values` | A list of Python numbers that specifies the values for the intervals defined by `boundaries`. It should have one more element than `boundaries`, and all elements should have the same type. |
| `name` | A string. Optional name of the operation. Defaults to `"PiecewiseConstant"`. |

| Returns | |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as the boundary tensors. | |

The output of the 1-arg function that takes the `step`
is `values[0]` when `step <= boundaries[0]`,
`values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`,
..., and `values[-1]` when `step > boundaries[-1]`.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the number of elements in the `boundaries` and `values` lists do not match. |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L66-L76)

```
@classmethod
from_config(
    config
)
```

Instantiates a `LearningRateSchedule` from its config.

| Args | |

|  |  |
| --- | --- |
| `config` | Output of `get_config()`. |

| Returns | |
| A `LearningRateSchedule` instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L296-L301)

```
get_config()
```

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L256-L294)

```
__call__(
    step
)
```

Call self as a function.