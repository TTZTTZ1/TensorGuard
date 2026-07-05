# tf.keras.layers.Layer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Layer](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Layer)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L59-L1448) |

This is the class from which all layers inherit.

Inherits From: [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer)

```
tf.keras.Layer(
    *,
    activity_regularizer=None,
    trainable=True,
    dtype=None,
    autocast=True,
    name=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Debug a TensorFlow 2 migrated training pipeline](https://tensorflow.google.cn/guide/migrate/migration_debugging) | * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [Custom layers](https://tensorflow.google.cn/tutorials/customization/custom_layers) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

A layer is a callable object that takes as input one or more tensors and
that outputs one or more tensors. It involves *computation*, defined
in the `call()` method, and a *state* (weight variables). State can be
created:

* in `__init__()`, for instance via `self.add_weight()`;
* in the optional `build()` method, which is invoked by the first
  `__call__()` to the layer, and supplies the shape(s) of the input(s),
  which may not have been known at initialization time.

Layers are recursively composable: If you assign a Layer instance as an
attribute of another Layer, the outer layer will start tracking the weights
created by the inner layer. Nested layers should be instantiated in the
`__init__()` method or `build()` method.

Users will just instantiate a layer and then treat it as a callable.

| Args | |

|  |  |
| --- | --- |
| `trainable` | Boolean, whether the layer's variables should be trainable. |
| `name` | String name of the layer. |
| `dtype` | The dtype of the layer's computations and weights. Can also be a [`keras.DTypePolicy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy), which allows the computation and weight dtype to differ. Defaults to `None`. `None` means to use [`keras.config.dtype_policy()`](https://tensorflow.google.cn/api_docs/python/tf/keras/config/dtype_policy), which is a `float32` policy unless set to different value (via [`keras.config.set_dtype_policy()`](https://tensorflow.google.cn/api_docs/python/tf/keras/config/set_dtype_policy)). |

We recommend that descendants of `Layer` implement the following methods:

* `__init__()`: Defines custom layer attributes, and creates layer weights
  that do not depend on input shapes, using `add_weight()`,
  or other state.
* `build(self, input_shape)`: This method can be used to create weights that
  depend on the shape(s) of the input(s), using `add_weight()`, or other
  state. `__call__()` will automatically build the layer
  (if it has not been built yet) by calling `build()`.
* `call(self, *args, **kwargs)`: Called in `__call__` after making
  sure `build()` has been called. `call()` performs the logic of applying
  the layer to the input arguments.
  Two reserved keyword arguments you can optionally use in `call()` are:
  1. `training` (boolean, whether the call is in inference mode or
  training mode).
  2. `mask` (boolean tensor encoding masked timesteps in the input,
  used e.g. in RNN layers).
  A typical signature for this method is `call(self, inputs)`, and user
  could optionally add `training` and `mask` if the layer need them.
* `get_config(self)`: Returns a dictionary containing the configuration
  used to initialize this layer. If the keys differ from the arguments
  in `__init__()`, then override `from_config(self)` as well.
  This method is used when saving
  the layer or a model that contains this layer.

#### Examples:

Here's a basic example: a layer with two variables, `w` and `b`,
that returns `y = w . x + b`.
It shows how to implement `build()` and `call()`.
Variables set as attributes of a layer are tracked as weights
of the layers (in `layer.weights`).

```
class SimpleDense(Layer):
    def __init__(self, units=32):
        super().__init__()
        self.units = units

    # Create the state of the layer (weights)
    def build(self, input_shape):
        self.kernel = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="glorot_uniform",
            trainable=True,
            name="kernel",
        )
        self.bias = self.add_weight(
            shape=(self.units,),
            initializer="zeros",
            trainable=True,
            name="bias",
        )

    # Defines the computation
    def call(self, inputs):
        return ops.matmul(inputs, self.kernel) + self.bias

# Instantiates the layer.
linear_layer = SimpleDense(4)

# This will also call `build(input_shape)` and create the weights.
y = linear_layer(ops.ones((2, 2)))
assert len(linear_layer.weights) == 2

# These weights are trainable, so they're listed in `trainable_weights`:
assert len(linear_layer.trainable_weights) == 2
```

Besides trainable weights, updated via backpropagation during training,
layers can also have non-trainable weights. These weights are meant to
be updated manually during `call()`. Here's a example layer that computes
the running sum of its inputs:

```
class ComputeSum(Layer):

  def __init__(self, input_dim):
      super(ComputeSum, self).__init__()
      # Create a non-trainable weight.
      self.total = self.add_weight(
        shape=(),
        initializer="zeros",
        trainable=False,
        name="total",
      )

  def call(self, inputs):
      self.total.assign(self.total + ops.sum(inputs))
      return self.total

my_sum = ComputeSum(2)
x = ops.ones((2, 2))
y = my_sum(x)

assert my_sum.weights == [my_sum.total]
assert my_sum.non_trainable_weights == [my_sum.total]
assert my_sum.trainable_weights == []
```

| Attributes | |

|  |  |
| --- | --- |
| `name` | The name of the layer (string). |
| `dtype` | Dtype of the layer's weights. Alias of `layer.variable_dtype`. |
| `variable_dtype` | Dtype of the layer's weights. |
| `compute_dtype` | The dtype of the layer's computations. Layers automatically cast inputs to this dtype, which causes the computations and output to also be in this dtype. When mixed precision is used with a [`keras.DTypePolicy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy), this will be different than `variable_dtype`. |
| `trainable_weights` | List of variables to be included in backprop. |
| `non_trainable_weights` | List of variables that should not be included in backprop. |
| `weights` | The concatenation of the lists trainable\_weights and non\_trainable\_weights (in this order). |
| `trainable` | Whether the layer should be trained (boolean), i.e. whether its potentially-trainable weights should be returned as part of `layer.trainable_weights`. |
| `input_spec` | Optional (list of) `InputSpec` object(s) specifying the constraints on inputs that can be accepted by the layer. |
| `dtype_policy` |  |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `input_dtype` | The dtype layer inputs should be converted to. |
| `losses` | List of scalar losses from `add_loss`, regularizers and sublayers. |
| `metrics` | List of all metrics. |
| `metrics_variables` | List of all metric variables. |
| `non_trainable_variables` | List of all non-trainable layer state. |

This extends `layer.non_trainable_weights` to include all state used by
the layer including state for metrics and `SeedGenerator`s.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `supports_masking` | Whether this layer supports computing a mask using `compute_mask`. |
| `trainable_variables` | List of all trainable layer state. |

This is equivalent to `layer.trainable_weights`.| `variables` | List of all layer state, including random seeds. |

This extends `layer.weights` to include all state used by the layer
including `SeedGenerator`s.

Note that metrics variables are not included here, use
`metrics_variables` to visit all the metric variables.

## Methods

### `add_loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1060-L1088)

```
add_loss(
    loss
)
```

Can be called inside of the `call()` method to add a scalar loss.

#### Example:

```
class MyLayer(Layer):
    ...
    def call(self, x):
        self.add_loss(ops.sum(x))
        return x
```

### `add_metric`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1244-L1246)

```
add_metric()
```

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L429-L453)

