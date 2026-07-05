# tf.Tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/Tensor](https://tensorflow.google.cn/api_docs/python/tf/Tensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L138-L766) |

A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) represents a multidimensional array of elements.

#### View aliases

**Main aliases**

[`tf.experimental.numpy.ndarray`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)

All elements are of a single known data type.

When writing a TensorFlow program, the main object that is
manipulated and passed around is the [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor).

A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) has the following properties:

* a single data type (float32, int32, or string, for example)
* a shape

TensorFlow supports eager execution and graph execution. In eager
execution, operations are evaluated immediately. In graph
execution, a computational graph is constructed for later
evaluation.

TensorFlow defaults to eager execution. In the example below, the
matrix multiplication results are calculated immediately.

```
>>> # Compute some values using a Tensor
>>> c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
>>> d = tf.constant([[1.0, 1.0], [0.0, 1.0]])
>>> e = tf.matmul(c, d)
>>> print(e)
tf.Tensor(
[[1. 3.]
 [3. 7.]], shape=(2, 2), dtype=float32)
```

Note that during eager execution, you may discover your `Tensors` are actually
of type `EagerTensor`. This is an internal detail, but it does give you
access to a useful function, `numpy`:

```
>>> type(e)
<class '...ops.EagerTensor'>
>>> print(e.numpy())
  [[1. 3.]
   [3. 7.]]
```

In TensorFlow, [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s are a common way to define graph execution.

A Tensor's shape (that is, the rank of the Tensor and the size of
each dimension) may not always be fully known. In [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)
definitions, the shape may only be partially known.

Most operations produce tensors of fully-known shapes if the shapes of their
inputs are also fully known, but in some cases it's only possible to find the
shape of a tensor at execution time.

