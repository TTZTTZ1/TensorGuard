# tf.keras.optimizers.schedules.deserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/deserialize](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/deserialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L934-L969) |

Instantiates a `LearningRateSchedule` object from a serialized form.

```
tf.keras.optimizers.schedules.deserialize(
    config, custom_objects=None
)
```

| Args | |

|  |  |
| --- | --- |
| `config` | The serialized form of the `LearningRateSchedule`. Dictionary of the form {'class\_name': str, 'config': dict}. |
| `custom_objects` | A dictionary mapping class names (or function names) of custom (non-Keras) objects to class/functions. |

| Returns | |
| A `LearningRateSchedule` object. | |

#### Example:

```
# Configuration for PolynomialDecay
config = {
    'class_name': 'PolynomialDecay',
    'config': {'cycle': False,
        'decay_steps': 10000,
        'end_learning_rate': 0.01,
        'initial_learning_rate': 0.1,
        'name': None,
        'power': 0.5
    }
}
lr_schedule = keras.optimizers.schedules.deserialize(config)
```