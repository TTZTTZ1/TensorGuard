# tf.keras.callbacks.Callback

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L5-L278) |

Base class used to build new callbacks.

```
tf.keras.callbacks.Callback()
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate the fault tolerance mechanism](https://tensorflow.google.cn/guide/migrate/fault_tolerance) * [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://tensorflow.google.cn/guide/migrate/logging_stop_hook) * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) * [Migrate SessionRunHook to Keras callbacks](https://tensorflow.google.cn/guide/migrate/sessionrunhook_callback) | * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Image segmentation](https://tensorflow.google.cn/tutorials/images/segmentation) * [Uncertainty-aware Deep Learning with SNGP](https://tensorflow.google.cn/tutorials/understanding/sngp) * [Assess privacy risks with the TensorFlow Privacy Report](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/privacy_report) * [Image captioning with visual attention](https://tensorflow.google.cn/text/tutorials/image_captioning) |

Callbacks can be passed to keras methods such as `fit()`, `evaluate()`, and
`predict()` in order to hook into the various stages of the model training,
evaluation, and inference lifecycle.

To create a custom callback, subclass [`keras.callbacks.Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback) and
override the method associated with the stage of interest.

#### Example:

```
>>> training_finished = False
>>> class MyCallback(Callback):
...   def on_train_end(self, logs=None):
...     global training_finished
...     training_finished = True
>>> model = Sequential([
...     layers.Dense(1, input_shape=(1,))])
>>> model.compile(loss='mean_squared_error')
>>> model.fit(np.array([[1.0]]), np.array([[1.0]]),
...           callbacks=[MyCallback()])
>>> assert training_finished == True
```

If you want to use `Callback` objects in a custom training loop:

1. You should pack all your callbacks into a single [`callbacks.CallbackList`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/CallbackList)
   so they can all be called together.
2. You will need to manually call all the `on_*` methods at the appropriate
   locations in your loop. Like this:

#### Example:

```
callbacks =  keras.callbacks.CallbackList([...])
callbacks.append(...)
callbacks.on_train_begin(...)
for epoch in range(EPOCHS):
    callbacks.on_epoch_begin(epoch)
    for i, data in dataset.enumerate():
    callbacks.on_train_batch_begin(i)
    batch_logs = model.train_step(data)
    callbacks.on_train_batch_end(i, batch_logs)
    epoch_logs = ...
    callbacks.on_epoch_end(epoch, epoch_logs)
final_logs=...
callbacks.on_train_end(final_logs)
```

The `logs` dictionary that callback methods
take as argument will contain keys for quantities relevant to
the current batch or epoch (see method-specific docstrings).

| Attributes | |

|  |  |
| --- | --- |
| `params` | Dict. Training parameters (eg. verbosity, batch size, number of epochs...). |
| `model` | Instance of `Model`. Reference of the model being trained. |

## Methods

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L106-L119)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L218-L226)

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