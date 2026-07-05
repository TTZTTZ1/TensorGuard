# tf.keras.models.Sequential

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/models/Sequential](https://tensorflow.google.cn/api_docs/python/tf/keras/models/Sequential)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/sequential.py#L17-L349) |

`Sequential` groups a linear stack of layers into a `Model`.

Inherits From: [`Model`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.models.Sequential`](https://tensorflow.google.cn/api_docs/python/tf/keras/Sequential)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Sequential`](https://tensorflow.google.cn/api_docs/python/tf/keras/Sequential)

```
tf.keras.Sequential(
    layers=None, trainable=True, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with TensorFlow](https://tensorflow.google.cn/guide/distributed_training) * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Migration examples: Canned Estimators](https://tensorflow.google.cn/guide/migrate/canned_estimators) * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) | * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

#### Examples:

```
model = keras.Sequential()
model.add(keras.Input(shape=(16,)))
model.add(keras.layers.Dense(8))

# Note that you can also omit the initial `Input`.
# In that case the model doesn't have any weights until the first call
# to a training/evaluation method (since it isn't yet built):
model = keras.Sequential()
model.add(keras.layers.Dense(8))
model.add(keras.layers.Dense(4))
# model.weights not created yet

# Whereas if you specify an `Input`, the model gets built
# continuously as you are adding layers:
model = keras.Sequential()
model.add(keras.Input(shape=(16,)))
model.add(keras.layers.Dense(8))
len(model.weights)  # Returns "2"

# When using the delayed-build pattern (no input shape specified), you can
# choose to manually build your model by calling
# `build(batch_input_shape)`:
model = keras.Sequential()
model.add(keras.layers.Dense(8))
model.add(keras.layers.Dense(4))
model.build((None, 16))
len(model.weights)  # Returns "4"

# Note that when using the delayed-build pattern (no input shape specified),
# the model gets built the first time you call `fit`, `eval`, or `predict`,
# or the first time you call the model on some input data.
model = keras.Sequential()
model.add(keras.layers.Dense(8))
model.add(keras.layers.Dense(1))
model.compile(optimizer='sgd', loss='mse')
# This builds the model for the first time:
model.fit(x, y, batch_size=32, epochs=10)
```

| Attributes | |

|  |  |
| --- | --- |
| `compiled_metrics` |  |

|  |  |
| --- | --- |
| `distribute_reduction_method` |  |

|  |  |
| --- | --- |
| `distribute_strategy` |  |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `input_shape` |  |

|  |  |
| --- | --- |
| `inputs` |  |

|  |  |
| --- | --- |
| `jit_compile` |  |

|  |  |
| --- | --- |
| `layers` |  |

|  |  |
| --- | --- |
| `metrics_names` |  |

|  |  |
| --- | --- |
| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output_shape` |  |

|  |  |
| --- | --- |
| `outputs` |  |

|  |  |
| --- | --- |
| `run_eagerly` |  |

## Methods

### `add`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/sequential.py#L76-L123)

```
add(
    layer, rebuild=True
)
```

Adds a layer instance on top of the layer stack.

| Args | |

|  |  |
| --- | --- |
| `layer` | layer instance. |

### `compile`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L29-L193)

```
compile(
    optimizer='rmsprop',
    loss=None,
    loss_weights=None,
    metrics=None,
    weighted_metrics=None,
    run_eagerly=False,
    steps_per_execution=1,
    jit_compile='auto',
    auto_scale_loss=True
)
```

Configures the model for training.

#### Example:

```
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[
        keras.metrics.BinaryAccuracy(),
        keras.metrics.FalseNegatives(),
    ],
)
```

| Args | |

|  |  |
| --- | --- |
| `optimizer` | String (name of optimizer) or optimizer instance. See [`keras.optimizers`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers). |
| `loss` | Loss function. May be a string (name of loss function), or a [`keras.losses.Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss) instance. See [`keras.losses`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses). A loss function is any callable with the signature `loss = fn(y_true, y_pred)`, where `y_true` are the ground truth values, and `y_pred` are the model's predictions. `y_true` should have shape `(batch_size, d0, .. dN)` (except in the case of sparse loss functions such as sparse categorical crossentropy which expects integer arrays of shape `(batch_size, d0, .. dN-1)`). `y_pred` should have shape `(batch_size, d0, .. dN)`. The loss function should return a float tensor. |
| `loss_weights` | Optional list or dictionary specifying scalar coefficients (Python floats) to weight the loss contributions of different model outputs. The loss value that will be minimized by the model will then be the *weighted sum* of all individual losses, weighted by the `loss_weights` coefficients. If a list, it is expected to have a 1:1 mapping to the model's outputs. If a dict, it is expected to map output names (strings) to scalar coefficients. |
| `metrics` | List of metrics to be evaluated by the model during training and testing. Each of this can be a string (name of a built-in function), function or a [`keras.metrics.Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric) instance. See [`keras.metrics`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics). Typically you will use `metrics=['accuracy']`. A function is any callable with the signature `result = fn(y_true, _pred)`. To specify different metrics for different outputs of a multi-output model, you could also pass a dictionary, such as `metrics={'a':'accuracy', 'b':['accuracy', 'mse']}`. You can also pass a list to specify a metric or a list of metrics for each output, such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or `metrics=['accuracy', ['accuracy', 'mse']]`. When you pass the strings 'accuracy' or 'acc', we convert this to one of [`keras.metrics.BinaryAccuracy`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/BinaryAccuracy), [`keras.metrics.CategoricalAccuracy`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/CategoricalAccuracy), [`keras.metrics.SparseCategoricalAccuracy`](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/SparseCategoricalAccuracy) based on the shapes of the targets and of the model output. A similar conversion is done for the strings `"crossentropy"` and `"ce"` as well. The metrics passed here are evaluated without sample weighting; if you would like sample weighting to apply, you can specify your metrics via the `weighted_metrics` argument instead. |
| `weighted_metrics` | List of metrics to be evaluated and weighted by `sample_weight` or `class_weight` during training and testing. |
| `run_eagerly` | Bool. If `True`, this model's forward pass will never be compiled. It is recommended to leave this as `False` when training (for best performance), and to set it to `True` when debugging. |
| `steps_per_execution` | Int. The number of batches to run during each a single compiled function call. Running multiple batches inside a single compiled function call can greatly improve performance on TPUs or small models with a large Python overhead. At most, one full epoch will be run each execution. If a number larger than the size of the epoch is passed, the execution will be truncated to the size of the epoch. Note that if `steps_per_execution` is set to `N`, [`Callback.on_batch_begin`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback#on_batch_begin) and [`Callback.on_batch_end`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback#on_batch_end) methods will only be called every `N` batches (i.e. before/after each compiled function execution). Not supported with the PyTorch backend. |
| `jit_compile` | Bool or `"auto"`. Whether to use XLA compilation when compiling a model. For `jax` and `tensorflow` backends, `jit_compile="auto"` enables XLA compilation if the model supports it, and disabled otherwise. For `torch` backend, `"auto"` will default to eager execution and `jit_compile=True` will run with `torch.compile` with the `"inductor"` backend. |
| `auto_scale_loss` | Bool. If `True` and the model dtype policy is `"mixed_float16"`, the passed optimizer will be automatically wrapped in a `LossScaleOptimizer`, which will dynamically scale the loss to prevent underflow. |

### `compile_from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L848-L874)

```
compile_from_config(
    config
)
```

Compiles the model with the information given in config.

This method uses the information in the config (optimizer, loss,
metrics, etc.) to compile the model.

| Args | |

|  |  |
| --- | --- |
| `config` | Dict containing information for compiling the model. |

### `compiled_loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L600-L609)

```
compiled_loss(
    y, y_pred, sample_weight=None, regularization_losses=None
)
```

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L258-L331)

```
compute_loss(
    x=None, y=None, y_pred=None, sample_weight=None
)
```

Compute the total loss, validate it, and return it.

Subclasses can optionally override this method to provide custom loss
computation logic.

#### Example:

```
class MyModel(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loss_tracker = metrics.Mean(name='loss')

    def compute_loss(self, x, y, y_pred, sample_weight):
        loss = ops.means((y_pred - y) ** 2)
        loss += ops.sum(self.losses)
        self.loss_tracker.update_state(loss)
        return loss

    def reset_metrics(self):
        self.loss_tracker.reset_state()

    @property
    def metrics(self):
        return [self.loss_tracker]

inputs = layers.Input(shape=(10,), name='my_input')
outputs = layers.Dense(10)(inputs)
model = MyModel(inputs, outputs)
model.add_loss(ops.sum(outputs))

optimizer = SGD()
model.compile(optimizer, loss='mse', steps_per_execution=10)
dataset = ...
model.fit(dataset, epochs=2, steps_per_epoch=10)
print(f"Custom loss: {model.loss_tracker.result()}")
```

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Predictions returned by the model (output of `model(x)`) |
| `sample_weight` | Sample weights for weighting the loss function. |

| Returns | |
| The total loss as a scalar tensor, or `None` if no loss results (which is the case when called by [`Model.test_step`](https://tensorflow.google.cn/api_docs/python/tf/keras/Model#test_step)). | |

### `compute_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L375-L413)

```
compute_metrics(
    x, y, y_pred, sample_weight=None
)
```

Update metric states and collect all metrics to be returned.

Subclasses can optionally override this method to provide custom metric
updating and collection logic.

#### Example:

```
class MyModel(Sequential):
    def compute_metrics(self, x, y, y_pred, sample_weight):
        # This super call updates `self.compiled_metrics` and returns
        # results for all metrics listed in `self.metrics`.
        metric_results = super().compute_metrics(
            x, y, y_pred, sample_weight)

        # Note that `self.custom_metric` is not listed
        # in `self.metrics`.
        self.custom_metric.update_state(x, y, y_pred, sample_weight)
        metric_results['metric_name'] = self.custom_metric.result()
        return metric_results
```

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Predictions returned by the model output of `model.call(x)`. |
| `sample_weight` | Sample weights for weighting the loss function. |

| Returns | |
| A `dict` containing values that will be passed to [`keras.callbacks.CallbackList.on_train_batch_end()`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/CallbackList#on_train_batch_end). Typically, the values of the metrics listed in `self.metrics` are returned. | |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `evaluate`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L371-L435)

```
evaluate(
    x=None,
    y=None,
    batch_size=None,
    verbose='auto',
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs
)
```

Returns the loss value & metrics values for the model in test mode.

Computation is done in batches (see the `batch_size` arg.)

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. It could be: |

* A NumPy array (or array-like), or a list of arrays
  (in case the model has multiple inputs).
* A tensor, or a list of tensors
  (in case the model has multiple inputs).
* A dict mapping input names to the corresponding array/tensors,
  if the model has named inputs.
* A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). Should return a tuple
  of either `(inputs, targets)` or
  `(inputs, targets, sample_weights)`.
* A generator or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) returning
  `(inputs, targets)` or `(inputs, targets, sample_weights)`.| `y` | Target data. Like the input data `x`, it could be either NumPy array(s) or backend-native tensor(s). If `x` is a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instance, `y` should not be specified (since targets will be obtained from the iterator/dataset). |
  | `batch_size` | Integer or `None`. Number of samples per batch of computation. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your data is in the form of a dataset, generators, or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instances (since they generate batches). |
  | `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
  | `sample_weight` | Optional NumPy array of weights for the test samples, used for weighting the loss function. You can either pass a flat (1D) NumPy array with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a dataset, instead pass sample weights as the third element of `x`. |
  | `steps` | Integer or `None`. Total number of steps (batches of samples) before declaring the evaluation round finished. Ignored with the default value of `None`. If `x` is a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) and `steps` is `None`, evaluation will run until the dataset is exhausted. |
  | `callbacks` | List of [`keras.callbacks.Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback) instances. List of callbacks to apply during evaluation. |
  | `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

| Returns | |
| Scalar test loss (if the model has a single output and no metrics) or list of scalars (if the model has multiple outputs and/or metrics). The attribute `model.metrics_names` will give you the display labels for the scalar outputs. | |

### `export`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L452-L488)

```
export(
    filepath, format='tf_saved_model'
)
```

Create a TF SavedModel artifact for inference.

**Note:** This can currently only be used with
the TensorFlow or JAX backends.

This method lets you export a model to a lightweight SavedModel artifact
that contains the model's forward pass only (its `call()` method)
and can be served via e.g. TF-Serving. The forward pass is registered
under the name `serve()` (see example below).

The original code of the model (including any custom layers you may
have used) is *no longer* necessary to reload the artifact -- it is
entirely standalone.

| Args | |

|  |  |
| --- | --- |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the artifact. |

#### Example:

```
# Create the artifact
model.export("path/to/location")

# Later, in a different process / environment...
reloaded_artifact = tf.saved_model.load("path/to/location")
predictions = reloaded_artifact.serve(input_data)
```

If you would like to customize your serving endpoints, you can
use the lower-level [`keras.export.ExportArchive`](https://tensorflow.google.cn/api_docs/python/tf/keras/export/ExportArchive) class. The
`export()` method relies on `ExportArchive` internally.

### `fit`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L236-L369)

```
fit(
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose='auto',
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1
)
```

Trains the model for a fixed number of epochs (dataset iterations).

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. It could be: |

* A NumPy array (or array-like), or a list of arrays
  (in case the model has multiple inputs).
* A tensor, or a list of tensors
  (in case the model has multiple inputs).
* A dict mapping input names to the corresponding array/tensors,
  if the model has named inputs.
* A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). Should return a tuple
  of either `(inputs, targets)` or
  `(inputs, targets, sample_weights)`.
* A [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) returning `(inputs,
  targets)` or `(inputs, targets, sample_weights)`.| `y` | Target data. Like the input data `x`, it could be either NumPy array(s) or backend-native tensor(s). If `x` is a dataset, generator, or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instance, `y` should not be specified (since targets will be obtained from `x`). |
  | `batch_size` | Integer or `None`. Number of samples per gradient update. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your data is in the form of datasets, generators, or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instances (since they generate batches). |
  | `epochs` | Integer. Number of epochs to train the model. An epoch is an iteration over the entire `x` and `y` data provided (unless the `steps_per_epoch` flag is set to something other than None). Note that in conjunction with `initial_epoch`, `epochs` is to be understood as "final epoch". The model is not trained for a number of iterations given by `epochs`, but merely until the epoch of index `epochs` is reached. |
  | `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = one line per epoch. "auto" becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g., in a production environment). Defaults to `"auto"`. |
  | `callbacks` | List of [`keras.callbacks.Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback) instances. List of callbacks to apply during training. See [`keras.callbacks`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks). Note [`keras.callbacks.ProgbarLogger`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ProgbarLogger) and [`keras.callbacks.History`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/History) callbacks are created automatically and need not be passed to `model.fit()`. [`keras.callbacks.ProgbarLogger`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/ProgbarLogger) is created or not based on the `verbose` argument in `model.fit()`. |
  | `validation_split` | Float between 0 and 1. Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch. The validation data is selected from the last samples in the `x` and `y` data provided, before shuffling. This argument is not supported when `x` is a dataset, generator or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instance. If both `validation_data` and `validation_split` are provided, `validation_data` will override `validation_split`. |
  | `validation_data` | Data on which to evaluate the loss and any model metrics at the end of each epoch. The model will not be trained on this data. Thus, note the fact that the validation loss of data provided using `validation_split` or `validation_data` is not affected by regularization layers like noise and dropout. `validation_data` will override `validation_split`. It could be: |
* A tuple `(x_val, y_val)` of NumPy arrays or tensors.
* A tuple `(x_val, y_val, val_sample_weights)` of NumPy
  arrays.
* A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).
* A Python generator or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) returning
  `(inputs, targets)` or `(inputs, targets, sample_weights)`.| `shuffle` | Boolean, whether to shuffle the training data before each epoch. This argument is ignored when `x` is a generator or a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). |
  | `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) value, used for weighting the loss function (during training only). This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of `1` must be included for sparse class labels. |
  | `sample_weight` | Optional NumPy array of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) NumPy array with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a dataset, generator, or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instance, instead provide the sample\_weights as the third element of `x`. Note that sample weighting does not apply to metrics specified via the `metrics` argument in `compile()`. To apply sample weighting to your metrics, you can specify them via the `weighted_metrics` in `compile()` instead. |
  | `initial_epoch` | Integer. Epoch at which to start training (useful for resuming a previous training run). |
  | `steps_per_epoch` | Integer or `None`. Total number of steps (batches of samples) before declaring one epoch finished and starting the next epoch. When training with input tensors such as backend-native tensors, the default `None` is equal to the number of samples in your dataset divided by the batch size, or 1 if that cannot be determined. If `x` is a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), and `steps_per_epoch` is `None`, the epoch will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps_per_epoch` argument. If `steps_per_epoch=-1` the training will run indefinitely with an infinitely repeating dataset. |
  | `validation_steps` | Only relevant if `validation_data` is provided. Total number of steps (batches of samples) to draw before stopping when performing validation at the end of every epoch. If `validation_steps` is `None`, validation will run until the `validation_data` dataset is exhausted. In the case of an infinitely repeated dataset, it will run into an infinite loop. If `validation_steps` is specified and only part of the dataset will be consumed, the evaluation will start from the beginning of the dataset at each epoch. This ensures that the same validation samples are used every time. |
  | `validation_batch_size` | Integer or `None`. Number of samples per validation batch. If unspecified, will default to `batch_size`. Do not specify the `validation_batch_size` if your data is in the form of datasets or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instances (since they generate batches). |
  | `validation_freq` | Only relevant if validation data is provided. Specifies how many training epochs to run before a new validation run is performed, e.g. `validation_freq=2` runs validation every 2 epochs. |

Unpacking behavior for iterator-like inputs:
A common pattern is to pass an iterator like object such as a
[`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) or a [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) to `fit()`,
which will in fact yield not only features (`x`)
but optionally targets (`y`) and sample weights (`sample_weight`).
Keras requires that the output of such iterator-likes be
unambiguous. The iterator should return a tuple
of length 1, 2, or 3, where the optional second and third elements
will be used for `y` and `sample_weight` respectively.
Any other type provided will be wrapped in
a length-one tuple, effectively treating everything as `x`. When
yielding dicts, they should still adhere to the top-level tuple
structure,
e.g. `({"x0": x0, "x1": x1}, y)`. Keras will not attempt to separate
features, targets, and weights from the keys of a single dict.
A notable unsupported data type is the `namedtuple`. The reason is
that it behaves like both an ordered datatype (tuple) and a mapping
datatype (dict). So given a namedtuple of the form:
`namedtuple("example_tuple", ["y", "x"])`
it is ambiguous whether to reverse the order of the elements when
interpreting the value. Even worse is a tuple of the form:
`namedtuple("other_tuple", ["x", "y", "z"])`
where it is unclear if the tuple was intended to be unpacked
into `x`, `y`, and `sample_weight` or passed through
as a single element to `x`.

