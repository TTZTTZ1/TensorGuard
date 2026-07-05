# tf.keras.optimizers.Nadam

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/Nadam](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/Nadam)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/nadam.py#L7-L169) |

Optimizer that implements the Nadam algorithm.

Inherits From: [`Optimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Optimizer)

```
tf.keras.optimizers.Nadam(
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name='nadam',
    **kwargs
)
```

Much like Adam is essentially RMSprop with momentum, Nadam is Adam with
Nesterov momentum.

| Args | |

|  |  |
| --- | --- |
| `learning_rate` | A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule) instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`. |
| `beta_1` | A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 1st moment estimates. Defaults to `0.9`. |
| `beta_2` | A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 2nd moment estimates. Defaults to `0.999`. |
| `epsilon` | A small constant for numerical stability. This epsilon is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to `1e-7`. |
| `name` | String. The name to use for momentum accumulator weights created by the optimizer. |
| `weight_decay` | Float. If set, weight decay is applied. |
| `clipnorm` | Float. If set, the gradient of each weight is individually clipped so that its norm is no higher than this value. |
| `clipvalue` | Float. If set, the gradient of each weight is clipped to be no higher than this value. |
| `global_clipnorm` | Float. If set, the gradient of all weights is clipped so that their global norm is no higher than this value. |
| `use_ema` | Boolean, defaults to `False`. If `True`, exponential moving average (EMA) is applied. EMA consists of computing an exponential moving average of the weights of the model (as the weight values change after each training batch), and periodically overwriting the weights with their moving average. |
| `ema_momentum` | Float, defaults to 0.99. Only used if `use_ema=True`. This is the momentum to use when computing the EMA of the model's weights: `new_average = ema_momentum * old_average + (1 - ema_momentum) * current_variable_value`. |
| `ema_overwrite_frequency` | Int or None, defaults to None. Only used if `use_ema=True`. Every `ema_overwrite_frequency` steps of iterations, we overwrite the model variable by its moving average. If None, the optimizer does not overwrite model variables in the middle of training, and you need to explicitly overwrite the variables at the end of training by calling `optimizer.finalize_variable_values()` (which updates the model variables in-place). When using the built-in `fit()` training loop, this happens automatically after the last epoch, and you don't need to do anything. |
| `loss_scale_factor` | Float or `None`. If a float, the scale factor will be multiplied the loss before computing gradients, and the inverse of the scale factor will be multiplied by the gradients before updating variables. Useful for preventing underflow during mixed precision training. Alternately, [`keras.optimizers.LossScaleOptimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer) will automatically set a loss scale factor. |
| `gradient_accumulation_steps` | Int or `None`. If an int, model & optimizer variables will not be updated at every step; instead they will be updated every `gradient_accumulation_steps` steps, using the average value of the gradients since the last update. This is known as "gradient accumulation". This can be useful when your batch size is very small, in order to reduce gradient noise at each update step. |

#### Reference:

* [Dozat, 2015](http://cs229.stanford.edu/proj2015/054_report.pdf).

| Attributes | |

|  |  |
| --- | --- |
| `learning_rate` |  |

|  |  |
| --- | --- |
| `variables` |  |

## Methods

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L181-L201)

```
add_variable(
    shape,
    initializer='zeros',
    dtype=None,
    aggregation='mean',
    name=None
)
```

### `add_variable_from_reference`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/optimizer.py#L25-L38)

```
add_variable_from_reference(
    reference_variable, name=None, initializer='zeros'
)
```

Add an all-zeros variable with the shape and dtype of a reference variable.

### `apply`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L286-L355)

```
apply(
    grads, trainable_variables=None
)
```

Update traininable variables according to provided gradient values.

`grads` should be a list of gradient tensors
with 1:1 mapping to the list of variables the optimizer was built with.

`trainable_variables` can be provided
on the first call to build the optimizer.

### `apply_gradients`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L280-L284)

```
apply_gradients(
    grads_and_vars
)
```

### `assign`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/optimizer.py#L48-L55)

```
assign(
    variable, value
)
```

Assign a value to a variable.

This should be used in optimizers instead of `variable.assign(value)` to
support backend specific optimizations.
Note that the variable can be a model variable or an optimizer variable;
it can be a backend native variable or a Keras variable.

| Args | |

|  |  |
| --- | --- |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `assign_add`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/optimizer.py#L57-L64)

```
assign_add(
    variable, value
)
```

Add a value to a variable.

This should be used in optimizers instead of
`variable.assign_add(value)` to support backend specific optimizations.
Note that the variable can be a model variable or an optimizer variable;
it can be a backend native variable or a Keras variable.

| Args | |

|  |  |
| --- | --- |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `assign_sub`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/optimizer.py#L66-L73)

```
assign_sub(
    variable, value
)
```

Subtract a value from a variable.

This should be used in optimizers instead of
`variable.assign_sub(value)` to support backend specific optimizations.
Note that the variable can be a model variable or an optimizer variable;
it can be a backend native variable or a Keras variable.

| Args | |

|  |  |
| --- | --- |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `build`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/nadam.py#L75-L104)

```
build(
    var_list
)
```

Initialize optimizer variables.

Nadam optimizer has 2 types of variables: momentums and velocities.

| Args | |

|  |  |
| --- | --- |
| `var_list` | list of model variables to build Nadam variables on. |

### `exclude_from_weight_decay`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L685-L723)

```
exclude_from_weight_decay(
    var_list=None, var_names=None
)
```

Exclude variables from weight decay.

This method must be called before the optimizer's `build` method is
called. You can set specific variables to exclude out, or set a list of
strings as the anchor words, if any of which appear in a variable's
name, then the variable is excluded.

| Args | |

|  |  |
| --- | --- |
| `var_list` | A list of `Variable`s to exclude from weight decay. |
| `var_names` | A list of strings. If any string in `var_names` appear in the model variable's name, then this model variable is excluded from weight decay. For example, `var_names=['bias']` excludes all bias variables from weight decay. |

### `finalize_variable_values`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L803-L816)

```
finalize_variable_values(
    var_list
)
```

Set the final value of model's trainable variables.

Sometimes there are some extra steps before ending the variable updates,
such as overriding the model variables with its average value.

| Args | |

|  |  |
| --- | --- |
| `var_list` | list of model variables. |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L866-L888)

```
@classmethod
from_config(
    config, custom_objects=None
)
```

Creates an optimizer from its config.

This method is the reverse of `get_config`, capable of instantiating the
same optimizer from the config dictionary.

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |
| `custom_objects` | A Python dictionary mapping names to additional user-defined Python objects needed to recreate this optimizer. |

| Returns | |
| An optimizer instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/nadam.py#L159-L169)

```
get_config()
```

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

Subclass optimizer should override this method to include other
hyperparameters.

| Returns | |
| Python dictionary. | |

### `load_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L567-L583)

```
load_own_variables(
    store
)
```

Set the state of this optimizer object.

### `save_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L562-L565)

```
save_own_variables(
    store
)
```

Get the state of this optimizer object.

### `scale_loss`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L499-L508)

```
scale_loss(
    loss
)
```

Scale the loss before computing gradients.

Scales the loss before gradients are computed in a `train_step`. This
is primarily useful during mixed precision training to prevent numeric
underflow.

### `set_weights`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L544-L560)

```
set_weights(
    weights
)
```

Set the weights of the optimizer.

### `stateless_apply`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/tensorflow/optimizer.py#L40-L46)

```
stateless_apply(
    optimizer_variables, grads, trainable_variables
)
```

### `update_step`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/nadam.py#L119-L157)

```
update_step(
    gradient, variable, learning_rate
)
```

Update step given gradient and the associated model variable.