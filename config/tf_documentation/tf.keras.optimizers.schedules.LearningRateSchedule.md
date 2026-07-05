# tf.keras.optimizers.schedules.LearningRateSchedule

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L10-L76) |

The learning rate schedule base class.

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Neural machine translation with a Transformer and Keras](https://tensorflow.google.cn/text/tutorials/transformer) |

You can use a learning rate schedule to modulate how the learning rate
of your optimizer changes over time.

Several built-in learning rate schedules are available, such as
[`keras.optimizers.schedules.ExponentialDecay`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay) or
[`keras.optimizers.schedules.PiecewiseConstantDecay`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay):

```
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=1e-2,
    decay_steps=10000,
    decay_rate=0.9)
optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)
```

A `LearningRateSchedule` instance can be passed in as the `learning_rate`
argument of any optimizer.

To implement your own schedule object, you should implement the `__call__`
method, which takes a `step` argument (scalar integer tensor, the
current training step count).
Like for any other Keras object, you can also optionally
make your object serializable by implementing the `get_config`
and `from_config` methods.

#### Example:

```
class MyLRSchedule(keras.optimizers.schedules.LearningRateSchedule):

    def __init__(self, initial_learning_rate):
        self.initial_learning_rate = initial_learning_rate

    def __call__(self, step):
        return self.initial_learning_rate / (step + 1)

optimizer = keras.optimizers.SGD(learning_rate=MyLRSchedule(0.1))
```

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L60-L64)

```
get_config()
```

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L54-L58)

```
__call__(
    step
)
```

Call self as a function.