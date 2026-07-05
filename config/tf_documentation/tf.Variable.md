# tf.Variable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/Variable](https://tensorflow.google.cn/api_docs/python/tf/Variable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L203-L1325) |

See the [variable guide](https://tensorflow.org/guide/variable).

```
tf.Variable(
    initial_value=None,
    trainable=None,
    validate_shape=True,
    caching_device=None,
    name=None,
    variable_def=None,
    dtype=None,
    import_scope=None,
    constraint=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE,
    shape=None,
    experimental_enable_variable_lifting=True
)

tf.VariableSynchronization.AUTO
tf.compat.v1.VariableAggregation.NONE
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating model checkpoints](https://tensorflow.google.cn/guide/migrate/migrating_checkpoints) * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) * [Introduction to Variables](https://tensorflow.google.cn/guide/variable) * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Learnable Distributions Zoo](https://tensorflow.google.cn/probability/examples/Learnable_Distributions_Zoo) |

A variable maintains shared, persistent state manipulated by a program.

The `Variable()` constructor requires an initial value for the variable, which
can be a `Tensor` of any type and shape. This initial value defines the type
and shape of the variable. After construction, the type and shape of the
variable are fixed. The value can be changed using one of the assign methods.

```
>>> v = tf.Variable(1.)
>>> v.assign(2.)
<tf.Variable ... shape=() dtype=float32, numpy=2.0>
>>> v.assign_add(0.5)
<tf.Variable ... shape=() dtype=float32, numpy=2.5>
```

The `shape` argument to `Variable`'s constructor allows you to construct a
variable with a less defined shape than its `initial_value`:

```
>>> v = tf.Variable(1., shape=tf.TensorShape(None))
>>> v.assign([[1.]])
<tf.Variable ... shape=<unknown> dtype=float32, numpy=array([[1.]], ...)>
```

Just like any `Tensor`, variables created with `Variable()` can be used as
inputs to operations. Additionally, all the operators overloaded for the
`Tensor` class are carried over to variables.

```
>>> w = tf.Variable([[1.], [2.]])
>>> x = tf.constant([[3., 4.]])
>>> tf.matmul(w, x)
<tf.Tensor:... shape=(2, 2), ... numpy=
  array([[3., 4.],
         [6., 8.]], dtype=float32)>
>>> tf.sigmoid(w + x)
<tf.Tensor:... shape=(2, 2), ...>
```

When building a machine learning model it is often convenient to distinguish
between variables holding trainable model parameters and other variables such
as a `step` variable used to count training steps. To make this easier, the
variable constructor supports a `trainable=<bool>`
parameter. [`tf.GradientTape`](https://tensorflow.google.cn/api_docs/python/tf/GradientTape) watches trainable variables by default:

```
>>> with tf.GradientTape(persistent=True) as tape:
...   trainable = tf.Variable(1.)
...   non_trainable = tf.Variable(2., trainable=False)
...   x1 = trainable * 2.
...   x2 = non_trainable * 3.
>>> tape.gradient(x1, trainable)
<tf.Tensor:... shape=(), dtype=float32, numpy=2.0>
>>> assert tape.gradient(x2, non_trainable) is None  # Unwatched
```

Variables are automatically tracked when assigned to attributes of types
inheriting from [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module).

```
>>> m = tf.Module()
>>> m.v = tf.Variable([1.])
>>> m.trainable_variables
(<tf.Variable ... shape=(1,) ... numpy=array([1.], dtype=float32)>,)
```

This tracking then allows saving variable values to
[training checkpoints](https://tensorflow.google.cn/guide/checkpoint), or to
[SavedModels](https://tensorflow.google.cn/guide/saved_model) which include
serialized TensorFlow graphs.

Variables are often captured and manipulated by [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s. This works the
same way the un-decorated function would have:

```
>>> v = tf.Variable(0.)
>>> read_and_decrement = tf.function(lambda: v.assign_sub(0.1))
>>> read_and_decrement()
<tf.Tensor: shape=(), dtype=float32, numpy=-0.1>
>>> read_and_decrement()
<tf.Tensor: shape=(), dtype=float32, numpy=-0.2>
```

Variables created inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) must be owned outside the function
and be created only once:

```
>>> class M(tf.Module):
...   @tf.function
...   def __call__(self, x):
...     if not hasattr(self, "v"):  # Or set self.v to None in __init__
...       self.v = tf.Variable(x)
...     return self.v * x
>>> m = M()
>>> m(2.)
<tf.Tensor: shape=(), dtype=float32, numpy=4.0>
>>> m(3.)
<tf.Tensor: shape=(), dtype=float32, numpy=6.0>
>>> m.v
<tf.Variable ... shape=() dtype=float32, numpy=2.0>
```

See the [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) documentation for details.

| Args | |

|  |  |
| --- | --- |
| `initial_value` | A `Tensor`, or Python object convertible to a `Tensor`, which is the initial value for the Variable. The initial value must have a shape specified unless `validate_shape` is set to False. Can also be a callable with no argument that returns the initial value when called. In that case, `dtype` must be specified. (Note that initializer functions from init\_ops.py must first be bound to a shape before being used here.) |
| `trainable` | If `True`, GradientTapes automatically watch uses of this variable. Defaults to `True`, unless `synchronization` is set to `ON_READ`, in which case it defaults to `False`. |
| `validate_shape` | If `False`, allows the variable to be initialized with a value of unknown shape. If `True`, the default, the shape of `initial_value` must be known. |
| `caching_device` | Note: This argument is only valid when using a v1-style `Session`. Optional device string describing where the Variable should be cached for reading. Defaults to the Variable's device. If not `None`, caches on another device. Typical use is to cache on the device where the Ops using the Variable reside, to deduplicate copying through `Switch` and other conditional statements. |
| `name` | Optional name for the variable. Defaults to `'Variable'` and gets uniquified automatically. |
| `variable_def` | `VariableDef` protocol buffer. If not `None`, recreates the Variable object with its contents, referencing the variable's nodes in the graph, which must already exist. The graph is not changed. `variable_def` and the other arguments are mutually exclusive. |
| `dtype` | If set, initial\_value will be converted to the given type. If `None`, either the datatype will be kept (if `initial_value` is a Tensor), or `convert_to_tensor` will decide. |
| `import_scope` | Optional `string`. Name scope to add to the `Variable.` Only used when initializing from protocol buffer. |
| `constraint` | An optional projection function to be applied to the variable after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected Tensor representing the value of the variable and return the Tensor for the projected value (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `synchronization` | Indicates when a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableSynchronization`](https://tensorflow.google.cn/api_docs/python/tf/VariableSynchronization). By default the synchronization is set to `AUTO` and the current `DistributionStrategy` chooses when to synchronize. |
| `aggregation` | Indicates how a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableAggregation`](https://tensorflow.google.cn/api_docs/python/tf/VariableAggregation). |
| `shape` | (optional) The shape of this variable. If None, the shape of `initial_value` will be used. When setting this argument to [`tf.TensorShape(None)`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) (representing an unspecified shape), the variable can be assigned with values of different shapes. |
| `experimental_enable_variable_lifting` | Whether to lift the variable out if it's in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function). Default is `True`. When this argument is `True`, variable creation will follow the behavior and restrictions described [here](https://tensorflow.google.cn/guide/function#creating_tfvariables). If this argument is `False`, that description doesn't apply, and you can freely create and use the variable in the [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), as if it's a "mutable [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)". You can't return the variable though. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If both `variable_def` and initial\_value are specified. |
| `ValueError` | If the initial value is not specified, or does not have a shape and `validate_shape` is `True`. |

| Attributes | |

|  |  |
| --- | --- |
| `aggregation` |  |

|  |  |
| --- | --- |
| `constraint` | Returns the constraint function associated with this variable. |
| `device` | The device of this variable. |
| `dtype` | The `DType` of this variable. |
| `graph` | The `Graph` of this variable. |
| `initial_value` | Returns the Tensor used as the initial value for the variable. |

Note that this is different from `initialized_value()` which runs
the op that initializes the variable before returning its value.
This method returns the tensor that is used by the op that initializes
the variable.| `initializer` | The initializer operation for this variable. |
| `name` | The name of this variable. |
| `op` | The `Operation` of this variable. |
| `shape` | The `TensorShape` of this variable. |
| `synchronization` |  |

|  |  |
| --- | --- |
| `trainable` |  |

## Child Classes

[`class SaveSliceInfo`](https://tensorflow.google.cn/api_docs/python/tf/Variable/SaveSliceInfo)

## Methods

### `assign`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L519-L535)

```
assign(
    value, use_locking=False, name=None, read_value=True
)
```

Assigns a new value to the variable.

This is essentially a shortcut for `assign(self, value)`.

| Args | |

|  |  |
| --- | --- |
| `value` | A `Tensor`. The new value for this variable. |
| `use_locking` | If `True`, use locking during the assignment. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

| Returns | |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. | |

### `assign_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L537-L553)

