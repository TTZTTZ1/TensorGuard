# tf.keras.optimizers.deserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/deserialize](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/deserialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/__init__.py#L48-L69) |

Returns a Keras optimizer object via its configuration.

```
tf.keras.optimizers.deserialize(
    config, custom_objects=None
)
```

| Args | |

|  |  |
| --- | --- |
| `config` | Optimizer configuration dictionary. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom objects (classes and functions) to be considered during deserialization. |

| Returns | |
| A Keras Optimizer instance. | |