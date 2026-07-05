# tf.keras.utils.pack_x_y_sample_weight

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/pack_x_y_sample_weight](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/pack_x_y_sample_weight)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/data_adapter_utils.py#L53-L92) |

Packs user-provided data into a tuple.

```
tf.keras.utils.pack_x_y_sample_weight(
    x, y=None, sample_weight=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Creating a custom Counterfactual Logit Pairing Dataset](https://tensorflow.google.cn/responsible_ai/model_remediation/counterfactual/guide/creating_a_custom_counterfactual_dataset) |

This is a convenience utility for packing data into the tuple formats
that [`Model.fit()`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#fit) uses.

#### Example:

```
>>> x = ops.ones((10, 1))
>>> data = pack_x_y_sample_weight(x)
>>> isinstance(data, ops.Tensor)
True
>>> y = ops.ones((10, 1))
>>> data = pack_x_y_sample_weight(x, y)
>>> isinstance(data, tuple)
True
>>> x, y = data
```

| Args | |

|  |  |
| --- | --- |
| `x` | Features to pass to `Model`. |
| `y` | Ground-truth targets to pass to `Model`. |
| `sample_weight` | Sample weight for each element. |

| Returns | |
| Tuple in the format used in [`Model.fit()`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#fit). | |