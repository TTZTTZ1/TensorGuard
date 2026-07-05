# tf.keras.backend.floatx

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/floatx](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/floatx)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/config.py#L19-L34) |

Return the default float type, as a string.

#### View aliases

**Main aliases**

[`tf.keras.config.floatx`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/floatx)

```
tf.keras.backend.floatx()
```

E.g. `'bfloat16'`, `'float16'`, `'float32'`, `'float64'`.

| Returns | |
| String, the current default float type. | |

#### Example:

```
>>> keras.config.floatx()
'float32'
```