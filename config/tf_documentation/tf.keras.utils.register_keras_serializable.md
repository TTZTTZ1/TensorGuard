# tf.keras.utils.register_keras_serializable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/register_keras_serializable](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/register_keras_serializable)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/object_registration.py#L94-L156) |

Registers an object with the Keras serialization framework.

```
tf.keras.utils.register_keras_serializable(
    package='Custom', name=None
)
```

This decorator injects the decorated class or function into the Keras custom
object dictionary, so that it can be serialized and deserialized without
needing an entry in the user-provided custom object dict. It also injects a
function that Keras will call to get the object's serializable string key.

Note that to be serialized and deserialized, classes must implement the
`get_config()` method. Functions do not have this requirement.

The object will be registered under the key `'package>name'` where `name`,
defaults to the object name if not passed.

#### Example:

```
# Note that `'my_package'` is used as the `package` argument here, and since
# the `name` argument is not provided, `'MyDense'` is used as the `name`.
@register_keras_serializable('my_package')
class MyDense(keras.layers.Dense):
    pass

assert get_registered_object('my_package>MyDense') == MyDense
assert get_registered_name(MyDense) == 'my_package>MyDense'
```

| Args | |

|  |  |
| --- | --- |
| `package` | The package that this class belongs to. This is used for the `key` (which is `"package>name"`) to idenfify the class. Note that this is the first argument passed into the decorator. |
| `name` | The name to serialize this class under in this package. If not provided or `None`, the class' name will be used (note that this is the case when the decorator is used with only one argument, which becomes the `package`). |

| Returns | |
| A decorator that registers the decorated class with the passed names. | |