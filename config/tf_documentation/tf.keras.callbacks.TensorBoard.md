# tf.keras.callbacks.TensorBoard

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/TensorBoard](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/TensorBoard)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L17-L628) |

Enable visualizations for TensorBoard.

Inherits From: [`Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback)

```
tf.keras.callbacks.TensorBoard(
    log_dir='logs',
    histogram_freq=0,
    write_graph=True,
    write_images=False,
    write_steps_per_second=False,
    update_freq='epoch',
    profile_batch=0,
    embeddings_freq=0,
    embeddings_metadata=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate TensorBoard: TensorFlow's visualization toolkit](https://tensorflow.google.cn/guide/migrate/tensorboard) | * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Transfer learning with TensorFlow Hub](https://tensorflow.google.cn/tutorials/images/transfer_learning_with_hub) * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [TensorBoard Scalars: Logging training metrics in Keras](https://tensorflow.google.cn/tensorboard/scalars_and_keras) |

TensorBoard is a visualization tool provided with TensorFlow. A TensorFlow
installation is required to use this callback.

This callback logs events for TensorBoard, including:

* Metrics summary plots
* Training graph visualization
* Weight histograms
* Sampled profiling

When used in `model.evaluate()` or regular validation
in addition to epoch summaries, there will be a summary that records
evaluation metrics vs `model.optimizer.iterations` written. The metric names
will be prepended with `evaluation`, with `model.optimizer.iterations` being
the step in the visualized TensorBoard.

If you have installed TensorFlow with pip, you should be able
to launch TensorBoard from the command line:

```
tensorboard --logdir=path_to_your_logs
```

You can find more information about TensorBoard
[here](https://tensorflow.google.cn/get_started/summaries_and_tensorboard).

| Args | |

|  |  |
| --- | --- |
| `log_dir` | the path of the directory where to save the log files to be parsed by TensorBoard. e.g., `log_dir = os.path.join(working_dir, 'logs')`. This directory should not be reused by any other callbacks. |
| `histogram_freq` | frequency (in epochs) at which to compute weight histograms for the layers of the model. If set to 0, histograms won't be computed. Validation data (or split) must be specified for histogram visualizations. |
| `write_graph` | (Not supported at this time) Whether to visualize the graph in TensorBoard. Note that the log file can become quite large when `write_graph` is set to `True`. |
| `write_images` | whether to write model weights to visualize as image in TensorBoard. |
| `write_steps_per_second` | whether to log the training steps per second into TensorBoard. This supports both epoch and batch frequency logging. |
| `update_freq` | `"batch"` or `"epoch"` or integer. When using `"epoch"`, writes the losses and metrics to TensorBoard after every epoch. If using an integer, let's say `1000`, all metrics and losses (including custom ones added by [`Model.compile`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#compile)) will be logged to TensorBoard every 1000 batches. `"batch"` is a synonym for 1, meaning that they will be written every batch. Note however that writing too frequently to TensorBoard can slow down your training, especially when used with distribution strategies as it will incur additional synchronization overhead. Batch-level summary writing is also available via `train_step` override. Please see [TensorBoard Scalars tutorial](https://tensorflow.google.cn/tensorboard/scalars_and_keras#batch-level_logging) # noqa: E501 for more details. |
| `profile_batch` | (Not supported at this time) Profile the batch(es) to sample compute characteristics. profile\_batch must be a non-negative integer or a tuple of integers. A pair of positive integers signify a range of batches to profile. By default, profiling is disabled. |
| `embeddings_freq` | frequency (in epochs) at which embedding layers will be visualized. If set to 0, embeddings won't be visualized. |
| `embeddings_metadata` | Dictionary which maps embedding layer names to the filename of a file in which to save metadata for the embedding layer. In case the same metadata file is to be used for all embedding layers, a single filename can be passed. |

#### Examples:

```
tensorboard_callback = keras.callbacks.TensorBoard(log_dir="./logs")
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
# Then run the tensorboard command to view the visualizations.
```

Custom batch-level summaries in a subclassed Model:

```
class MyModel(keras.Model):

    def build(self, _):
        self.dense = keras.layers.Dense(10)

    def call(self, x):
        outputs = self.dense(x)
        tf.summary.histogram('outputs', outputs)
        return outputs

model = MyModel()
model.compile('sgd', 'mse')

# Make sure to set `update_freq=N` to log a batch-level summary every N
# batches.  In addition to any `tf.summary` contained in `model.call()`,
# metrics added in `Model.compile` will be logged every N batches.
tb_callback = keras.callbacks.TensorBoard('./logs', update_freq=1)
model.fit(x_train, y_train, callbacks=[tb_callback])
```

Custom batch-level summaries in a Functional API Model:

```
def my_summary(x):
    tf.summary.histogram('x', x)
    return x

inputs = keras.Input(10)
x = keras.layers.Dense(10)(inputs)
outputs = keras.layers.Lambda(my_summary)(x)
model = keras.Model(inputs, outputs)
model.compile('sgd', 'mse')

# Make sure to set `update_freq=N` to log a batch-level summary every N
# batches. In addition to any `tf.summary` contained in `Model.call`,
# metrics added in `Model.compile` will be logged every N batches.
tb_callback = keras.callbacks.TensorBoard('./logs', update_freq=1)
model.fit(x_train, y_train, callbacks=[tb_callback])
```

#### Profiling:

```
# Profile a single batch, e.g. the 5th batch.
tensorboard_callback = keras.callbacks.TensorBoard(
    log_dir='./logs', profile_batch=5)
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])

# Profile a range of batches, e.g. from 10 to 20.
tensorboard_callback = keras.callbacks.TensorBoard(
    log_dir='./logs', profile_batch=(10,20))
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
```

| Attributes | |

|  |  |
| --- | --- |
| `model` |  |

|  |  |
| --- | --- |
| `summary` |  |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L466-L470)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L472-L480)

```
on_epoch_end(
    epoch, logs=None
)
```

Runs metrics and histogram summaries at epoch end.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L412-L413)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L415-L424)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L431-L439)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L441-L464)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L399-L402)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L404-L410)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/tensorboard.py#L201-L219)

```
set_model(
    model
)
```

Sets Keras model and writes graph if specified.

### `set_params`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/callbacks/callback.py#L70-L71)

```
set_params(
    params
)
```