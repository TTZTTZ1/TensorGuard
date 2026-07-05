# tf.keras.optimizers.Optimizer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/Optimizer](https://tensorflow.google.cn/api_docs/python/tf/keras/optimizers/Optimizer)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/optimizer.py#L21-L23) |

A class for Tensorflow specific optimizer logic.

#### View aliases

**Main aliases**

[`tf.keras.optimizers.Optimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Optimizer)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Optimizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Optimizer)

```
tf.keras.Optimizer(
    *args, **kwargs
)
```

The major behavior change for this class is for tf.distribute.

It will override methods from base Keras core Optimizer,
which provide distribute specific functionality, e.g. variable
creation, loss reduction, etc.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L145-L168)

```
build(
    variables
)
```

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L821-L864)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/optimizers/base_optimizer.py#L277-L278)

```
update_step(
    gradient, variable, learning_rate
)
```