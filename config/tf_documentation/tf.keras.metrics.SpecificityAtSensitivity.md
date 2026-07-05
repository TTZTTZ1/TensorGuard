# tf.keras.metrics.SpecificityAtSensitivity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SpecificityAtSensitivity](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SpecificityAtSensitivity)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L781-L882) |

Computes best specificity where sensitivity is >= specified value.

Inherits From: [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.SpecificityAtSensitivity(
    sensitivity, num_thresholds=200, class_id=None, name=None, dtype=None
)
```

`Sensitivity` measures the proportion of actual positives that are correctly
identified as such `(tp / (tp + fn))`.
`Specificity` measures the proportion of actual negatives that are correctly
identified as such `(tn / (tn + fp))`.

This metric creates four local variables, `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` that are used to
compute the specificity at the given sensitivity. The threshold for the
given sensitivity value is computed and used to evaluate the corresponding
specificity.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

If `class_id` is specified, we calculate precision by considering only the
entries in the batch for which `class_id` is above the threshold
predictions, and computing the fraction of them for which `class_id` is
indeed a correct label.

For additional information about specificity and sensitivity, see
[the following](https://en.wikipedia.org/wiki/Sensitivity_and_specificity).

| Args | |

|  |  |
| --- | --- |
| `sensitivity` | A scalar value in range `[0, 1]`. |
| `num_thresholds` | (Optional) Defaults to 200. The number of thresholds to use for matching the given sensitivity. |
| `class_id` | (Optional) Integer class ID for which we want binary metrics. This must be in the half-open interval `[0, num_classes)`, where `num_classes` is the last dimension of predictions. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
>>> m = keras.metrics.SpecificityAtSensitivity(0.5)
>>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8])
>>> m.result()
0.66666667
```

```
>>> m.reset_state()
>>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8],
...                sample_weight=[1, 1, 2, 2, 2])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='binary_crossentropy',
    metrics=[keras.metrics.SpecificityAtSensitivity()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L876-L882)

```
get_config()
```

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L638-L643)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L863-L874)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L613-L636)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulates confusion matrix statistics.

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