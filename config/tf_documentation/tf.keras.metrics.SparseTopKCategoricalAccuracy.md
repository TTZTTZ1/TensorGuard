# tf.keras.metrics.SparseTopKCategoricalAccuracy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseTopKCategoricalAccuracy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseTopKCategoricalAccuracy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L423-L469) |

Computes how often integer targets are in the top `K` predictions.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.SparseTopKCategoricalAccuracy(
    k=5, name='sparse_top_k_categorical_accuracy', dtype=None
)
```

| Args | |

|  |  |
| --- | --- |
| `k` | (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
>>> m = keras.metrics.SparseTopKCategoricalAccuracy(k=1)
>>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=[keras.metrics.SparseTopKCategoricalAccuracy()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L468-L469)

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