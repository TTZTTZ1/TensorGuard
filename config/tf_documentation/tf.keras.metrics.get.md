# tf.keras.metrics.get

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/get](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/get)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/__init__.py#L162-L206) |

Retrieves a Keras metric as a `function`/`Metric` class instance.

```
tf.keras.metrics.get(
    identifier
)
```

The `identifier` may be the string name of a metric function or class.

```
>>> metric = metrics.get("categorical_crossentropy")
>>> type(metric)
<class 'function'>
>>> metric = metrics.get("CategoricalCrossentropy")
>>> type(metric)
<class '...metrics.CategoricalCrossentropy'>
```

You can also specify `config` of the metric to this function by passing dict
containing `class_name` and `config` as an identifier. Also note that the
`class_name` must map to a `Metric` class

```
>>> identifier = {"class_name": "CategoricalCrossentropy",
...               "config": {"from_logits": True} }
>>> metric = metrics.get(identifier)
>>> type(metric)
<class '...metrics.CategoricalCrossentropy'>
```

| Args | |

|  |  |
| --- | --- |
| `identifier` | A metric identifier. One of None or string name of a metric function/class or metric configuration dictionary or a metric function or a metric class instance |

| Returns | |
| A Keras metric as a `function`/ `Metric` class instance. | |