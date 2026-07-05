# tf.keras.initializers.get

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/get](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers/get)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/initializers/__init__.py#L74-L120) |

Retrieves a Keras initializer object via an identifier.

```
tf.keras.initializers.get(
    identifier
)
```

The `identifier` may be the string name of a initializers function or class
(case-sensitively).

```
>>> identifier = 'Ones'
>>> keras.initializers.deserialize(identifier)
<...keras.initializers.initializers.Ones...>
```

You can also specify `config` of the initializer to this function by passing
dict containing `class_name` and `config` as an identifier. Also note that
the `class_name` must map to a `Initializer` class.

```
>>> cfg = {'class_name': 'Ones', 'config': {} }
>>> keras.initializers.deserialize(cfg)
<...keras.initializers.initializers.Ones...>
```

In the case that the `identifier` is a class, this method will return a new
instance of the class by its constructor.

| Args | |

|  |  |
| --- | --- |
| `identifier` | String or dict that contains the initializer name or configurations. |

| Returns | |
| Initializer instance base on the input identifier. | |