```
assign_add(
    delta, use_locking=False, name=None, read_value=True
)
```

Adds a value to this variable.

This is essentially a shortcut for `assign_add(self, delta)`.

| Args | |

|  |  |
| --- | --- |
| `delta` | A `Tensor`. The value to add to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

| Returns | |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. | |

### `assign_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L555-L571)

```
assign_sub(
    delta, use_locking=False, name=None, read_value=True
)
```

Subtracts a value from this variable.

This is essentially a shortcut for `assign_sub(self, delta)`.

| Args | |

|  |  |
| --- | --- |
| `delta` | A `Tensor`. The value to subtract from this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | The name of the operation to be created |
| `read_value` | if True, will return something which evaluates to the new value of the variable; if False will return the assign op. |

| Returns | |
| The updated variable. If `read_value` is false, instead returns None in Eager mode and the assign op in graph mode. | |

### `batch_scatter_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L687-L731)

```
batch_scatter_update(
    sparse_delta, use_locking=False, name=None
)
```

Assigns [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to this variable batch-wise.

Analogous to `batch_gather`. This assumes that this variable and the
sparse\_delta IndexedSlices have a series of leading dimensions that are the
same for all of them, and the updates are performed on the last dimension of
indices. In other words, the dimensions should be the following:

`num_prefix_dims = sparse_delta.indices.ndims - 1`
`batch_dim = num_prefix_dims + 1`
`sparse_delta.updates.shape = sparse_delta.indices.shape + var.shape[
batch_dim:]`

where

`sparse_delta.updates.shape[:num_prefix_dims]`
`== sparse_delta.indices.shape[:num_prefix_dims]`
`== var.shape[:num_prefix_dims]`

And the operation performed can be expressed as:

`var[i_1, ..., i_n,
sparse_delta.indices[i_1, ..., i_n, j]] = sparse_delta.updates[
i_1, ..., i_n, j]`

When sparse\_delta.indices is a 1D tensor, this operation is equivalent to
`scatter_update`.

To avoid this operation one can looping over the first `ndims` of the
variable and using `scatter_update` on the subtensors that result of slicing
the first dimension. This is a valid option for `ndims = 1`, but less
efficient than this implementation.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to be assigned to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `count_up_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L902-L923)

```
count_up_to(
    limit
)
```

Increments this variable until it reaches `limit`. (deprecated)

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Prefer Dataset.range instead.

When that Op is run it tries to increment the variable by `1`. If
incrementing the variable would bring it above `limit` then the Op raises
the exception `OutOfRangeError`.

If no error is raised, the Op outputs the value of the variable before
the increment.

This is essentially a shortcut for `count_up_to(self, limit)`.

| Args | |

|  |  |
| --- | --- |
| `limit` | value at which incrementing the variable raises an error. |

| Returns | |
| A `Tensor` that will hold the variable value before the increment. If no other Op modifies this variable, the values produced will all be distinct. | |

### `eval`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L439-L469)

```
eval(
    session=None
)
```

In a session, computes and returns the value of this variable.

This is not a graph construction method, it does not add ops to the graph.

This convenience method requires a session where the graph
containing this variable has been launched. If no session is
passed, the default session is used. See [`tf.compat.v1.Session`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/Session) for more
information on launching a graph and on sessions.

```
v = tf.Variable([1, 2])
init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    # Usage passing the session explicitly.
    print(v.eval(sess))
    # Usage with the default session.  The 'with' block
    # above makes 'sess' the default session.
    print(v.eval())
```

| Args | |

|  |  |
| --- | --- |
| `session` | The session to use to evaluate this variable. If none, the default session is used. |

| Returns | |
| A numpy `ndarray` with a copy of the value of this variable. | |

### `experimental_ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1156-L1158)