| Returns | |
| A `History` object. Its `History.history` attribute is a record of training loss values and metrics values at successive epochs, as well as validation loss values and validation metrics values (if applicable). | |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/sequential.py#L319-L349)

```
@classmethod
from_config(
    config, custom_objects=None
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `get_compile_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L836-L846)

```
get_compile_config()
```

Returns a serialized config with information for compiling the model.

This method returns a config dictionary containing all the information
(optimizer, loss, metrics, etc.) with which the model was compiled.

| Returns | |
| A dict containing information for compiling the model. | |

### `get_layer`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L175-L214)

```
get_layer(
    name=None, index=None
)
```

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence.
Indices are based on order of horizontal graph traversal (bottom-up).

| Args | |

|  |  |
| --- | --- |
| `name` | String, name of layer. |
| `index` | Integer, index of layer. |

| Returns | |
| A layer instance. | |

### `get_metrics_result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L415-L432)

```
get_metrics_result()
```

Returns the model's metrics values as a dict.

If any of the metric result is a dict (containing multiple metrics),
each of them gets added to the top level returned dict of this method.

| Returns | |
| A `dict` containing values of the metrics listed in `self.metrics`. | |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `load_weights`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L320-L349)

```
load_weights(
    filepath, skip_mismatch=False, **kwargs
)
```