```
add_variable(
    shape,
    initializer,
    dtype=None,
    trainable=True,
    autocast=True,
    regularizer=None,
    constraint=None,
    name=None
)
```

Add a weight variable to the layer.

Alias of `add_weight()`.

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L455-L524)

```
add_weight(
    shape=None,
    initializer=None,
    dtype=None,
    trainable=True,
    autocast=True,
    regularizer=None,
    constraint=None,
    aggregation='mean',
    name=None
)
```

Add a weight variable to the layer.

| Args | |

|  |  |
| --- | --- |
| `shape` | Shape tuple for the variable. Must be fully-defined (no `None` entries). Defaults to `()` (scalar) if unspecified. |
| `initializer` | Initializer object to use to populate the initial variable value, or string name of a built-in initializer (e.g. `"random_normal"`). If unspecified, defaults to `"glorot_uniform"` for floating-point variables and to `"zeros"` for all other types (e.g. int, bool). |
| `dtype` | Dtype of the variable to create, e.g. `"float32"`. If unspecified, defaults to the layer's variable dtype (which itself defaults to `"float32"` if unspecified). |
| `trainable` | Boolean, whether the variable should be trainable via backprop or whether its updates are managed manually. Defaults to `True`. |
| `autocast` | Boolean, whether to autocast layers variables when accessing them. Defaults to `True`. |
| `regularizer` | Regularizer object to call to apply penalty on the weight. These penalties are summed into the loss function during optimization. Defaults to `None`. |
| `constraint` | Contrainst object to call on the variable after any optimizer update, or string name of a built-in constraint. Defaults to `None`. |
| `aggregation` | String, one of `'mean'`, `'sum'`, `'only_first_replica'`. Annotates the variable with the type of multi-replica aggregation to be used for this variable when writing custom data parallel training loops. |
| `name` | String name of the variable. Useful for debugging purposes. |

