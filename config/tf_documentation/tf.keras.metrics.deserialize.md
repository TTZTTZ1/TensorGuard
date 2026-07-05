# tf.keras.metrics.deserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/deserialize](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/deserialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/__init__.py#L142-L159) |

Deserializes a serialized metric class/function instance.

```
tf.keras.metrics.deserialize(
    config, custom_objects=None
)
```

| Args | |

|  |  |
| --- | --- |
| `config` | Metric configuration. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom objects (classes and functions) to be considered during deserialization. |

| Returns | |
| A Keras `Metric` instance or a metric function. | |