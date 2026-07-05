# tf.keras.metrics.SparseCategoricalCrossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/probabilistic_metrics.py#L264-L347) |

Computes the crossentropy metric between the labels and predictions.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.SparseCategoricalCrossentropy(
    name='sparse_categorical_crossentropy',
    dtype=None,
    from_logits=False,
    axis=-1
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) | * [Working with tff's ClientData.](https://tensorflow.google.cn/federated/tutorials/working_with_client_data) |

Use this crossentropy metric when there are two or more label classes.
It expects labels to be provided as integers. If you want to provide labels
that are one-hot encoded, please use the `CategoricalCrossentropy`
metric instead.

There should be `num_classes` floating point values per feature for `y_pred`
and a single floating point value per feature for `y_true`.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `from_logits` | (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution. |
| `axis` | (Optional) Defaults to `-1`. The dimension along which entropy is computed. |

#### Example:

#### Example:

```
>>> # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]]
>>> # logits = log(y_pred)
>>> # softmax = exp(logits) / sum(exp(logits), axis=-1)
>>> # softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
>>> # xent = -sum(y * log(softmax), 1)
>>> # log(softmax) = [[-2.9957, -0.0513, -16.1181],
>>> #                [-2.3026, -0.2231, -2.3026]]
>>> # y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]]
>>> # xent = [0.0513, 2.3026]
>>> # Reduced xent = (0.0513 + 2.3026) / 2
>>> m = keras.metrics.SparseCategoricalCrossentropy()
>>> m.update_state([1, 2],
...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
>>> m.result()
1.1769392
```

```
>>> m.reset_state()
>>> m.update_state([1, 2],
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
    metrics=[keras.metrics.SparseCategoricalCrossentropy()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/probabilistic_metrics.py#L341-L347)

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