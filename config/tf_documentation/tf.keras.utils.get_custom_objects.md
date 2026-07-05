# tf.keras.utils.get_custom_objects

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_custom_objects](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_custom_objects)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L68-L91) |

Retrieves a live reference to the global dictionary of custom objects.

```
tf.keras.utils.get_custom_objects()
```

Custom objects set using `custom_object_scope()` are not added to the
global dictionary of custom objects, and will not appear in the returned
dictionary.

#### Example:

```
get_custom_objects().clear()
get_custom_objects()['MyObject'] = MyObject
```

| Returns | |
| Global dictionary mapping registered class names to classes. | |