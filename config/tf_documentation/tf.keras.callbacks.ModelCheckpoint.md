# tf.keras.callbacks.ModelCheckpoint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ModelCheckpoint](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ModelCheckpoint)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/model_checkpoint.py#L14-L416) |

Callback to save the Keras model or model weights at some frequency.

Inherits From: [`Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback)

```
tf.keras.callbacks.ModelCheckpoint(
    filepath,
    monitor='val_loss',
    verbose=0,
    save_best_only=False,
    save_weights_only=False,
    mode='auto',
    save_freq='epoch',
    initial_value_threshold=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate checkpoint saving](https://tensorflow.google.cn/guide/migrate/checkpoint_saver) * [Migrate evaluation](https://tensorflow.google.cn/guide/migrate/evaluator) * [Multi-GPU and distributed training](https://tensorflow.google.cn/guide/keras/distributed_training) | * [Save and load models](https://tensorflow.google.cn/tutorials/keras/save_and_load) * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) |

`ModelCheckpoint` callback is used in conjunction with training using
`model.fit()` to save a model or weights (in a checkpoint file) at some
interval, so the model or weights can be loaded later to continue the
training from the state saved.

A few options this callback provides include:

* Whether to only keep the model that has achieved the "best performance" so
  far, or whether to save the model at the end of every epoch regardless of
  performance.
* Definition of "best"; which quantity to monitor and whether it should be
  maximized or minimized.
* The frequency it should save at. Currently, the callback supports saving
  at the end of every epoch, or after a fixed number of training batches.
* Whether only weights are saved, or the whole model is saved.

#### Example:

```
model.compile(loss=..., optimizer=...,
              metrics=['accuracy'])

EPOCHS = 10
checkpoint_filepath = '/tmp/ckpt/checkpoint.model.keras'
model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)

# Model is saved at the end of every epoch, if it's the best seen so far.
model.fit(epochs=EPOCHS, callbacks=[model_checkpoint_callback])

# The model (that are considered the best) can be loaded as -
keras.models.load_model(checkpoint_filepath)

# Alternatively, one could checkpoint just the model weights as -
checkpoint_filepath = '/tmp/ckpt/checkpoint.weights.h5'
model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)

# Model weights are saved at the end of every epoch, if it's the best seen
# so far.
model.fit(epochs=EPOCHS, callbacks=[model_checkpoint_callback])

# The model weights (that are considered the best) can be loaded as -
model.load_weights(checkpoint_filepath)
```

| Args | |

|  |  |
| --- | --- |
| `filepath` | string or `PathLike`, path to save the model file. `filepath` can contain named formatting options, which will be filled the value of `epoch` and keys in `logs` (passed in `on_epoch_end`). The `filepath` name needs to end with `".weights.h5"` when `save_weights_only=True` or should end with `".keras"` when checkpoint saving the whole model (default). For example: if `filepath` is `"{epoch:02d}-{val_loss:.2f}.keras"`, then the model checkpoints will be saved with the epoch number and the validation loss in the filename. The directory of the filepath should not be reused by any other callbacks to avoid conflicts. |
| `monitor` | The metric name to monitor. Typically the metrics are set by the [`Model.compile`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#compile) method. Note: |

* Prefix the name with `"val_"` to monitor validation metrics.
* Use `"loss"` or `"val_loss"` to monitor the model's total loss.
* If you specify metrics as strings, like `"accuracy"`, pass the
  same string (with or without the `"val_"` prefix).
* If you pass [`metrics.Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric) objects, `monitor` should be set to
  `metric.name`
* If you're not sure about the metric names you can check the
  contents of the `history.history` dictionary returned by
  `history = model.fit()`
* Multi-output models set additional prefixes on the metric names.|  |  |
  | --- | --- |
  | `verbose` | Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1 displays messages when the callback takes an action. |
  | `save_best_only` | if `save_best_only=True`, it only saves when the model is considered the "best" and the latest best model according to the quantity monitored will not be overwritten. If `filepath` doesn't contain formatting options like `{epoch}` then `filepath` will be overwritten by each new better model. |
  | `mode` | one of {`"auto"`, `"min"`, `"max"`}. If `save_best_only=True`, the decision to overwrite the current save file is made based on either the maximization or the minimization of the monitored quantity. For `val_acc`, this should be `"max"`, for `val_loss` this should be `"min"`, etc. In `"auto"` mode, the mode is set to `"max"` if the quantities monitored are `"acc"` or start with `"fmeasure"` and are set to `"min"` for the rest of the quantities. |
  | `save_weights_only` | if `True`, then only the model's weights will be saved (`model.save_weights(filepath)`), else the full model is saved (`model.save(filepath)`). |
  | `save_freq` | `"epoch"` or integer. When using `"epoch"`, the callback saves the model after each epoch. When using integer, the callback saves the model at end of this many batches. If the `Model` is compiled with `steps_per_execution=N`, then the saving criteria will be checked every Nth batch. Note that if the saving isn't aligned to epochs, the monitored metric may potentially be less reliable (it could reflect as little as 1 batch, since the metrics get reset every epoch). Defaults to `"epoch"`. |
  | `initial_value_threshold` | Floating point initial "best" value of the metric to be monitored. Only applies if `save_best_value=True`. Only overwrites the model weights already saved if the performance of current model is better than this value. |

| Attributes | |

|  |  |
| --- | --- |
| `model` |  |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/model_checkpoint.py#L201-L202)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/model_checkpoint.py#L204-L206)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/model_checkpoint.py#L197-L199)

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