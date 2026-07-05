# tf.keras.models.model_from_json

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/models/model_from_json](https://tensorflow.google.cn/api_docs/python/tf/keras/models/model_from_json)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L551-L577) |

Parses a JSON model configuration string and returns a model instance.

```
tf.keras.models.model_from_json(
    json_string, custom_objects=None
)
```

#### Example:

```
>>> model = keras.Sequential([
...     keras.layers.Dense(5, input_shape=(3,)),
...     keras.layers.Softmax()])
>>> config = model.to_json()
>>> loaded_model = keras.models.model_from_json(config)
```

| Args | |

|  |  |
| --- | --- |
| `json_string` | JSON string encoding a model configuration. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom classes or functions to be considered during deserialization. |

| Returns | |
| A Keras model instance (uncompiled). | |