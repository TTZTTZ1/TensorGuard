# tf.keras.optimizers.schedules.ExponentialDecay

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L79-L184) |

A `LearningRateSchedule` that uses an exponential decay schedule.

Inherits From: [`LearningRateSchedule`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

```
tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps,
    decay_rate,
    staircase=False,
    name='ExponentialDecay'
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) * [Migration examples: Canned Estimators](https://tensorflow.google.cn/guide/migrate/canned_estimators) |

When training a model, it is often useful to lower the learning rate as
the training progresses. This schedule applies an exponential decay function
to an optimizer step, given a provided initial learning rate.

The schedule is a 1-arg callable that produces a decayed learning
rate when passed the current optimizer step. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
It is computed as:

```
def decayed_learning_rate(step):
    return initial_learning_rate * decay_rate ^ (step / decay_steps)
```

If the argument `staircase` is `True`, then `step / decay_steps` is
an integer division and the decayed learning rate follows a
staircase function.

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Optimizer)
as the learning rate.
Example: When fitting a Keras model, decay every 100000 steps with a base
of 0.96:

```
initial_learning_rate = 0.1
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=100000,
    decay_rate=0.96,
    staircase=True)

model.compile(optimizer=keras.optimizers.SGD(learning_rate=lr_schedule),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=5)
```

The learning rate schedule is also serializable and deserializable using
[`keras.optimizers.schedules.serialize`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/serialize) and
[`keras.optimizers.schedules.deserialize`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/deserialize).

| Args | |

|  |  |
| --- | --- |
| `initial_learning_rate` | A Python float. The initial learning rate. |
| `decay_steps` | A Python integer. Must be positive. See the decay computation above. |
| `decay_rate` | A Python float. The decay rate. |
| `staircase` | Boolean. If `True` decay the learning rate at discrete intervals. |
| `name` | String. Optional name of the operation. Defaults to `"ExponentialDecay`". |

| Returns | |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`. | |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L177-L184)

```
get_config()
```

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L162-L175)

```
__call__(
    step
)
```

Call self as a function.