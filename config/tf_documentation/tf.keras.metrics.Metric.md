# tf.keras.metrics.Metric

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Metric](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Metric)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L10-L247) |

Encapsulates metric logic and state.

#### View aliases

**Main aliases**

[`tf.keras.metrics.Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.Metric(
    dtype=None, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
m = SomeMetric(...)
for input in ...:
    m.update_state(input)
print('Final result: ', m.result())
```

Usage with `compile()` API:

```
model = keras.Sequential()
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=keras.optimizers.RMSprop(0.01),
              loss=keras.losses.CategoricalCrossentropy(),
              metrics=[keras.metrics.CategoricalAccuracy()])

data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

model.fit(data, labels, epochs=10)
```

To be implemented by subclasses:

* `__init__()`: All state variables should be created in this method by
  calling `self.add_variable()` like: `self.var = self.add_variable(...)`
* `update_state()`: Has all updates to the state variables like:
  `self.var.assign(...)`.
* `result()`: Computes and returns a scalar value or a dict of scalar values
  for the metric from the state variables.

Example subclass implementation:

```
class BinaryTruePositives(Metric):

    def __init__(self, name='binary_true_positives', **kwargs):
        super().__init__(name=name, **kwargs)
        self.true_positives = self.add_variable(
            shape=(),
            initializer='zeros',
            name='true_positives'
        )

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = ops.cast(y_true, "bool")
        y_pred = ops.cast(y_pred, "bool")

        values = ops.logical_and(
            ops.equal(y_true, True), ops.equal(y_pred, True))
        values = ops.cast(values, self.dtype)
        if sample_weight is not None:
            sample_weight = ops.cast(sample_weight, self.dtype)
            sample_weight = ops.broadcast_to(
                sample_weight, ops.shape(values)
            )
            values = ops.multiply(values, sample_weight)
        self.true_positives.assign(self.true_positives + ops.sum(values))

    def result(self):
        return self.true_positives
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L102-L109)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L140-L146)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L111-L113)

```
update_state(
    *args, **kwargs
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