Load weights from a file saved via `save_weights()`.

Weights are loaded based on the network's
topology. This means the architecture should be the same as when the
weights were saved. Note that layers that don't have weights are not
taken into account in the topological ordering, so adding or removing
layers is fine as long as they don't have weights.

**Partial weight loading**

If you have modified your model, for instance by adding a new layer
(with weights) or by changing the shape of the weights of a layer,
you can choose to ignore errors and continue loading
by setting `skip_mismatch=True`. In this case any layer with
mismatching weights will be skipped. A warning will be displayed
for each skipped layer.

| Args | |

|  |  |
| --- | --- |
| `filepath` | String, path to the weights file to load. It can either be a `.weights.h5` file or a legacy `.h5` weights file. |
| `skip_mismatch` | Boolean, whether to skip loading of layers where there is a mismatch in the number of weights, or a mismatch in the shape of the weights. |

### `loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L611-L618)

```
loss(
    y, y_pred, sample_weight=None
)
```

### `make_predict_function`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L187-L234)

```
make_predict_function(
    force=False
)
```

### `make_test_function`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L143-L185)

```
make_test_function(
    force=False
)
```

### `make_train_function`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L97-L141)

```
make_train_function(
    force=False
)
```

### `pop`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/sequential.py#L125-L132)

