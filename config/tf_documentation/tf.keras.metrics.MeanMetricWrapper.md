# tf.keras.metrics.MeanMetricWrapper

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L160-L219) |

Wrap a stateless metric function with the `Mean` metric.

Inherits From: [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.MeanMetricWrapper(
    fn, name=None, dtype=None, **kwargs
)
```

You could use this class to quickly build a mean metric from a function. The
function needs to have the signature `fn(y_true, y_pred)` and return a
per-sample loss array. [`MeanMetricWrapper.result()`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean#result) will return
the average metric value across all samples seen so far.

#### For example:

```
def mse(y_true, y_pred):
    return (y_true - y_pred) ** 2

mse_metric = MeanMetricWrapper(fn=mse)
```

| Args | |

|  |  |
| --- | --- |
| `fn` | The metric function to wrap, with signature `fn(y_true, y_pred, **kwargs)`. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `**kwargs` | Keyword arguments to pass on to `fn`. |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L209-L213)

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