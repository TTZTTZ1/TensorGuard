# tf.train.ExponentialMovingAverage

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/ExponentialMovingAverage](https://tensorflow.google.cn/api_docs/python/tf/train/ExponentialMovingAverage)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/moving_averages.py#L283-L689) |

Maintains moving averages of variables by employing an exponential decay.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.ExponentialMovingAverage`](https://tensorflow.google.cn/api_docs/python/tf/train/ExponentialMovingAverage)

```
tf.train.ExponentialMovingAverage(
    decay,
    num_updates=None,
    zero_debias=False,
    name='ExponentialMovingAverage'
)
```

When training a model, it is often beneficial to maintain moving averages of
the trained parameters. Evaluations that use averaged parameters sometimes
produce significantly better results than the final trained values.

The `apply()` method adds shadow copies of trained variables the first time
it is called, and maintains a moving average of the trained variables in
their shadow copies at every additional invocation.
It should generally be called immediately after creating the model weights,
and then after each training step.

The `average()` method gives access to the shadow variables.
It allows you to use the moving averages in place of the last trained values
for evaluations, by loading the moving averages into your model via
`var.assign(ema.average(var))`.
Additionally, although `ExponentialMovingAverage`
objects are not directly trackable by checkpoints,
`average()` returns the moving average variables for your model weights,
which you can then checkpoint. (There is an example
of this near the bottom of this docstring).
So, `average()` is useful when
building an evaluation model, or when restoring a model from a checkpoint
file.

The moving averages are computed using exponential decay. You specify the
decay value (as a scalar float value, `Tensor`, or `Variable`) when creating
the `ExponentialMovingAverage` object. The shadow variables are initialized
with the same initial values as the trained variables. When you run `apply`
to update the moving averages, each shadow variable is updated with the
formula:

`shadow_variable -= (1 - decay) * (shadow_variable - variable)`

This is mathematically equivalent to the classic formula below, but the use
of an `assign_sub` op (the `"-="` in the formula) allows concurrent lockless
updates to the variables:

`shadow_variable = decay * shadow_variable + (1 - decay) * variable`

Reasonable values for `decay` are close to 1.0, typically in the
multiple-nines range: 0.999, 0.9999, etc.

To have fine-grained control over the value of the decay parameter during
training, pass a scalar [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable) as the `decay` value to the constructor,
and update the variable as needed.

Example usage when creating a training model:

```
# Create variables.
var0 = tf.Variable(...)
var1 = tf.Variable(...)
# ... use the variables to build a training model...

# Create an ExponentialMovingAverage object
ema = tf.train.ExponentialMovingAverage(decay=0.9999)

# The first `apply` creates the shadow variables that hold the moving averages
ema.apply([var0, var1])

# grab the moving averages for checkpointing purposes or to be able to
# load the moving averages into the model weights
averages = [ema.average(var0), ema.average(var1)]

...
def train_step(...):
...
  # Apply the optimizer.
  opt.minimize(my_loss, [var0, var1])

  # Update the moving averages
  # of var0 and var1 with additional calls to `apply`
  ema.apply([var0, var1])

...train the model by running train_step multiple times...
```

There are several ways to use the moving averages for evaluations:

1. Assign the values of the shadow variables to your model variables with
   [`Variable.assign(...)`](https://tensorflow.google.cn/api_docs/python/tf/Variable#assign) before evaluating your
   model. You can use the `average()`
   method to get the shadow variable for a given variable. To continue
   training after using this approach, make sure to record the unaveraged
   weights and restore them before continuing to train. You can see the
   tensorflow-addons' MovingAverage optimizer's `swap_weights` method for
   one example of how to swap variables efficiently in distributed settings:
   https://github.com/tensorflow/addons/blob/v0.13.0/tensorflow\_addons/optimizers/moving\_average.py#L151
2. Make sure to checkpoint out your moving average variables in your
   [`tf.train.Checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint). At evaluation time, create your shadow variables and
   use [`tf.train.Checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint) to restore the moving averages into the shadow
   variables. Then, load the moving averages into the actual model weights via
   `var.assign(moving_avg)`.
3. Checkpoint out your moving average variables in your [`tf.train.Checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint).
   For evaluation, restore your model weights directly from the moving
   averages instead of from the non-averaged weights.
   Caution: If you choose this approach, include only the object-graph paths
   to the averaged path in your checkpoint restore.
   If you point both the unaveraged and averaged paths in a checkpoint
   restore to the same variables, it is hard to reason about whether your
   model will restore the averaged or non-averaged variables.

