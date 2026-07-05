# tf.keras.utils.serialize_keras_object

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/serialize_keras_object](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/serialize_keras_object)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/serialization_lib.py#L117-L279) |

Retrieve the config dict by serializing the Keras object.

```
tf.keras.utils.serialize_keras_object(
    obj
)
```

`serialize_keras_object()` serializes a Keras object to a python dictionary
that represents the object, and is a reciprocal function of
`deserialize_keras_object()`. See `deserialize_keras_object()` for more
information about the config format.

| Args | |

|  |  |
| --- | --- |
| `obj` | the Keras object to serialize. |

| Returns | |
| A python dict that represents the object. The python dict can be deserialized via `deserialize_keras_object()`. | |