A number of specialized tensors are available: see [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable),
[`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant), `tf.placeholder`, [`tf.sparse.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor), and
[`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor).

**Caution:** when constructing a tensor from a numpy array or pandas dataframe
the underlying buffer may be re-used:

```
a = np.array([1, 2, 3])
b = tf.constant(a)
a[0] = 4
print(b)  # tf.Tensor([4 2 3], shape=(3,), dtype=int64)
```

**Note:** this is an implementation detail that is subject to change and users
should not rely on this behaviour.

For more on Tensors, see the [guide](https://tensorflow.org/guide/tensor).

| Attributes | |

|  |  |
| --- | --- |
| `dtype` | The `DType` of elements in this tensor. |
| `name` |  |

|  |  |
| --- | --- |
| `ndim` |  |

|  |  |
| --- | --- |
| `shape` | Returns a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) that represents the shape of this tensor. |

```
>>> t = tf.constant([1,2,3,4,5])
>>> t.shape
TensorShape([5])
```

[`tf.Tensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#shape) is equivalent to [`tf.Tensor.get_shape()`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#get_shape).

In a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) or when building a model using
[`tf.keras.Input`](https://tensorflow.google.cn/api_docs/python/tf/keras/Input), they return the build-time shape of the
tensor, which may be partially unknown.

A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) is not a tensor. Use [`tf.shape(t)`](https://tensorflow.google.cn/api_docs/python/tf/shape) to get a tensor
containing the shape, calculated at runtime.

See [`tf.Tensor.get_shape()`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#get_shape), and [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) for details and examples.

## Methods

### `eval`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L672-L696)

```
eval(
    feed_dict=None, session=None
)
```

Evaluates this tensor in a `Session`.

**Note:** If you are not using [`compat.v1`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1) libraries, you should not need this,
(or `feed_dict` or `Session`). In eager execution (or within [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function))
you do not need to call `eval`.

Calling this method will execute all preceding operations that
produce the inputs needed for the operation that produces this
tensor.

**Note:** Before invoking [`Tensor.eval()`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#eval), its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

| Args | |

|  |  |
| --- | --- |
| `feed_dict` | A dictionary that maps `Tensor` objects to feed values. See `tf.Session.run` for a description of the valid feed values. |
| `session` | (Optional.) The `Session` to be used to evaluate this tensor. If none, the default session will be used. |

| Returns | |
| A numpy array corresponding to the value of this tensor. | |

### `experimental_ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L698-L700)

```
experimental_ref()
```

DEPRECATED FUNCTION

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use ref() instead.

### `get_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L359-L438)

```
get_shape() -> tf.TensorShape

tf.TensorShape
```

Returns a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) that represents the shape of this tensor.

In eager execution the shape is always fully-known.

```
>>> a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
>>> print(a.shape)
(2, 3)
```

[`tf.Tensor.get_shape()`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#get_shape) is equivalent to [`tf.Tensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#shape).

When executing in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) or building a model using
[`tf.keras.Input`](https://tensorflow.google.cn/api_docs/python/tf/keras/Input), [`Tensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#shape) may return a partial shape (including
`None` for unknown dimensions). See [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) for more details.

```
>>> inputs = tf.keras.Input(shape = [10])
>>> # Unknown batch size
>>> print(inputs.shape)
(None, 10)
```

The shape is computed using shape inference functions that are
registered for each [`tf.Operation`](https://tensorflow.google.cn/api_docs/python/tf/Operation).

The returned [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) is determined at *build* time, without
executing the underlying kernel. It is not a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). If you need a
shape *tensor*, either convert the [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) to a [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant), or
use the [`tf.shape(tensor)`](https://tensorflow.google.cn/api_docs/python/tf/shape) function, which returns the tensor's shape at
*execution* time.

This is useful for debugging and providing early errors. For
example, when tracing a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), no ops are being executed, shapes
may be unknown (See the [Concrete Functions
Guide](https://tensorflow.google.cn/guide/concrete_function) for details).

```
>>> @tf.function
... def my_matmul(a, b):
...   result = a@b
...   # the `print` executes during tracing.
...   print("Result shape: ", result.shape)
...   return result
```

The shape inference functions propagate shapes to the extent possible:

```
>>> f = my_matmul.get_concrete_function(
...   tf.TensorSpec([None,3]),
...   tf.TensorSpec([3,5]))
Result shape: (None, 5)
```

Tracing may fail if a shape missmatch can be detected:

```
>>> cf = my_matmul.get_concrete_function(
...   tf.TensorSpec([None,3]),
...   tf.TensorSpec([4,5]))
Traceback (most recent call last):
... 
ValueError: Dimensions must be equal, but are 3 and 4 for 'matmul' (op:
'MatMul') with input shapes: [?,3], [4,5].
```

In some cases, the inferred shape may have unknown dimensions. If
the caller has additional information about the values of these
dimensions, [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape) or [`Tensor.set_shape()`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#set_shape) can be used to augment
the inferred shape.

```
>>> @tf.function
... def my_fun(a):
...   a = tf.ensure_shape(a, [5, 5])
...   # the `print` executes during tracing.
...   print("Result shape: ", a.shape)
...   return a
```

```
>>> cf = my_fun.get_concrete_function(
...   tf.TensorSpec([None, None]))
Result shape: (5, 5)
```

| Returns | |
| A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) representing the shape of this tensor. | |

### `ref`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L702-L741)

```
ref()
```

Returns a hashable reference object to this Tensor.

The primary use case for this API is to put tensors in a set/dictionary.
We can't put tensors in a set/dictionary as `tensor.__hash__()` is no longer
available starting Tensorflow 2.0.

The following will raise an exception starting 2.0

```
>>> x = tf.constant(5)
>>> y = tf.constant(10)
>>> z = tf.constant(10)
>>> tensor_set = {x, y, z}
Traceback (most recent call last):
... 
TypeError: Tensor is unhashable. Instead, use tensor.ref() as the key.
>>> tensor_dict = {x: 'five', y: 'ten'}
Traceback (most recent call last):
... 
TypeError: Tensor is unhashable. Instead, use tensor.ref() as the key.
```

Instead, we can use `tensor.ref()`.

```
>>> tensor_set = {x.ref(), y.ref(), z.ref()}
>>> x.ref() in tensor_set
True
>>> tensor_dict = {x.ref(): 'five', y.ref(): 'ten', z.ref(): 'ten'}
>>> tensor_dict[y.ref()]
'ten'
```

Also, the reference object provides `.deref()` function that returns the
original Tensor.

```
>>> x = tf.constant(5)
>>> x.ref().deref()
<tf.Tensor: shape=(), dtype=int32, numpy=5>
```

### `set_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L440-L576)

```
set_shape(
    shape
)
```

Updates the shape of this tensor.

**Note:** It is recommended to use [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape) instead of
[`Tensor.set_shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#set_shape), because [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape) provides better checking for
programming errors and can create guarantees for compiler
optimization.

With eager execution this operates as a shape assertion.
Here the shapes match:

```
>>> t = tf.constant([[1,2,3]])
>>> t.set_shape([1, 3])
```

Passing a `None` in the new shape allows any value for that axis:

```
>>> t.set_shape([1,None])
```

An error is raised if an incompatible shape is passed.

```
>>> t.set_shape([1,5])
Traceback (most recent call last):
... 
ValueError: Tensor's shape (1, 3) is not compatible with supplied
shape [1, 5]
```

When executing in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), or building a model using
[`tf.keras.Input`](https://tensorflow.google.cn/api_docs/python/tf/keras/Input), [`Tensor.set_shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#set_shape) will *merge* the given `shape` with
the current shape of this tensor, and set the tensor's shape to the
merged value (see [`tf.TensorShape.merge_with`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape#merge_with) for details):

```
>>> t = tf.keras.Input(shape=[None, None, 3])
>>> print(t.shape)
(None, None, None, 3)
```

Dimensions set to `None` are not updated:

```
>>> t.set_shape([None, 224, 224, None])
>>> print(t.shape)
(None, 224, 224, 3)
```

The main use case for this is to provide additional shape information
that cannot be inferred from the graph alone.

For example if you know all the images in a dataset have shape [28,28,3] you
can set it with `tf.set_shape`:

```
>>> @tf.function
... def load_image(filename):
...   raw = tf.io.read_file(filename)
...   image = tf.image.decode_png(raw, channels=3)
...   # the `print` executes during tracing.
...   print("Initial shape: ", image.shape)
...   image.set_shape([28, 28, 3])
...   print("Final shape: ", image.shape)
...   return image
```

Trace the function, see the [Concrete Functions
Guide](https://tensorflow.google.cn/guide/concrete_function) for details.

```
>>> cf = load_image.get_concrete_function(
...     tf.TensorSpec([], dtype=tf.string))
Initial shape:  (None, None, 3)
Final shape: (28, 28, 3)
```

Similarly the [`tf.io.parse_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor) function could return a tensor with
any shape, even the [`tf.rank`](https://tensorflow.google.cn/api_docs/python/tf/rank) is unknown. If you know that all your
serialized tensors will be 2d, set it with `set_shape`:

```
>>> @tf.function
... def my_parse(string_tensor):
...   result = tf.io.parse_tensor(string_tensor, out_type=tf.float32)
...   # the `print` executes during tracing.
...   print("Initial shape: ", result.shape)
...   result.set_shape([None, None])
...   print("Final shape: ", result.shape)
...   return result
```

Trace the function

```
>>> concrete_parse = my_parse.get_concrete_function(
...     tf.TensorSpec([], dtype=tf.string))
Initial shape:  <unknown>
Final shape:  (None, None)
```

#### Make sure it works:

```
>>> t = tf.ones([5,3], dtype=tf.float32)
>>> serialized = tf.io.serialize_tensor(t)
>>> print(serialized.dtype)
<dtype: 'string'>
>>> print(serialized.shape)
()
>>> t2 = concrete_parse(serialized)
>>> print(t2.shape)
(5, 3)
```

**Caution:** `set_shape` ensures that the applied shape is compatible with
the existing shape, but it does not check at runtime. Setting
incorrect shapes can result in inconsistencies between the
statically-known graph and the runtime value of tensors. For runtime
validation of the shape, use [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape) instead. It also modifies
the `shape` of the tensor.

```
>>> # Serialize a rank-3 tensor
>>> t = tf.ones([5,5,5], dtype=tf.float32)
>>> serialized = tf.io.serialize_tensor(t)
>>> # The function still runs, even though it `set_shape([None,None])`
>>> t2 = concrete_parse(serialized)
>>> print(t2.shape)
(5, 5, 5)
```

| Args | |

|  |  |
| --- | --- |
| `shape` | A `TensorShape` representing the shape of this tensor, a `TensorShapeProto`, a list, a tuple, or None. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `shape` is not compatible with the current shape of this tensor. |

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

### `__array__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L625-L630)

```
__array__(
    dtype=None
)
```

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L642-L660)

```
__bool__()
```

Dummy method to prevent a tensor from being used as a Python `bool`.

This overload raises a `TypeError` when the user inadvertently
treats a `Tensor` as a boolean (most commonly in an `if` or `while`
statement), in code that was not converted by AutoGraph. For example:

```
if tf.constant(True):  # Will raise.
  # ...

if tf.constant(5) < tf.constant(7):  # Will raise.
  # ...
```

| Raises | |
| `TypeError`. | |

### `__div__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L105-L131)

```
__div__(
    y
)
```

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_math_operator_overrides.py#L135-L138)

```
__eq__(
    other
)
```

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_getitem_override.py#L65-L267)

```
__getitem__(
    slice_spec, var=None
)
```

Overload for Tensor.**getitem**.

This operation extracts the specified region from the tensor.
The notation is similar to NumPy with the restriction that
currently only support basic indexing. That means that
using a non-scalar tensor as input is not currently allowed.

#### Some useful examples:

```
# Strip leading and trailing 2 elements
foo = tf.constant([1,2,3,4,5,6])
print(foo[2:-2])  # => [3,4]

# Skip every other row and reverse the order of the columns
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[::2,::-1])  # => [[3,2,1], [9,8,7]]

# Use scalar tensors as indices on both dimensions
print(foo[tf.constant(0), tf.constant(2)])  # => 3

# Insert another dimension
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[tf.newaxis, :, :]) # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[:, tf.newaxis, :]) # => [[[1,2,3]], [[4,5,6]], [[7,8,9]]]
print(foo[:, :, tf.newaxis]) # => [[[1],[2],[3]], [[4],[5],[6]],
[[7],[8],[9]]]

# Ellipses (3 equivalent operations)
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[tf.newaxis, :, :])  # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[tf.newaxis, ...])  # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[tf.newaxis])  # => [[[1,2,3], [4,5,6], [7,8,9]]]

# Masks
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[foo > 2])  # => [3, 4, 5, 6, 7, 8, 9]
```

| Notes | |
|  | |

* [`tf.newaxis`](https://tensorflow.google.cn/api_docs/python/tf#newaxis) is `None` as in NumPy.
* An implicit ellipsis is placed at the end of the `slice_spec`
* NumPy advanced indexing is currently not supported.

| Purpose in the API | |
| This method is exposed in TensorFlow's API so that library developers can register dispatching for [`Tensor.getitem`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#__getitem__) to allow it to handle custom composite tensors & other custom objects. | |

The API symbol is not intended to be called by users directly and does
appear in TensorFlow's generated documentation.

| Args | |

|  |  |
| --- | --- |
| `tensor` | An tensor.Tensor object. |
| `slice_spec` | The arguments to Tensor.**getitem**. |
| `var` | In the case of variable slice assignment, the Variable object to slice (i.e. tensor is the read-only view of this variable). |

| Returns | |
| The appropriate slice of "tensor", based on "slice\_spec". | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If a slice range is negative size. |
| `TypeError` | If the slice indices aren't int, slice, ellipsis, tf.newaxis or scalar int32/int64 tensors. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L321-L326)

```
__iter__()
```

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

### `__len__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L632-L635)

```
__len__()
```

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_math_operator_overrides.py#L141-L144)

```
__ne__(
    other
)
```

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

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`

### `__nonzero__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L662-L670)

```
__nonzero__()
```

Dummy method to prevent a tensor from being used as a Python `bool`.

This is the Python 2.x counterpart to `__bool__()` above.

| Raises | |
| `TypeError`. | |

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

| Class Variables | |

|  |  |
| --- | --- |
| OVERLOADABLE\_OPERATORS |  |

```
{
 '__abs__',
 '__add__',
 '__and__',
 '__div__',
 '__eq__',
 '__floordiv__',
 '__ge__',
 '__getitem__',
 '__gt__',
 '__invert__',
 '__le__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__or__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdiv__',
 '__rfloordiv__',
 '__rmatmul__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__sub__',
 '__truediv__',
 '__xor__'
}
```