### `build`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L357-L369)

```
build(
    input_shape
)
```

### `build_from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L408-L424)

```
build_from_config(
    config
)
```

Builds the layer's states with the supplied config dict.

By default, this method calls the `build(config["input_shape"])` method,
which creates weights based on the layer's input shape in the supplied
config. If your config contains other information needed to load the
layer's state, you should override this method.

| Args | |

|  |  |
| --- | --- |
| `config` | Dict containing the input shape associated with this layer. |

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L889-L893)

```
call(
    *args, **kwargs
)
```

### `compute_mask`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L720-L722)

```
compute_mask(
    inputs, previous_mask
)
```

### `compute_output_shape`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1053-L1058)

```
compute_output_shape(
    *args, **kwargs
)
```

### `compute_output_spec`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1009-L1051)

```
compute_output_spec(
    *args, **kwargs
)
```

### `count_params`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1248-L1262)

```
count_params()
```

Count the total number of scalars composing the weights.

| Returns | |
| An integer count. | |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L191-L213)

```
@classmethod
from_config(
    config
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

### `get_build_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L384-L406)

```
get_build_config()
```

Returns a dictionary with the layer's input shape.

This method returns a config dict that can be used by
`build_from_config(config)` to create all states (e.g. Variables and
Lookup tables) needed by the layer.

By default, the config only contains the input shape that the layer
was built with. If you're writing a custom layer that creates state in
an unusual way, you should override this method to make sure this state
is already created when Keras attempts to load its value upon model
loading.

| Returns | |
| A dict containing the input shape associated with the layer. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1435-L1443)

```
get_config()
```

Returns the config of the object.

An object config is a Python dictionary (serializable)
containing the information needed to re-instantiate it.

### `get_weights`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L658-L660)

```
get_weights()
```

Return the values of `layer.weights` as a list of NumPy arrays.

### `load_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1183-L1225)

```
load_own_variables(
    store
)
```

Loads the state of the layer.

You can override this method to take full control of how the state of
the layer is loaded upon calling [`keras.models.load_model()`](https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model).

| Args | |

|  |  |
| --- | --- |
| `store` | Dict from which the state of the model will be loaded. |

### `quantize`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1137-L1141)

```
quantize(
    mode
)
```

### `quantized_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L895-L899)

```
quantized_call(
    *args, **kwargs
)
```

### `save_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L1170-L1181)

```
save_own_variables(
    store
)
```

Saves the state of the layer.

You can override this method to take full control of how the state of
the layer is saved upon calling `model.save()`.

| Args | |

|  |  |
| --- | --- |
| `store` | Dict where the state of the model will be saved. |

### `set_weights`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L662-L678)

```
set_weights(
    weights
)
```

Sets the values of `layer.weights` from a list of NumPy arrays.

### `stateless_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L901-L1007)

```
stateless_call(
    trainable_variables,
    non_trainable_variables,
    *args,
    return_losses=False,
    **kwargs
)
```

Call the layer without any side effects.

| Args | |

|  |  |
| --- | --- |
| `trainable_variables` | List of trainable variables of the model. |
| `non_trainable_variables` | List of non-trainable variables of the model. |
| `*args` | Positional arguments to be passed to `call()`. |
| `return_losses` | If `True`, `stateless_call()` will return the list of losses created during `call()` as part of its return values. |
| `**kwargs` | Keyword arguments to be passed to `call()`. |

| Returns | |
| A tuple. By default, returns `(outputs, non_trainable_variables)`. If `return_losses = True`, then returns `(outputs, non_trainable_variables, losses)`. | |

**Note:** `non_trainable_variables` include not only non-trainable weights
such as `BatchNormalization` statistics, but also RNG seed state
(if there are any random operations part of the layer, such as dropout),
and `Metric` state (if there are any metrics attached to the layer).
These are all elements of state of the layer.

#### Example:

```
model = ...
data = ...
trainable_variables = model.trainable_variables
non_trainable_variables = model.non_trainable_variables
# Call the model with zero side effects
outputs, non_trainable_variables = model.stateless_call(
    trainable_variables,
    non_trainable_variables,
    data,
)
# Attach the updated state to the model
# (until you do this, the model is still in its pre-call state).
for ref_var, value in zip(
    model.non_trainable_variables, non_trainable_variables
):
    ref_var.assign(value)
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/layer.py#L724-L887)

```
__call__(
    *args, **kwargs
)
```

Call self as a function.