```
pop(
    rebuild=True
)
```

Removes the last layer in the model.

### `predict`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L437-L513)

```
predict(
    x, batch_size=None, verbose='auto', steps=None, callbacks=None
)
```

Generates output predictions for the input samples.

Computation is done in batches. This method is designed for batch
processing of large numbers of inputs. It is not intended for use inside
of loops that iterate over your data and process small numbers of inputs
at a time.

For small numbers of inputs that fit in one batch,
directly use `__call__()` for faster execution, e.g.,
`model(x)`, or `model(x, training=False)` if you have layers such as
`BatchNormalization` that behave differently during
inference.

**Note:** See [this FAQ entry](https://keras.io/getting_started/faq/#whats-the-difference-between-model-methods-predict-and-call)
for more details about the difference between `Model` methods
`predict()` and `__call__()`.

| Args | |

|  |  |
| --- | --- |
| `x` | Input samples. It could be: |

* A NumPy array (or array-like), or a list of arrays
  (in case the model has multiple inputs).
* A tensor, or a list of tensors
  (in case the model has multiple inputs).
* A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).
* A [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instance.| `batch_size` | Integer or `None`. Number of samples per batch. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your data is in the form of dataset, generators, or [`keras.utils.PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset) instances (since they generate batches). |
  | `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
  | `steps` | Total number of steps (batches of samples) before declaring the prediction round finished. Ignored with the default value of `None`. If `x` is a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) and `steps` is `None`, `predict()` will run until the input dataset is exhausted. |
  | `callbacks` | List of [`keras.callbacks.Callback`](https://tensorflow.google.cn/api_docs/python/tf/keras/callbacks/Callback) instances. List of callbacks to apply during prediction. |

| Returns | |
| NumPy array(s) of predictions. | |

### `predict_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L565-L571)

```
predict_on_batch(
    x
)
```

Returns predictions for a single batch of samples.

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. It must be array-like. |

| Returns | |
| NumPy array(s) of predictions. | |

### `predict_step`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L89-L95)

```
predict_step(
    data
)
```

### `reset_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L254-L256)

```
reset_metrics()
```

### `save`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L266-L305)

```
save(
    filepath, overwrite=True, **kwargs
)
```

Saves a model as a `.keras` file.

| Args | |

|  |  |
| --- | --- |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the model. Must end in `.keras`. |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |
| `save_format` | The `save_format` argument is deprecated in Keras 3. Format to use, as a string. Only the `"keras"` format is supported at this time. |

#### Example:

```
model = keras.Sequential(
    [
        keras.layers.Dense(5, input_shape=(3,)),
        keras.layers.Softmax(),
    ],
)
model.save("model.keras")
loaded_model = keras.saving.load_model("model.keras")
x = keras.random.uniform((10, 3))
assert np.allclose(model.predict(x), loaded_model.predict(x))
```

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file contains:

* The model's configuration (architecture)
* The model's weights
* The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

### `save_weights`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L307-L318)

```
save_weights(
    filepath, overwrite=True
)
```

Saves all layer weights to a `.weights.h5` file.

| Args | |

|  |  |
| --- | --- |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the model. Must end in `.weights.h5`. |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |

### `stateless_compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/trainer.py#L333-L373)

```
stateless_compute_loss(
    trainable_variables,
    non_trainable_variables,
    metrics_variables,
    x=None,
    y=None,
    y_pred=None,
    sample_weight=None
)
```

### `summary`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L216-L264)

```
summary(
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=False,
    show_trainable=False,
    layer_range=None
)
```

Prints a string summary of the network.

| Args | |

|  |  |
| --- | --- |
| `line_length` | Total length of printed lines (e.g. set this to adapt the display to different terminal window sizes). |
| `positions` | Relative or absolute positions of log elements in each line. If not provided, becomes `[0.3, 0.6, 0.70, 1.]`. Defaults to `None`. |
| `print_fn` | Print function to use. By default, prints to `stdout`. If `stdout` doesn't work in your environment, change to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary. |
| `expand_nested` | Whether to expand the nested models. Defaults to `False`. |
| `show_trainable` | Whether to show if a layer is trainable. Defaults to `False`. |
| `layer_range` | a list or tuple of 2 strings, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers to be printed in summary. It also accepts regex patterns instead of exact name. In such case, start predicate will be the first element it matches to `layer_range[0]` and the end predicate will be the last element it matches to `layer_range[1]`. By default `None` which considers all layers of model. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `summary()` is called before the model is built. |

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```

### `test_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L546-L563)

```
test_on_batch(
    x, y=None, sample_weight=None, return_dict=False
)
```

Test the model on a single batch of samples.

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

| Returns | |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). | |

### `test_step`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L75-L87)

```
test_step(
    data
)
```

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/models/model.py#L434-L450)

```
to_json(
    **kwargs
)
```

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use
[`keras.models.model_from_json(json_string, custom_objects={...})`](https://tensorflow.google.cn/api_docs/python/tf/keras/models/model_from_json).

| Args | |

|  |  |
| --- | --- |
| `**kwargs` | Additional keyword arguments to be passed to `json.dumps()`. |

| Returns | |
| A JSON string. | |

### `train_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L515-L544)

```
train_on_batch(
    x, y=None, sample_weight=None, class_weight=None, return_dict=False
)
```

Runs a single gradient update on a single batch of data.

| Args | |

|  |  |
| --- | --- |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) to apply to the model's loss for the samples from this class during training. This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of 1 must be included for sparse class labels. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

| Returns | |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). | |

### `train_step`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/trainer.py#L45-L73)

```
train_step(
    data
)
```