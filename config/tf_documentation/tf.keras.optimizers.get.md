# tf.keras.optimizers.get

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/get](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/get)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/__init__.py#L72-L97) |

Retrieves a Keras Optimizer instance.

```
tf.keras.optimizers.get(
    identifier
)
```

| Args | |

|  |  |
| --- | --- |
| `identifier` | Optimizer identifier, one of: |

* String: name of an optimizer
* Dictionary: configuration dictionary.
* Keras Optimizer instance (it will be returned unchanged).

| Returns | |
| A Keras Optimizer instance. | |