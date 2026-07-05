# tf.keras.utils.get_registered_object

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_registered_object](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_registered_object)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L185-L230) |

Returns the class associated with `name` if it is registered with Keras.

```
tf.keras.utils.get_registered_object(
    name, custom_objects=None, module_objects=None
)
```

This function is part of the Keras serialization and deserialization
framework. It maps strings to the objects associated with them for
serialization/deserialization.

#### Example:

```
def from_config(cls, config, custom_objects=None):
    if 'my_custom_object_name' in config:
        config['hidden_cls'] = tf.keras.saving.get_registered_object(
            config['my_custom_object_name'], custom_objects=custom_objects)
```

| Args | |

|  |  |
| --- | --- |
| `name` | The name to look up. |
| `custom_objects` | A dictionary of custom objects to look the name up in. Generally, custom\_objects is provided by the user. |
| `module_objects` | A dictionary of custom objects to look the name up in. Generally, module\_objects is provided by midlevel library implementers. |

| Returns | |
| An instantiable class associated with `name`, or `None` if no such class exists. | |