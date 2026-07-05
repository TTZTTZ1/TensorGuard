# tf.keras.metrics.RootMeanSquaredError

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/RootMeanSquaredError](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/RootMeanSquaredError)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/regression_metrics.py#L186-L251) |

Computes root mean squared error metric between `y_true` and `y_pred`.

Inherits From: [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.RootMeanSquaredError(
    name='root_mean_squared_error', dtype=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Recommending movies: ranking](https://tensorflow.google.cn/recommenders/examples/basic_ranking) * [Deep & Cross Network (DCN)](https://tensorflow.google.cn/recommenders/examples/dcn) * [Listwise ranking](https://tensorflow.google.cn/recommenders/examples/listwise_ranking) * [Multi-task recommenders](https://tensorflow.google.cn/recommenders/examples/multitask) * [Using TensorFlow Recommenders with TFX](https://tensorflow.google.cn/recommenders/examples/ranking_tfx) |

#### Formula:

```
loss = sqrt(mean((y_pred - y_true) ** 2))
```

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

#### Example:

```
>>> m = keras.metrics.RootMeanSquaredError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
0.70710677
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.RootMeanSquaredError()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L222-L224)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/regression_metrics.py#L250-L251)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/regression_metrics.py#L230-L248)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulates root mean squared error statistics.

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Can be a `Tensor` whose rank is either 0, or the same rank as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |

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