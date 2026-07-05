# tf.keras.callbacks.ReduceLROnPlateau

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ReduceLROnPlateau](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ReduceLROnPlateau)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/reduce_lr_on_plateau.py#L11-L149) |

Reduce learning rate when a metric has stopped improving.

Inherits From: [`Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback)

```
tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.1,
    patience=10,
    verbose=0,
    mode='auto',
    min_delta=0.0001,
    cooldown=0,
    min_lr=0.0,
    **kwargs
)
```

Models often benefit from reducing the learning rate by a factor
of 2-10 once learning stagnates. This callback monitors a
quantity and if no improvement is seen for a 'patience' number
of epochs, the learning rate is reduced.

#### Example:

```
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(x_train, y_train, callbacks=[reduce_lr])
```

| Args | |

|  |  |
| --- | --- |
| `monitor` | String. Quantity to be monitored. |
| `factor` | Float. Factor by which the learning rate will be reduced. `new_lr = lr * factor`. |
| `patience` | Integer. Number of epochs with no improvement after which learning rate will be reduced. |
| `verbose` | Integer. 0: quiet, 1: update messages. |
| `mode` | String. One of `{'auto', 'min', 'max'}`. In `'min'` mode, the learning rate will be reduced when the quantity monitored has stopped decreasing; in `'max'` mode it will be reduced when the quantity monitored has stopped increasing; in `'auto'` mode, the direction is automatically inferred from the name of the monitored quantity. |
| `min_delta` | Float. Threshold for measuring the new optimum, to only focus on significant changes. |
| `cooldown` | Integer. Number of epochs to wait before resuming normal operation after the learning rate has been reduced. |
| `min_lr` | Float. Lower bound on the learning rate. |

| Attributes | |

|  |  |
| --- | --- |
| `model` |  |

## Methods

### `in_cooldown`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/reduce_lr_on_plateau.py#L148-L149)

```
in_cooldown()
```

### `on_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L88-L89)

```
on_batch_begin(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_begin`.

### `on_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L91-L92)

```
on_batch_end(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_end`.

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L94-L104)

```
on_epoch_begin(
    epoch, logs=None
)
```

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should
only be called during TRAIN mode.

| Args | |

|  |  |
| --- | --- |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/reduce_lr_on_plateau.py#L105-L146)

```
on_epoch_end(
    epoch, logs=None
)
```

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should
only be called during TRAIN mode.

| Args | |

|  |  |
| --- | --- |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict, metric results for this training epoch, and for the validation epoch if validation is performed. Validation result keys are prefixed with `val_`. For training epoch, the values of the `Model`'s metrics are returned. Example: `{'loss': 0.2, 'accuracy': 0.7}`. |

### `on_predict_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L189-L202)

```
on_predict_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L204-L216)

```
on_predict_batch_end(
    batch, logs=None
)
```

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_predict_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L260-L268)

```
on_predict_begin(
    logs=None
)
```

Called at the beginning of prediction.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L270-L278)

```
on_predict_end(
    logs=None
)
```

Called at the end of prediction.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L154-L170)

```
on_test_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L172-L187)

```
on_test_batch_end(
    batch, logs=None
)
```

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_test_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L239-L247)

```
on_test_begin(
    logs=None
)
```

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L249-L258)

```
on_test_end(
    logs=None
)
```

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently the output of the last call to `on_test_batch_end()` is passed to this argument for this method but that may change in the future. |

### `on_train_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L121-L136)

```
on_train_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L138-L152)

```
on_train_batch_end(
    batch, logs=None
)
```

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
`Model` is set to `N`, this method will only be called every
`N` batches.

| Args | |

|  |  |
| --- | --- |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_train_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/reduce_lr_on_plateau.py#L102-L103)

```
on_train_begin(
    logs=None
)
```

Called at the beginning of training.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L228-L237)

```
on_train_end(
    logs=None
)
```

Called at the end of training.

Subclasses should override for any actions to run.

| Args | |

|  |  |
| --- | --- |
| `logs` | Dict. Currently the output of the last call to `on_epoch_end()` is passed to this argument for this method but that may change in the future. |

### `set_model`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L73-L74)

```
set_model(
    model
)
```

### `set_params`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L70-L71)

```
set_params(
    params
)
```