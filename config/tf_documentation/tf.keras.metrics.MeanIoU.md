# tf.keras.metrics.MeanIoU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanIoU](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanIoU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/iou_metrics.py#L422-L523) |

Computes the mean Intersection-Over-Union metric.

Inherits From: [`IoU`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/IoU), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.MeanIoU(
    num_classes,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_true=True,
    sparse_y_pred=True,
    axis=-1
)
```

#### Formula:

```
iou = true_positives / (true_positives + false_positives + false_negatives)
```

Intersection-Over-Union is a common evaluation metric for semantic image
segmentation.

To compute IoUs, the predictions are accumulated in a confusion matrix,
weighted by `sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

Note that this class first computes IoUs for all individual classes, then
returns the mean of these values.

| Args | |

|  |  |
| --- | --- |
| `num_classes` | The possible number of labels the prediction task can have. This value must be provided, since a confusion matrix of dimension = [num\_classes, num\_classes] will be allocated. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during metric computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered. |
| `sparse_y_true` | Whether labels are encoded using integers or dense floating point vectors. If `False`, the `argmax` function is used to determine each sample's most likely associated label. |
| `sparse_y_pred` | Whether predictions are encoded using integers or dense floating point vectors. If `False`, the `argmax` function is used to determine each sample's most likely associated label. |
| `axis` | (Optional) The dimension containing the logits. Defaults to `-1`. |

#### Example:

#### Example:

```
>>> # cm = [[1, 1],
>>> #        [1, 1]]
>>> # sum_row = [2, 2], sum_col = [2, 2], true_positives = [1, 1]
>>> # iou = true_positives / (sum_row + sum_col - true_positives))
>>> # result = (1 / (2 + 2 - 1) + 1 / (2 + 2 - 1)) / 2 = 0.33
>>> m = keras.metrics.MeanIoU(num_classes=2)
>>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1])
>>> m.result()
0.33333334
```

```
>>> m.reset_state()
>>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1],
...                sample_weight=[0.3, 0.3, 0.3, 0.1])
>>> m.result().numpy()
0.23809525
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.MeanIoU(num_classes=2)])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/iou_metrics.py#L514-L523)

```
get_config()
```

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/iou_metrics.py#L139-L142)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/iou_metrics.py#L250-L285)

```
result()
```

Compute the intersection-over-union via the confusion matrix.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/iou_metrics.py#L74-L137)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulates the confusion matrix statistics.

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Can be a `Tensor` whose rank is either 0, or the same as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |

| Returns | |
| Update op. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L217-L220)

```
__call__(
    *args, **kwargs
)
```

Call self as a function.