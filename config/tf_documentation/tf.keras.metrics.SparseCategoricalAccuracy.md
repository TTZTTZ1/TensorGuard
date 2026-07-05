# tf.keras.metrics.SparseCategoricalAccuracy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseCategoricalAccuracy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseCategoricalAccuracy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L261-L312) |

Calculates how often predictions match integer labels.

Inherits From: [`MeanMetricWrapper`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MeanMetricWrapper), [`Mean`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean), [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.SparseCategoricalAccuracy(
    name='sparse_categorical_accuracy', dtype=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) * [Use TPUs](https://tensorflow.google.cn/guide/tpu) * [Multi-GPU and distributed training](https://tensorflow.google.cn/guide/keras/distributed_training) | * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [TensorFlow 2 quickstart for experts](https://tensorflow.google.cn/tutorials/quickstart/advanced) * [Custom training: walkthrough](https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough) |

```
acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))
```

You can provide logits of classes as `y_pred`, since argmax of
logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used
to compute the frequency with which `y_pred` matches `y_true`. This
frequency is ultimately returned as `sparse categorical accuracy`: an
idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
>>> m = keras.metrics.SparseCategoricalAccuracy()
>>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=[keras.metrics.SparseCategoricalAccuracy()])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/accuracy_metrics.py#L311-L312)

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