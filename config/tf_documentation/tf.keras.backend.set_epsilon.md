# tf.keras.backend.set_epsilon

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_epsilon](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_epsilon)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/config.py#L90-L110) |

Set the value of the fuzz factor used in numeric expressions.

#### View aliases

**Main aliases**

[`tf.keras.config.set_epsilon`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_epsilon)

```
tf.keras.backend.set_epsilon(
    value
)
```

| Args | |

|  |  |
| --- | --- |
| `value` | float. New value of epsilon. |

#### Examples:

```
>>> keras.config.epsilon()
1e-07
```

```
>>> keras.config.set_epsilon(1e-5)
>>> keras.config.epsilon()
1e-05
```

```
>>> # Set it back to the default value.
>>> keras.config.set_epsilon(1e-7)
```