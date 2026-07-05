# tf.nn.RNNCellResidualWrapper

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/RNNCellResidualWrapper](https://tensorflow.google.cn/api_docs/python/tf/nn/RNNCellResidualWrapper)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L110-L119) |

RNNCell wrapper that ensures cell inputs are added to the outputs. (deprecated)

Inherits From: [`Module`](https://tensorflow.google.cn/api_docs/python/tf/Module)

```
tf.nn.RNNCellResidualWrapper(
    *args, **kwargs
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use tf.keras.layers.RNN instead.

| Args | |

|  |  |
| --- | --- |
| `cell` | An instance of `RNNCell`. |
| `residual_fn` | (Optional) The function to map raw cell inputs and raw cell outputs to the actual cell outputs of the residual network. Defaults to calling nest.map\_structure on (lambda i, o: i + o), inputs and outputs. |
| `**kwargs` | dict of keyword arguments for base layer. |

| Attributes | |

|  |  |
| --- | --- |
| `activity_regularizer` | Optional regularizer function for the output of this layer. |
| `compute_dtype` | The dtype of the layer's computations. |

This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless
mixed precision is used, this is the same as [`Layer.dtype`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer#dtype), the dtype of
the weights.

Layers automatically cast their inputs to the compute dtype, which causes
computations and the output to be in the compute dtype as well. This is done
by the base Layer class in [`Layer.call`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer#__call__), so you do not have to insert
these casts if implementing your own layer.

Layers often perform certain internal computations in higher precision when
`compute_dtype` is float16 or bfloat16 for numeric stability. The output
will still typically be float16 or bfloat16 in such cases.| `dtype` | The dtype of the layer weights. |

This is equivalent to `Layer.dtype_policy.variable_dtype`. Unless
mixed precision is used, this is the same as [`Layer.compute_dtype`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer#compute_dtype), the
dtype of the layer's computations.| `dtype_policy` | The dtype policy associated with this layer. |

This is an instance of a [`tf.keras.mixed_precision.Policy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy).| `dynamic` | Whether the layer is dynamic (eager-only); set in the constructor. |
| `input` | Retrieves the input tensor(s) of a layer. |

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer.|  |  |
| --- | --- |
| `input_spec` | `InputSpec` instance(s) describing the input format for this layer. |

When you create a layer subclass, you can set `self.input_spec` to enable
the layer to run input compatibility checks when it is called.
Consider a `Conv2D` layer: it can only be called on a single input tensor
of rank 4. As such, you can set, in `__init__()`:

```
self.input_spec = tf.keras.layers.InputSpec(ndim=4)
```

Now, if you try to call the layer on an input that isn't rank 4
(for instance, an input of shape `(2,)`, it will raise a nicely-formatted
error:

```
ValueError: Input 0 of layer conv2d is incompatible with the layer:
expected ndim=4, found ndim=1. Full shape received: [2]
```

Input checks that can be specified via `input_spec` include:

* Structure (e.g. a single input, a list of 2 inputs, etc)
* Shape
* Rank (ndim)
* Dtype

For more information, see [`tf.keras.layers.InputSpec`](https://tensorflow.google.cn/api_docs/python/tf/keras/InputSpec).| `losses` | List of losses added using the `add_loss()` API. |

Variable regularization tensors are created when this property is accessed,
so it is eager safe: accessing `losses` under a [`tf.GradientTape`](https://tensorflow.google.cn/api_docs/python/tf/GradientTape) will
propagate gradients back to the corresponding variables.

```
>>> class MyLayer(tf.keras.layers.Layer):
...   def call(self, inputs):
...     self.add_loss(tf.abs(tf.reduce_mean(inputs)))
...     return inputs
>>> l = MyLayer()
>>> l(np.ones((10, 1)))
>>> l.losses
[1.0]
```

```
>>> inputs = tf.keras.Input(shape=(10,))
>>> x = tf.keras.layers.Dense(10)(inputs)
>>> outputs = tf.keras.layers.Dense(1)(x)
>>> model = tf.keras.Model(inputs, outputs)
>>> # Activity regularization.
>>> len(model.losses)
0
>>> model.add_loss(tf.abs(tf.reduce_mean(x)))
>>> len(model.losses)
1
```

```
>>> inputs = tf.keras.Input(shape=(10,))
>>> d = tf.keras.layers.Dense(10, kernel_initializer='ones')
>>> x = d(inputs)
>>> outputs = tf.keras.layers.Dense(1)(x)
>>> model = tf.keras.Model(inputs, outputs)
>>> # Weight regularization.
>>> model.add_loss(lambda: tf.reduce_mean(d.kernel))
>>> model.losses
[<tf.Tensor: shape=(), dtype=float32, numpy=1.0>]
```

|  |  |
| --- | --- |
| `metrics` | List of metrics added using the `add_metric()` API. |

```
>>> input = tf.keras.layers.Input(shape=(3,))
>>> d = tf.keras.layers.Dense(2)
>>> output = d(input)
>>> d.add_metric(tf.reduce_max(output), name='max')
>>> d.add_metric(tf.reduce_min(output), name='min')
>>> [m.name for m in d.metrics]
['max', 'min']
```

|  |  |
| --- | --- |
| `non_trainable_weights` | List of all non-trainable weights tracked by this layer. |

Non-trainable weights are *not* updated during training. They are expected
to be updated manually in `call()`.| `output` | Retrieves the output tensor(s) of a layer. |

Only applicable if the layer has exactly one output,
i.e. if it is connected to one incoming layer.|  |  |
| --- | --- |
| `output_size` |  |

|  |  |
| --- | --- |
| `state_size` |  |

|  |  |
| --- | --- |
| `supports_masking` | Whether this layer supports computing a mask using `compute_mask`. |
| `trainable` |  |

|  |  |
| --- | --- |
| `trainable_weights` | List of all trainable weights tracked by this layer. |

Trainable weights are updated via gradient descent during training.|  |  |
| --- | --- |
| `variable_dtype` | Alias of [`Layer.dtype`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer#dtype), the dtype of the weights. |
| `weights` | Returns the list of all layer variables/weights. |

## Methods

### `add_loss`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L1411-L1531)

```
add_loss(
    losses, **kwargs
)
```

Add loss tensor(s), potentially dependent on layer inputs.

Some losses (for instance, activity regularization losses) may be dependent
on the inputs passed when calling a layer. Hence, when reusing the same
layer on different inputs `a` and `b`, some entries in `layer.losses` may
be dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

This method can be used inside a subclassed layer or model's `call`
function, in which case `losses` should be a Tensor or list of Tensors.

#### Example:

```
class MyLayer(tf.keras.layers.Layer):
  def call(self, inputs):
    self.add_loss(tf.abs(tf.reduce_mean(inputs)))
    return inputs
```

This method can also be called directly on a Functional Model during
construction. In this case, any loss Tensors passed to this Model must
be symbolic and be able to be traced back to the model's `Input`s. These
losses become part of the model's topology and are tracked in `get_config`.

#### Example:

```
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(10)(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
# Activity regularization.
model.add_loss(tf.abs(tf.reduce_mean(x)))
```

If this is not the case for your loss (if, for example, your loss references
a `Variable` of one of the model's layers), you can wrap your loss in a
zero-argument lambda. These losses are not tracked as part of the model's
topology since they can't be serialized.

#### Example:

```
inputs = tf.keras.Input(shape=(10,))
d = tf.keras.layers.Dense(10)
x = d(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
# Weight regularization.
model.add_loss(lambda: tf.reduce_mean(d.kernel))
```

| Args | |

|  |  |
| --- | --- |
| `losses` | Loss tensor, or list/tuple of tensors. Rather than tensors, losses may also be zero-argument callables which create a loss tensor. |
| `**kwargs` | Additional keyword arguments for backward compatibility. Accepted values: inputs - Deprecated, will be automatically inferred. |

### `add_metric`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L1566-L1685)

```
add_metric(
    value, name=None, **kwargs
)
```

Adds metric tensor to the layer.

This method can be used inside the `call()` method of a subclassed layer
or model.

```
class MyMetricLayer(tf.keras.layers.Layer):
  def __init__(self):
    super(MyMetricLayer, self).__init__(name='my_metric_layer')
    self.mean = tf.keras.metrics.Mean(name='metric_1')

  def call(self, inputs):
    self.add_metric(self.mean(inputs))
    self.add_metric(tf.reduce_sum(inputs), name='metric_2')
    return inputs
```

This method can also be called directly on a Functional Model during
construction. In this case, any tensor passed to this Model must
be symbolic and be able to be traced back to the model's `Input`s. These
metrics become part of the model's topology and are tracked when you
save the model via `save()`.

```
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(10)(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
model.add_metric(math_ops.reduce_sum(x), name='metric_1')
```

**Note:** Calling `add_metric()` with the result of a metric object on a
Functional Model, as shown in the example below, is not supported. This is
because we cannot trace the metric result tensor back to the model's inputs.

```
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(10)(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
model.add_metric(tf.keras.metrics.Mean()(x), name='metric_1')
```

| Args | |

|  |  |
| --- | --- |
| `value` | Metric tensor. |
| `name` | String metric name. |
| `**kwargs` | Additional keyword arguments for backward compatibility. Accepted values: `aggregation` - When the `value` tensor provided is not the result of calling a [`keras.Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric) instance, it will be aggregated by default using a `keras.Metric.Mean`. |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L71-L74)

```
build(
    inputs_shape
)
```

Builds the wrapped cell.

### `compute_mask`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L909-L929)

```
compute_mask(
    inputs, mask=None
)
```

Computes an output mask tensor.

| Args | |

|  |  |
| --- | --- |
| `inputs` | Tensor or list of tensors. |
| `mask` | Tensor or list of tensors. |

| Returns | |
| None or a tensor (or list of tensors, one per output tensor of the layer). | |

### `compute_output_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L755-L798)

```
compute_output_shape(
    input_shape
)
```

Computes the output shape of the layer.

If the layer has not been built, this method will call `build` on the
layer. This assumes that the layer will later be used with inputs that
match the input shape provided here.

| Args | |

|  |  |
| --- | --- |
| `input_shape` | Shape tuple (tuple of integers) or list of shape tuples (one per output tensor of the layer). Shape tuples can include None for free dimensions, instead of an integer. |

| Returns | |
| An input shape tuple. | |

### `count_params`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L2130-L2149)

```
count_params()
```

Count the total number of scalars composing the weights.

| Returns | |
| An integer count. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the layer isn't yet built (in which case its weights aren't yet defined). |

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L395-L405)

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

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L380-L393)

```
get_config()
```

Returns the config of the residual wrapper.

### `get_initial_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/recurrent.py#L1089-L1090)

```
get_initial_state(
    inputs=None, batch_size=None, dtype=None
)
```

### `get_weights`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L1809-L1851)

```
get_weights()
```

Returns the current weights of the layer, as NumPy arrays.

The weights of a layer represent the state of the layer. This function
returns both trainable and non-trainable weight values associated with this
layer as a list of NumPy arrays, which can in turn be used to load state
into similarly parameterized layers.

For example, a `Dense` layer returns a list of two values: the kernel matrix
and the bias vector. These can be used to set the weights of another
`Dense` layer:

```
>>> layer_a = tf.keras.layers.Dense(1,
...   kernel_initializer=tf.constant_initializer(1.))
>>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]]))
>>> layer_a.get_weights()
[array([[1.],
       [1.],
       [1.]], dtype=float32), array([0.], dtype=float32)]
>>> layer_b = tf.keras.layers.Dense(1,
...   kernel_initializer=tf.constant_initializer(2.))
>>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]]))
>>> layer_b.get_weights()
[array([[2.],
       [2.],
       [2.]], dtype=float32), array([0.], dtype=float32)]
>>> layer_b.set_weights(layer_a.get_weights())
>>> layer_b.get_weights()
[array([[1.],
       [1.],
       [1.]], dtype=float32), array([0.], dtype=float32)]
```

| Returns | |
| Weights values as a list of NumPy arrays. | |

### `set_weights`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L1724-L1807)

```
set_weights(
    weights
)
```

Sets the weights of the layer, from NumPy arrays.

The weights of a layer represent the state of the layer. This function
sets the weight values from numpy arrays. The weight values should be
passed in the order they are created by the layer. Note that the layer's
weights must be instantiated before calling this function, by calling
the layer.

For example, a `Dense` layer returns a list of two values: the kernel matrix
and the bias vector. These can be used to set the weights of another
`Dense` layer:

```
>>> layer_a = tf.keras.layers.Dense(1,
...   kernel_initializer=tf.constant_initializer(1.))
>>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]]))
>>> layer_a.get_weights()
[array([[1.],
       [1.],
       [1.]], dtype=float32), array([0.], dtype=float32)]
>>> layer_b = tf.keras.layers.Dense(1,
...   kernel_initializer=tf.constant_initializer(2.))
>>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]]))
>>> layer_b.get_weights()
[array([[2.],
       [2.],
       [2.]], dtype=float32), array([0.], dtype=float32)]
>>> layer_b.set_weights(layer_a.get_weights())
>>> layer_b.get_weights()
[array([[1.],
       [1.],
       [1.]], dtype=float32), array([0.], dtype=float32)]
```

| Args | |

|  |  |
| --- | --- |
| `weights` | a list of NumPy arrays. The number of arrays and their shape must match number of the dimensions of the weights of the layer (i.e. it should match the output of `get_weights`). |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the provided weights list does not match the layer's specifications. |

### `zero_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L345-L347)

```
zero_state(
    batch_size, dtype
)
```

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/keras/engine/base_layer.py#L931-L1052)

```
__call__(
    *args, **kwargs
)
```

Wraps `call`, applying pre- and post-processing steps.

| Args | |

|  |  |
| --- | --- |
| `*args` | Positional arguments to be passed to `self.call`. |
| `**kwargs` | Keyword arguments to be passed to `self.call`. |

| Returns | |
| Output tensor(s). | |

| Note | |
|  | |

* The following optional keyword arguments are reserved for specific uses:
  + `training`: Boolean scalar tensor of Python boolean indicating
    whether the `call` is meant for training or inference.
  + `mask`: Boolean input mask.
* If the layer's `call` method takes a `mask` argument (as some Keras
  layers do), its default value will be set to the mask generated
  for `inputs` by the previous layer (if `input` did come from
  a layer that generated a corresponding mask, i.e. if it came from
  a Keras layer with masking support.
* If the layer is not built, the method will call `build`.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the layer's `call` method returns None (an invalid value). |
| `RuntimeError` | if `super().__init__()` was not called in the constructor. |