# tf.keras.losses.deserialize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/deserialize](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/deserialize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/__init__.py#L131-L148) |

Deserializes a serialized loss class/function instance.

```
tf.keras.losses.deserialize(
    name, custom_objects=None
)
```

| Args | |

|  |  |
| --- | --- |
| `name` | Loss configuration. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom objects (classes and functions) to be considered during deserialization. |

| Returns | |
| A Keras `Loss` instance or a loss function. | |