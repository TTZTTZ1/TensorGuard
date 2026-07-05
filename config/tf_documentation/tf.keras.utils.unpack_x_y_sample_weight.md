# tf.keras.utils.unpack_x_y_sample_weight

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/unpack_x_y_sample_weight)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/data_adapter_utils.py#L10-L50) |

Unpacks user-provided data tuple.

```
tf.keras.utils.unpack_x_y_sample_weight(
    data
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Integrating MinDiff without MinDiffModel](https://tensorflow.google.cn/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_without_min_diff_model) * [Creating a custom Counterfactual Logit Pairing Dataset](https://tensorflow.google.cn/responsible_ai/model_remediation/counterfactual/guide/creating_a_custom_counterfactual_dataset) |

This is a convenience utility to be used when overriding
[`Model.train_step`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#train_step), [`Model.test_step`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#test_step), or [`Model.predict_step`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#predict_step).
This utility makes it easy to support data of the form `(x,)`,
`(x, y)`, or `(x, y, sample_weight)`.

#### Example:

```
>>> features_batch = ops.ones((10, 5))
>>> labels_batch = ops.zeros((10, 5))
>>> data = (features_batch, labels_batch)
>>> # `y` and `sample_weight` will default to `None` if not provided.
>>> x, y, sample_weight = unpack_x_y_sample_weight(data)
>>> sample_weight is None
True
```

| Args | |

|  |  |
| --- | --- |
| `data` | A tuple of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`. |

| Returns | |
| The unpacked tuple, with `None`s for `y` and `sample_weight` if they are not provided. | |