```
experimental_ref()
```

DEPRECATED FUNCTION

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use ref() instead.

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1140-L1143)

```
@staticmethod
from_proto(
    variable_def, import_scope=None
)
```

Returns a `Variable` object created from `variable_def`.

### `gather_nd`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L887-L900)

```
gather_nd(
    indices, name=None
)
```

Gather slices from `params` into a Tensor with shape specified by `indices`.

See tf.gather\_nd for details.

| Args | |

|  |  |
| --- | --- |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `params`. | |

### `get_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1120-L1122)

```
get_shape() -> tf.TensorShape

tf.TensorShape
```

Alias of [`Variable.shape`](https://tensorflow.google.cn/api_docs/python/tf/Variable#shape).

### `initialized_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L471-L493)

```
initialized_value()
```

Returns the value of the initialized variable. (deprecated)

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use Variable.read\_value. Variables in 2.X are initialized automatically both in eager and graph (inside tf.defun) contexts.

You should use this instead of the variable itself to initialize another
variable with a value that depends on the value of this variable.

```
# Initialize 'v' with a random tensor.
v = tf.Variable(tf.random.truncated_normal([10, 40]))
# Use `initialized_value` to guarantee that `v` has been
# initialized before its value is used to initialize `w`.
# The random values are picked only once.
w = tf.Variable(v.initialized_value() * 2.0)
```

| Returns | |
| A `Tensor` holding the value of this variable after its initializer has run. | |

### `load`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L925-L968)

```
load(
    value, session=None
)
```

Load new value into this variable. (deprecated)

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Prefer Variable.assign which has equivalent behavior in 2.X.

Writes new value to variable's memory. Doesn't add ops to the graph.

This convenience method requires a session where the graph
containing this variable has been launched. If no session is
passed, the default session is used. See [`tf.compat.v1.Session`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/Session) for more
information on launching a graph and on sessions.

```
v = tf.Variable([1, 2])
init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    # Usage passing the session explicitly.
    v.load([2, 3], sess)
    print(v.eval(sess)) # prints [2 3]
    # Usage with the default session.  The 'with' block
    # above makes 'sess' the default session.
    v.load([3, 4], sess)
    print(v.eval()) # prints [3 4]
```

| Args | |

|  |  |
| --- | --- |
| `value` | New variable value |
| `session` | The session to use to evaluate this variable. If none, the default session is used. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | Session is not passed and no default session |

### `read_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L408-L417)

```
read_value()
```

Returns the value of this variable, read in the current context.

Can be different from value() if it's on another device, with control
dependencies, etc.

| Returns | |
| A `Tensor` containing the value of the variable. | |

### `ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1160-L1199)

```
ref()
```

Returns a hashable reference object to this Variable.

The primary use case for this API is to put variables in a set/dictionary.
We can't put variables in a set/dictionary as `variable.__hash__()` is no
longer available starting Tensorflow 2.0.

The following will raise an exception starting 2.0

```
>>> x = tf.Variable(5)
>>> y = tf.Variable(10)
>>> z = tf.Variable(10)
>>> variable_set = {x, y, z}
Traceback (most recent call last):
... 
TypeError: Variable is unhashable. Instead, use tensor.ref() as the key.
>>> variable_dict = {x: 'five', y: 'ten'}
Traceback (most recent call last):
... 
TypeError: Variable is unhashable. Instead, use tensor.ref() as the key.
```

Instead, we can use `variable.ref()`.

```
>>> variable_set = {x.ref(), y.ref(), z.ref()}
>>> x.ref() in variable_set
True
>>> variable_dict = {x.ref(): 'five', y.ref(): 'ten', z.ref(): 'ten'}
>>> variable_dict[y.ref()]
'ten'
```

Also, the reference object provides `.deref()` function that returns the
original Variable.

```
>>> x = tf.Variable(5)
>>> x.ref().deref()
<tf.Variable 'Variable:0' shape=() dtype=int32, numpy=5>
```

### `scatter_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L589-L603)

```
scatter_add(
    sparse_delta, use_locking=False, name=None
)
```

Adds [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to this variable.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to be added to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_div`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L655-L669)

```
scatter_div(
    sparse_delta, use_locking=False, name=None
)
```

Divide this variable by [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices).

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to divide this variable by. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_max`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L605-L620)

```
scatter_max(
    sparse_delta, use_locking=False, name=None
)
```

Updates this variable with the max of [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) and itself.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to use as an argument of max with this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_min`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L622-L637)

```
scatter_min(
    sparse_delta, use_locking=False, name=None
)
```

Updates this variable with the min of [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) and itself.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to use as an argument of min with this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_mul`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L639-L653)

