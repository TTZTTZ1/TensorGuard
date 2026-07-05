# tf.keras.utils.get_registered_name

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_registered_name](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_registered_name)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L159-L182) |

Returns the name registered to an object within the Keras framework.

```
tf.keras.utils.get_registered_name(
    obj
)
```

This function is part of the Keras serialization and deserialization
framework. It maps objects to the string names associated with those objects
for serialization/deserialization.

| Args | |

|  |  |
| --- | --- |
| `obj` | The object to look up. |

| Returns | |
| The name associated with the object, or the default Python name if the object is not registered. | |