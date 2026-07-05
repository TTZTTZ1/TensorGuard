# tf.keras.optimizers.schedules.serialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/serialize](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/serialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/schedules/learning_rate_schedule.py#L912-L931) |

Serializes a `LearningRateSchedule` into a JSON-compatible dict.

```
tf.keras.optimizers.schedules.serialize(
    learning_rate_schedule
)
```

| Args | |

|  |  |
| --- | --- |
| `learning_rate_schedule` | The `LearningRateSchedule` object to serialize. |

| Returns | |
| A JSON-serializable dict representing the object's config. | |

#### Example:

```
>>> lr_schedule = keras.optimizers.schedules.ExponentialDecay(
...     0.1, decay_steps=100000, decay_rate=0.96, staircase=True)
>>> keras.optimizers.schedules.serialize(lr_schedule)
{'module': 'keras.optimizers.schedules',
'class_name': 'ExponentialDecay', 'config': {...},
'registered_name': None}
```