```
scatter_mul(
    sparse_delta, use_locking=False, name=None
)
```

Multiply this variable by [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices).

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to multiply this variable by. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_nd_add`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L779-L823)

```
scatter_nd_add(
    indices, updates, name=None
)
```

Applies sparse addition to individual values or slices in a Variable.

The Variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self.
It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

```
[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].
```

For example, say we want to add 4 scattered elements to a rank-1 tensor to
8 elements. In Python, that update would look like this:

```
    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1] ,[7]])
    updates = tf.constant([9, 10, 11, 12])
    v.scatter_nd_add(indices, updates)
    print(v)
```

The resulting update to v would look like this:

```
[1, 13, 3, 14, 14, 6, 7, 20]
```

See [`tf.scatter_nd`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd) for more details about how to make updates to
slices.

| Args | |

|  |  |
| --- | --- |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

### `scatter_nd_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L733-L777)

```
scatter_nd_sub(
    indices, updates, name=None
)
```

Applies sparse subtraction to individual values or slices in a Variable.

Assuming the variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self.
It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

```
[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].
```

For example, say we want to add 4 scattered elements to a rank-1 tensor to
8 elements. In Python, that update would look like this:

```
    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1] ,[7]])
    updates = tf.constant([9, 10, 11, 12])
    v.scatter_nd_sub(indices, updates)
    print(v)
```

