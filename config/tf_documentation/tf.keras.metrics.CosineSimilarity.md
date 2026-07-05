# tf.keras.metrics.CosineSimilarity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/CosineSimilarity](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/CosineSimilarity)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/regression_metrics.py#L254-L308) |

Computes the cosine similarity between the labels and predictions.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.CosineSimilarity(
    name='cosine_similarity', dtype=None, axis=-1
)
```

#### Formula:

```
loss = sum(l2_norm(y_true) * l2_norm(y_pred))
```

See: [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity).
This metric keeps the average cosine similarity between `predictions` and
`labels` over a stream of data.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `axis` | (Optional) Defaults to `-1`. The dimension along which the cosine similarity is computed. |

#### Example:

#### Example:

```
>>> # l2_norm(y_true) = [[0., 1.], [1./1.414, 1./1.414]]
>>> # l2_norm(y_pred) = [[1., 0.], [1./1.414, 1./1.414]]
>>> # l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]]
>>> # result = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1))
>>> #        = ((0. + 0.) +  (0.5 + 0.5)) / 2
>>> m = keras.metrics.CosineSimilarity(axis=1)
>>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]])
>>> m.result()
0.49999997
>>> m.reset_state()
>>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]],
...                sample_weight=[0.3, 0.7])
>>> m.result()
0.6999999
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.CosineSimilarity(axis=1)])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/regression_metrics.py#L307-L308)

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