# tf.keras.metrics.CategoricalCrossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/CategoricalCrossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/CategoricalCrossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/probabilistic_metrics.py#L175-L261) |

Computes the crossentropy metric between the labels and predictions.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.CategoricalCrossentropy(
    name='categorical_crossentropy',
    dtype=None,
    from_logits=False,
    label_smoothing=0,
    axis=-1
)
```

This is the crossentropy metric class to be used when there are multiple
label classes (2 or more). It assumes that labels are one-hot encoded,
e.g., when labels values are `[2, 0, 1]`, then
`y_true` is `[[0, 0, 1], [1, 0, 0], [0, 1, 0]]`.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `from_logits` | (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution. |
| `label_smoothing` | (Optional) Float in `[0, 1]`. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of 0.1 for label "0" and 0.9 for label "1". |
| `axis` | (Optional) Defaults to `-1`. The dimension along which entropy is computed. |

#### Example:

#### Example:

```
>>> # EPSILON = 1e-7, y = y_true, y` = y_pred
>>> # y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON)
>>> # y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
>>> # xent = -sum(y * log(y'), axis = -1)
>>> #      = -((log 0.95), (log 0.1))
>>> #      = [0.051, 2.302]
>>> # Reduced xent = (0.051 + 2.302) / 2
>>> m = keras.metrics.CategoricalCrossentropy()
>>> m.update_state([[0, 1, 0], [0, 0, 1]],
...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
>>> m.result()
1.1769392
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1, 0], [0, 0, 1]],
...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]],
...                sample_weight=np.array([0.3, 0.7]))
>>> m.result()
1.6271976
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.CategoricalCrossentropy()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L215-L219)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/probabilistic_metrics.py#L254-L261)

```
get_config()
```

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L150-L152)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L154-L157)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L200-L207)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulate statistics for the metric.

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L217-L220)

```
__call__(
    *args, **kwargs
)
```

Call self as a function.