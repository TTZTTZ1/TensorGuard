# tf.keras.losses.get

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/get](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/get)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/__init__.py#L151-L196) |

Retrieves a Keras loss as a `function`/`Loss` class instance.

```
tf.keras.losses.get(
    identifier
)
```

The `identifier` may be the string name of a loss function or `Loss` class.

```
>>> loss = losses.get("categorical_crossentropy")
>>> type(loss)
<class 'function'>
>>> loss = losses.get("CategoricalCrossentropy")
>>> type(loss)
<class '...CategoricalCrossentropy'>
```

You can also specify `config` of the loss to this function by passing dict
containing `class_name` and `config` as an identifier. Also note that the
`class_name` must map to a `Loss` class

```
>>> identifier = {"class_name": "CategoricalCrossentropy",
...               "config": {"from_logits": True} }
>>> loss = losses.get(identifier)
>>> type(loss)
<class '...CategoricalCrossentropy'>
```

| Args | |

|  |  |
| --- | --- |
| `identifier` | A loss identifier. One of None or string name of a loss function/class or loss configuration dictionary or a loss function or a loss class instance. |

| Returns | |
| A Keras loss as a `function`/ `Loss` class instance. | |