Example of saving out then restoring the shadow variable values:

```
# Create variables.
var0 = tf.Variable(...)
var1 = tf.Variable(...)
# ... use the variables to build a training model...

# Create an ExponentialMovingAverage object, create the shadow variables,
# and grab the moving averages for checkpointing purposes.
# (The ExponentialMovingAverage object itself is not checkpointable)
ema = tf.train.ExponentialMovingAverage(decay=0.9999)
ema.apply([var0, var1])
avg_var0 = ema.average(var0)
avg_var1 = ema.average(var1)

# Create a Checkpoint that will manage the model weights and the averages,
checkpoint = tf.train.Checkpoint(model_weights=[var0, var1],
                                 averaged_weights=[avg_var0, avg_var1])
... # Do training

# Save out the checkpoint including the model weights and the moving averages
checkpoint.save(...)
```

Restore option: restore all averaged & non-averaged weights, then load
moving averages into the model via `var.assign()`

```
# Create variables.
var0 = tf.Variable(...)
var1 = tf.Variable(...)
# ... use the variables to build a training model...

# Create an ExponentialMovingAverage object, create the shadow variables,
# and grab the moving averages for checkpoint restore purposes.
# (The ExponentialMovingAverage object itself is not checkpointable)
ema = tf.train.ExponentialMovingAverage(decay=0.9999)
ema.apply([var0, var1])
avg_var0 = ema.average(var0)
avg_var1 = ema.average(var1)

# Create a Checkpoint that will manage the model weights and the averages,
checkpoint = tf.train.Checkpoint(model_weights=[var0, var1],
                                 averaged_weights=[avg_var0, avg_var1])
checkpoint.restore(...)
var0.assign(avg_var0)
var1.assign(avg_var1)
# var0 and var1 now hold the moving average values
```

Restore option: Directly restore the moving averages into the model weights.

```
# Create variables.
var0 = tf.Variable(...)
var1 = tf.Variable(...)
# ... use the variables to build a training model...

# Create a Checkpoint that will manage two objects with trackable state,
checkpoint = tf.train.Checkpoint(averaged_weights=[var0, var1])
checkpoint.restore(...)
# var0 and var1 now hold the moving average values
```

| Args | |

|  |  |
| --- | --- |
| `decay` | A scalar float value, `Tensor`, or `Variable`. The decay parameter. |
| `num_updates` | Optional count of number of updates applied to variables. |
| `zero_debias` | If `True`, zero debias moving-averages that are initialized with tensors. (Note: moving averages may not be initialized with non-variable tensors when eager execution is enabled). |
| `name` | String. Optional prefix name to use for the name of ops added in `apply()`. |

| Attributes | |

|  |  |
| --- | --- |
| `name` | The name of this ExponentialMovingAverage object. |

## Methods

### `apply`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/moving_averages.py#L493-L592)

```
apply(
    var_list=None
)
```

Maintains moving averages of variables.

`var_list` must be a list of `Variable` objects. This method
creates shadow variables (holding the moving averages)
for all elements of `var_list`, and
updates the moving averages using the current `var_list` values. Shadow
variables for `Variable` objects are initialized to the variable's initial
value.

Shadow variables are created with `trainable=False`. To access them you
can use the EMA object's `average` method. Note that `EMA` objects are
not trackable by checkpoints, so if you want to checkpoint or restore the
moving variables you will need to manually grab the shadow
variables via `average()` and assign them as [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module) properties or
directly pass them to your [`tf.train.Checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint).

Note that `apply()` can be called multiple times. When eager execution is
enabled each call to apply will update the variables once, so this needs to
be called in a loop.

In legacy TF 1.x graphs, this method returns an op that updates all
shadow variables from the current value of their associated variables. In
TF 1.x graphs without automatically control dependencies this op needs to be
manually run.

| Args | |

|  |  |
| --- | --- |
| `var_list` | A list of Variable objects. The variables must be of types bfloat16, float16, float32, or float64. (In legacy TF 1.x graphs these may be tensors, but this is unsupported when eager execution is enabled.) |

| Returns | |
| An Operation that updates the moving averages. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If the arguments are not an allowed type. |

### `average`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/moving_averages.py#L594-L604)

```
average(
    var
)
```

Returns the `Variable` holding the average of `var`.

| Args | |

|  |  |
| --- | --- |
| `var` | A `Variable` object. |

| Returns | |
| A `Variable` object or `None` if the moving average of `var` is not maintained. | |