# tf.keras.metrics.TruePositives

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/TruePositives](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/TruePositives)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L210-L251) |

Calculates the number of true positives.

Inherits From: [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.TruePositives(
    thresholds=None, name=None, dtype=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Classification on imbalanced data](https://tensorflow.google.cn/tutorials/structured_data/imbalanced_data) |

If `sample_weight` is given, calculates the sum of the weights of
true positives. This metric creates one local variable, `true_positives`
that is used to keep track of the number of true positives.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

| Args | |

|  |  |
| --- | --- |
| `thresholds` | (Optional) Defaults to `0.5`. A float value, or a Python list/tuple of float threshold values in `[0, 1]`. A threshold is compared with prediction values to determine the truth value of predictions (i.e., above the threshold is `True`, below is `False`). If used with a loss function that sets `from_logits=True` (i.e. no sigmoid applied to predictions), `thresholds` should be set to 0. One metric value is generated for each threshold value. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
>>> m = keras.metrics.TruePositives()
>>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
>>> m.result()
2.0
```

```
>>> m.reset_state()
>>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1], sample_weight=[0, 0, 1, 0])
>>> m.result()
1.0
```

| Attributes | |

|  |  |
| --- | --- |
| `dtype` |  |

|  |  |
| --- | --- |
| `variables` |  |

## Methods

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L186-L202)

```
add_variable(
    shape, initializer, dtype=None, aggregation='sum', name=None
)
```

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L204-L208)

```
add_weight(
    shape=(), initializer=None, dtype=None, name=None
)
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L226-L228)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L72-L75)

```
get_config()
```

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L102-L109)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L65-L70)

```
result()
```

Compute the current metric value.

| Returns | |
| A scalar tensor, or a dictionary of scalar tensors. | |

### `stateless_reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L164-L177)

```
stateless_reset_state()
```

### `stateless_result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L148-L162)

```
stateless_result(
    metric_variables
)
```

### `stateless_update_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L115-L138)

```
stateless_update_state(
    metric_variables, *args, **kwargs
)
```

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L46-L63)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulates the metric statistics.

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Defaults to `1`. Can be a tensor whose rank is either 0, or the same rank as `y_true`, and must be broadcastable to `y_true`. |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L217-L220)

```
__call__(
    *args, **kwargs
)
```

Call self as a function.