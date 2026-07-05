# tf.keras.utils.CustomObjectScope

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/CustomObjectScope](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/CustomObjectScope)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L10-L61) |

Exposes custom classes/functions to Keras deserialization internals.

#### View aliases

**Main aliases**

[`tf.keras.utils.custom_object_scope`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/CustomObjectScope)

```
tf.keras.utils.CustomObjectScope(
    custom_objects
)
```

Under a scope `with custom_object_scope(objects_dict)`, Keras methods such
as [`keras.models.load_model()`](https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model) or
`keras.models.model_from_config()` will be able to deserialize any
custom object referenced by a saved config (e.g. a custom layer or metric).

#### Example:

Consider a custom regularizer `my_regularizer`:

```
layer = Dense(3, kernel_regularizer=my_regularizer)
# Config contains a reference to `my_regularizer`
config = layer.get_config()
...
# Later:
with custom_object_scope({'my_regularizer': my_regularizer}):
    layer = Dense.from_config(config)
```

| Args | |

|  |  |
| --- | --- |
| `custom_objects` | Dictionary of `{str: object}` pairs, where the `str` key is the object name. |

## Methods

### `__enter__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L49-L56)

```
__enter__()
```

### `__exit__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L58-L61)

```
__exit__(
    *args, **kwargs
)
```