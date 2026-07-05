# tf.keras.backend.get_uid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/get_uid](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/get_uid)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/naming.py#L34-L57) |

Associates a string prefix with an integer counter.

```
tf.keras.backend.get_uid(
    prefix=''
)
```

| Args | |

|  |  |
| --- | --- |
| `prefix` | String prefix to index. |

| Returns | |
| Unique integer ID. | |

#### Example:

```
>>> get_uid('dense')
1
>>> get_uid('dense')
2
```