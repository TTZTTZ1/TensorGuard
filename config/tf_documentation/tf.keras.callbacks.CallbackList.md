# tf.keras.callbacks.CallbackList

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/CallbackList](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/CallbackList)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L8-L156) |

Container abstracting a list of callbacks.

Inherits From: [`Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback)

```
tf.keras.callbacks.CallbackList(
    callbacks=None, add_history=False, add_progbar=False, model=None, **params
)
```

| Args | |

|  |  |
| --- | --- |
| `callbacks` | List of `Callback` instances. |
| `add_history` | Whether a `History` callback should be added, if one does not already exist in the `callbacks` list. |
| `add_progbar` | Whether a `ProgbarLogger` callback should be added, if one does not already exist in the `callbacks` list. |
| `model` | The `Model` these callbacks are used with. |
| `**params` | If provided, parameters will be passed to each `Callback` via [`Callback.set_params`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback#set_params). |

| Attributes | |

|  |  |
| --- | --- |
| `model` |  |

## Methods

### `append`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L63-L64)

```
append(
    callback
)
```

### `on_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L78-L81)

```
on_batch_begin(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_begin`.

### `on_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L83-L86)

```
on_batch_end(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_end`.

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L88-L91)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L93-L96)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L118-L121)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L123-L126)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L148-L151)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L153-L156)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L108-L111)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L113-L116)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L138-L141)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L143-L146)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L98-L101)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L103-L106)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L128-L131)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L133-L136)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L71-L76)

```
set_model(
    model
)
```

### `set_params`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback_list.py#L66-L69)

```
set_params(
    params
)
```