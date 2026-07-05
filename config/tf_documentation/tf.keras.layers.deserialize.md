# tf.keras.layers.deserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/deserialize](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/deserialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/__init__.py#L153-L175) |

Returns a Keras layer object via its configuration.

```
tf.keras.layers.deserialize(
    config, custom_objects=None
)
```

| Args | |

|  |  |
| --- | --- |
| `config` | A python dict containing a serialized layer configuration. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom objects (classes and functions) to be considered during deserialization. |

| Returns | |
| A Keras layer instance. | |