After the update `v` would look like this:

```
[1, -9, 3, -6, -4, 6, 7, -4]
```

See [`tf.scatter_nd`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd) for more details about how to make updates to
slices.

| Args | |

|  |  |
| --- | --- |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

### `scatter_nd_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L825-L869)

```
scatter_nd_update(
    indices, updates, name=None
)
```

Applies sparse assignment to individual values or slices in a Variable.

The Variable has rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into self.
It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
dimension of self.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

```
[d_0, ..., d_{Q-2}, self.shape[K], ..., self.shape[P-1]].
```

For example, say we want to add 4 scattered elements to a rank-1 tensor to
8 elements. In Python, that update would look like this:

```
    v = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1] ,[7]])
    updates = tf.constant([9, 10, 11, 12])
    v.scatter_nd_update(indices, updates)
    print(v)
```

The resulting update to v would look like this:

```
[1, 11, 3, 10, 9, 6, 7, 12]
```

See [`tf.scatter_nd`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd) for more details about how to make updates to
slices.

| Args | |

|  |  |
| --- | --- |
| `indices` | The indices to be used in the operation. |
| `updates` | The values to be used in the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

### `scatter_sub`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L573-L587)

```
scatter_sub(
    sparse_delta, use_locking=False, name=None
)
```

Subtracts [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) from this variable.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to be subtracted from this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `scatter_update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L671-L685)

```
scatter_update(
    sparse_delta, use_locking=False, name=None
)
```

Assigns [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to this variable.

| Args | |

|  |  |
| --- | --- |
| `sparse_delta` | [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) to be assigned to this variable. |
| `use_locking` | If `True`, use locking during the operation. |
| `name` | the name of the operation. |

| Returns | |
| The updated variable. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `sparse_delta` is not an `IndexedSlices`. |

### `set_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L419-L425)

```
set_shape(
    shape
)
```

Overrides the shape for this variable.

| Args | |

|  |  |
| --- | --- |
| `shape` | the `TensorShape` representing the overridden shape. |

### `sparse_read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L871-L885)

```
sparse_read(
    indices, name=None
)
```

Gather slices from params axis axis according to indices.

This function supports a subset of tf.gather, see tf.gather for details on
usage.

| Args | |

|  |  |
| --- | --- |
| `indices` | The index `Tensor`. Must be one of the following types: `int32`, `int64`. Must be in range `[0, params.shape[axis])`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `params`. | |

### `to_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1128-L1138)

```
to_proto(
    export_scope=None
)
```

Converts a `Variable` to a `VariableDef` protocol buffer.

| Args | |

|  |  |
| --- | --- |
| `export_scope` | Optional `string`. Name scope to remove. |

| Returns | |
| A `VariableDef` protocol buffer, or `None` if the `Variable` is not in the specified name scope. | |

### `value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L389-L406)

```
value()
```

Returns the last snapshot of this variable.

You usually do not need to call this method as all ops that need the value
of the variable call it automatically through a `convert_to_tensor()` call.

Returns a `Tensor` which holds the value of the variable. You can not
assign a new value to this tensor as it is not a reference to the variable.

To avoid copies, if the consumer of the returned value is on the same device
as the variable, this actually returns the live value of the variable, not
a copy. Updates to the variable are seen by the consumer. If the consumer
is on a different device it will get a copy of the variable.

| Returns | |
| A `Tensor` containing the value of the variable. | |

### `__abs__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_math_operator_overrides.py#L129-L132)

```
__abs__(
    name=None
)
```

