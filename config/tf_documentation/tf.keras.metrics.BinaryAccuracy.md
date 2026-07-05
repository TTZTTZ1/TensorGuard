# tf.keras.metrics.BinaryAccuracy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/BinaryAccuracy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/BinaryAccuracy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L78-L137) |

Calculates how often predictions match binary labels.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.BinaryAccuracy(
    name='binary_accuracy', dtype=None, threshold=0.5
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Classification on imbalanced data](https://tensorflow.google.cn/tutorials/structured_data/imbalanced_data) * [TensorFlow Constrained Optimization Example Using CelebA Dataset](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

This metric creates two local variables, `total` and `count` that are used
to compute the frequency with which `y_pred` matches `y_true`. This
frequency is ultimately returned as `binary accuracy`: an idempotent
operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `threshold` | (Optional) Float representing the threshold for deciding whether prediction values are 1 or 0. |

#### Example:

```
>>> m = keras.metrics.BinaryAccuracy()
>>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]])
>>> m.result()
0.75
```

```
>>> m.reset_state()
>>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]],
...                sample_weight=[1, 0, 0, 1])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=[keras.metrics.BinaryAccuracy()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L132-L137)

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