### `__add__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__add__(
    y
)
```

### `__and__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__and__(
    y
)
```

### `__div__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__div__(
    y
)
```

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1033-L1042)

```
__eq__(
    other
)
```

Compares two variables element-wise for equality.

### `__floordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__floordiv__(
    y
)
```

### `__ge__`

```
__ge__(
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Returns the truth value of (x >= y) element-wise.

**Note:** [`math.greater_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/greater_equal) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6, 7])
y = tf.constant([5, 2, 5, 10])
tf.math.greater_equal(x, y) ==> [True, True, True, False]

x = tf.constant([5, 4, 6, 7])
y = tf.constant([5])
tf.math.greater_equal(x, y) ==> [True, False, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_getitem_override.py#L270-L311)

```
__getitem__(
    slice_spec
)
```

Creates a slice helper object given a variable.

This allows creating a sub-tensor from part of the current contents
of a variable. See [`tf.Tensor.getitem`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#__getitem__) for detailed examples
of slicing.

This function in addition also allows assignment to a sliced range.
This is similar to `__setitem__` functionality in Python. However,
the syntax is different so that the user can capture the assignment
operation for grouping or passing to `sess.run()` in TF1.
For example,

```
import tensorflow as tf
A = tf.Variable([[1,2,3], [4,5,6], [7,8,9]], dtype=tf.float32)
print(A[:2, :2])  # => [[1,2], [4,5]]

A[:2,:2].assign(22. * tf.ones((2, 2))))
print(A) # => [[22, 22, 3], [22, 22, 6], [7,8,9]]
```

Note that assignments currently do not support NumPy broadcasting
semantics.

| Args | |

|  |  |
| --- | --- |
| `var` | An `ops.Variable` object. |
| `slice_spec` | The arguments to [`Tensor.getitem`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#__getitem__). |

| Returns | |
| The appropriate slice of "tensor", based on "slice\_spec". As an operator. The operator also has a `assign()` method that can be used to generate an assignment operator. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If a slice range is negative size. |
| `TypeError` | TypeError: If the slice indices aren't int, slice, ellipsis, tf.newaxis or int32/int64 tensors. |

### `__gt__`

```
__gt__(
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Returns the truth value of (x > y) element-wise.

**Note:** [`math.greater`](https://tensorflow.google.cn/api_docs/python/tf/math/greater) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5, 2, 5])
tf.math.greater(x, y) ==> [False, True, True]

x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.greater(x, y) ==> [False, False, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

### `__invert__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_math_operator_overrides.py#L123-L126)

```
__invert__(
    name=None
)
```

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1056-L1058)

```
__iter__()
```

When executing eagerly, iterates over the value of the variable.

### `__le__`

```
__le__(
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Returns the truth value of (x <= y) element-wise.

**Note:** [`math.less_equal`](https://tensorflow.google.cn/api_docs/python/tf/math/less_equal) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less_equal(x, y) ==> [True, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 6])
tf.math.less_equal(x, y) ==> [True, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

### `__lt__`

```
__lt__(
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Returns the truth value of (x < y) element-wise.

**Note:** [`math.less`](https://tensorflow.google.cn/api_docs/python/tf/math/less) supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:

```
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less(x, y) ==> [False, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 7])
tf.math.less(x, y) ==> [False, True, True]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |

### `__matmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__matmul__(
    y
)
```

### `__mod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__mod__(
    y
)
```

### `__mul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__mul__(
    y
)
```

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L1045-L1054)

```
__ne__(
    other
)
```

Compares two variables element-wise for equality.

### `__neg__`

```
__neg__(
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
```

Computes numerical negative value element-wise.

I.e., \(y = -x\).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |

### `__or__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__or__(
    y
)
```

### `__pow__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__pow__(
    y
)
```

### `__radd__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__radd__(
    x
)
```

### `__rand__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rand__(
    x
)
```

### `__rdiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rdiv__(
    x
)
```

### `__rfloordiv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rfloordiv__(
    x
)
```

### `__rmatmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rmatmul__(
    x
)
```

### `__rmod__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rmod__(
    x
)
```

### `__rmul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rmul__(
    x
)
```

### `__ror__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__ror__(
    x
)
```

### `__rpow__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rpow__(
    x
)
```

### `__rsub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rsub__(
    x
)
```

### `__rtruediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rtruediv__(
    x
)
```

### `__rxor__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L144-L150)

```
__rxor__(
    x
)
```

### `__sub__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__sub__(
    y
)
```

### `__truediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__truediv__(
    y
)
```

### `__xor__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__xor__(
    y
)
```