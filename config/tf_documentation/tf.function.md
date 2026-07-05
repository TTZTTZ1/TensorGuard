# tf.function

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/function](https://tensorflow.google.cn/api_docs/python/tf/function)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/polymorphic_function/polymorphic_function.py#L1300-L1682) |

Compiles a function into a callable TensorFlow graph. (deprecated arguments) (deprecated arguments) (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.function`](https://tensorflow.google.cn/api_docs/python/tf/function)

```
tf.function(
    func=None,
    input_signature=None,
    autograph=True,
    jit_compile=None,
    reduce_retracing=False,
    experimental_implements=None,
    experimental_autograph_options=None,
    experimental_attributes=None,
    experimental_relax_shapes=None,
    experimental_compile=None,
    experimental_follow_type_hints=None
) -> tf.types.experimental.PolymorphicFunction

tf.types.experimental.PolymorphicFunction
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Random number generation](https://tensorflow.google.cn/guide/random_numbers) * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) | * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Distributed Input](https://tensorflow.google.cn/tutorials/distribute/input) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) |

**Deprecated:** SOME ARGUMENTS ARE DEPRECATED: `(experimental_compile)`. They will be removed in a future version.
Instructions for updating:
experimental\_compile is deprecated, use jit\_compile instead**Deprecated:** SOME ARGUMENTS ARE DEPRECATED: `(experimental_relax_shapes)`. They will be removed in a future version.
Instructions for updating:
experimental\_relax\_shapes is deprecated, use reduce\_retracing instead**Deprecated:** SOME ARGUMENTS ARE DEPRECATED: `(experimental_follow_type_hints)`. They will be removed in a future version.
Instructions for updating:
experimental\_follow\_type\_hints is deprecated

[`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) constructs a [`tf.types.experimental.PolymorphicFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction) that
executes a TensorFlow graph ([`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph)) created by trace-compiling the
TensorFlow operations in `func`. More information on the topic can be found
in [Introduction to Graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs).

See [Better Performance with tf.function](https://tensorflow.google.cn/guide/function) for tips on performance and
known limitations.

#### Example usage:

```
>>> @tf.function
... def f(x, y):
...   return x ** 2 + y
>>> x = tf.constant([2, 3])
>>> y = tf.constant([3, -2])
>>> f(x, y)
<tf.Tensor: ... numpy=array([7, 7], ...)>
```

The trace-compilation allows non-TensorFlow operations to execute, but under
special conditions. In general, only TensorFlow operations are guaranteed to
run and create fresh results whenever the `PolymorphicFunction` is called.

## Features

`func` may use data-dependent Python control flow statements, including `if`,
`for`, `while` `break`, `continue` and `return`:

```
>>> @tf.function
... def f(x):
...   if tf.reduce_sum(x) > 0:
...     return x * x
...   else:
...     return -x // 2
>>> f(tf.constant(-2))
<tf.Tensor: ... numpy=1>
```

`func`'s closure may include [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) and [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable) objects:

```
>>> @tf.function
... def f():
...   return x ** 2 + y
>>> x = tf.constant([-2, -3])
>>> y = tf.Variable([3, -2])
>>> f()
<tf.Tensor: ... numpy=array([7, 7], ...)>
```

`func` may also use ops with side effects, such as [`tf.print`](https://tensorflow.google.cn/api_docs/python/tf/print), [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)
and others:

```
>>> v = tf.Variable(1)
>>> @tf.function
... def f(x):
...   for i in tf.range(x):
...     v.assign_add(i)
>>> f(3)
>>> v
<tf.Variable ... numpy=4>
```

**Important:** Any Python side-effects (appending to a list, printing with
`print`, etc) will only happen once, when `func` is traced. To have
side-effects executed into your [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) they need to be written
as TF ops:

```
>>> l = []
>>> @tf.function
... def f(x):
...   for i in x:
...     l.append(i + 1)    # Caution! Will only happen once when tracing
>>> f(tf.constant([1, 2, 3]))
>>> l
[<tf.Tensor ...>]
```

Instead, use TensorFlow collections like [`tf.TensorArray`](https://tensorflow.google.cn/api_docs/python/tf/TensorArray):

```
>>> @tf.function
... def f(x):
...   ta = tf.TensorArray(dtype=tf.int32, size=0, dynamic_size=True)
...   for i in range(len(x)):
...     ta = ta.write(i, x[i] + 1)
...   return ta.stack()
>>> f(tf.constant([1, 2, 3]))
<tf.Tensor: ..., numpy=array([2, 3, 4], ...)>
```

## [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) creates polymorphic callables

Internally, [`tf.types.experimental.PolymorphicFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction) may contain multiple
[`tf.types.experimental.ConcreteFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/ConcreteFunction)s, each specialized to arguments with
different data types or shapes, since TensorFlow can perform more
optimizations on graphs of specific shapes, dtypes and values of constant
arguments. [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) treats any pure Python values as opaque objects (best
thought of as compile-time constants), and builds a separate [`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph) for
each set of Python arguments that it encounters.
For more information, see the
[tf.function guide](https://tensorflow.google.cn/guide/function#rules_of_tracing)

Executing a `PolymorphicFunction` will select and execute the appropriate
`ConcreteFunction` based on the argument types and values.

To obtain an individual `ConcreteFunction`, use the
[`PolymorphicFunction.get_concrete_function`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction#get_concrete_function) method. It can be called with the
same arguments as `func` and returns a
[`tf.types.experimental.ConcreteFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/ConcreteFunction). `ConcreteFunction`s are backed by a
single [`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph):

```
>>> @tf.function
... def f(x):
...   return x + 1
>>> isinstance(f.get_concrete_function(1).graph, tf.Graph)
True
```

`ConcreteFunction`s can be executed just like `PolymorphicFunction`s, but their
input is resticted to the types to which they're specialized.

## Retracing

`ConcreteFunctions` are built (traced) on the fly, as the `PolymorphicFunction` is
called with new TensorFlow types or shapes, or with new Python values as
arguments. When `PolymorphicFunction` builds a new trace, it is said that `func`
is retraced. Retracing is a frequent performance concern for [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) as
it can be considerably slower than executing a graph that's already been
traced. It is ideal to minimize the amount of retracing in your code.

**Caution:** Passing python scalars or lists as arguments to [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) will
usually retrace. To avoid this, pass numeric arguments as Tensors whenever
possible:

```
>>> @tf.function
... def f(x):
...   return tf.abs(x)
>>> f1 = f.get_concrete_function(1)
>>> f2 = f.get_concrete_function(2)  # Slow - compiles new graph
>>> f1 is f2
False
>>> f1 = f.get_concrete_function(tf.constant(1))
>>> f2 = f.get_concrete_function(tf.constant(2))  # Fast - reuses f1
>>> f1 is f2
True
```

Python numerical arguments should only be used when they take few distinct
values, such as hyperparameters like the number of layers in a neural network.

## Input signatures

For Tensor arguments, `PolymorphicFunction`creates a new `ConcreteFunction` for
every unique set of input shapes and datatypes. The example below creates two
separate `ConcreteFunction`s, each specialized to a different shape:

```
>>> @tf.function
... def f(x):
...   return x + 1
>>> vector = tf.constant([1.0, 1.0])
>>> matrix = tf.constant([[3.0]])
>>> f.get_concrete_function(vector) is f.get_concrete_function(matrix)
False
```

An "input signature" can be optionally provided to [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) to control
this process. The input signature specifies the shape and type of each
Tensor argument to the function using a [`tf.TensorSpec`](https://tensorflow.google.cn/api_docs/python/tf/TensorSpec) object. More general
shapes can be used. This ensures only one `ConcreteFunction` is created, and
restricts the `PolymorphicFunction` to the specified shapes and types. It is
an effective way to limit retracing when Tensors have dynamic shapes.

```
>>> @tf.function(
...     input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
... def f(x):
...   return x + 1
>>> vector = tf.constant([1.0, 1.0])
>>> matrix = tf.constant([[3.0]])
>>> f.get_concrete_function(vector) is f.get_concrete_function(matrix)
True
```

## Variables may only be created once

[`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) only allows creating new [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable) objects when it is called
for the first time:

```
>>> class MyModule(tf.Module):
...   def __init__(self):
...     self.v = None
... 
...   @tf.function
...   def __call__(self, x):
...     if self.v is None:
...       self.v = tf.Variable(tf.ones_like(x))
...     return self.v * x
```

In general, it is recommended to create [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)s outside of
[`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function).
In simple cases, persisting state across [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) boundaries may be
implemented using a pure functional style in which state is represented by
[`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)s passed as arguments and returned as return values.

Contrast the two styles below:

```
>>> state = tf.Variable(1)
>>> @tf.function
... def f(x):
...   state.assign_add(x)
>>> f(tf.constant(2))  # Non-pure functional style
>>> state
<tf.Variable ... numpy=3>
```

```
>>> state = tf.constant(1)
>>> @tf.function
... def f(state, x):
...   state += x
...   return state
>>> state = f(state, tf.constant(2))  # Pure functional style
>>> state
<tf.Tensor: ... numpy=3>
```

## Python operations execute only once per trace

`func` may contain TensorFlow operations mixed with pure Python operations.
However, when the function is executed, only the TensorFlow operations will
run. The Python operations run only once, at trace time. If TensorFlow
operations depend on results from Python operations, those results will be
frozen into the graph.

```
>>> @tf.function
... def f(a, b):
...   print('this runs at trace time; a is', a, 'and b is', b)
...   return b
>>> f(1, tf.constant(1))
this runs at trace time; a is 1 and b is Tensor("...", shape=(), dtype=int32)
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

```
>>> f(1, tf.constant(2))
<tf.Tensor: shape=(), dtype=int32, numpy=2>
```

```
>>> f(2, tf.constant(1))
this runs at trace time; a is 2 and b is Tensor("...", shape=(), dtype=int32)
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

```
>>> f(2, tf.constant(2))
<tf.Tensor: shape=(), dtype=int32, numpy=2>
```

| Args | |

|  |  |
| --- | --- |
| `func` | The function to be compiled. If `func` is None, [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) returns a decorator that can be invoked with a single argument - `func`. In other words, `tf.function(input_signature=...)(func)` is equivalent to [`tf.function(func, input_signature=...)`](https://tensorflow.google.cn/api_docs/python/tf/function). The former can be used as decorator. |
| `input_signature` | A possibly nested sequence of [`tf.TensorSpec`](https://tensorflow.google.cn/api_docs/python/tf/TensorSpec) objects specifying the shapes and dtypes of the Tensors that will be supplied to this function. If `None`, a separate function is instantiated for each inferred input signature. If input\_signature is specified, every input to `func` must be a `Tensor`, and `func` cannot accept `**kwargs`. |
| `autograph` | Whether autograph should be applied on `func` before tracing a graph. Data-dependent Python control flow statements require `autograph=True`. For more information, see the [tf.function and AutoGraph guide](https://tensorflow.google.cn/guide/function#autograph_transformations). |
| `jit_compile` | If `True`, compiles the function using [XLA](https://tensorflow.org/xla). XLA performs compiler optimizations, such as fusion, and attempts to emit more efficient code. This may drastically improve the performance. If set to `True`, the whole function needs to be compilable by XLA, or an [`errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError) is thrown. If `None` (default), compiles the function with XLA when running on TPU and goes through the regular function execution path when running on other devices. If `False`, executes the function without XLA compilation. Set this value to `False` when directly running a multi-device function on TPUs (e.g. two TPU cores, one TPU core and its host CPU). Not all functions are compilable, see a list of [sharp corners](https://tensorflow.org/xla/known_issues). |
| `reduce_retracing` | When True, [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) attempts to reduce the amount of retracing, for example by using more generic shapes. This can be controlled for user objects by customizing their associated [`tf.types.experimental.TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType). |
| `experimental_implements` | If provided, contains a name of a "known" function this implements. For example "mycompany.my\_recurrent\_cell". This is stored as an attribute in inference function, which can then be detected when processing serialized function. See [standardizing composite ops](https://github.com/tensorflow/community/blob/master/rfcs/20190610-standardizing-composite_ops.md)  for details. For an example of utilizing this attribute see this [example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/lite/transforms/prepare_composite_functions_tf.cc) The code above automatically detects and substitutes function that implements "embedded\_matmul" and allows TFLite to substitute its own implementations. For instance, a tensorflow user can use this attribute to mark that their function also implements `embedded_matmul` (perhaps more efficiently!) by specifying it using this parameter: `@tf.function(experimental_implements="embedded_matmul")` This can either be specified as just the string name of the function or a NameAttrList corresponding to a list of key-value attributes associated with the function name. The name of the function will be in the 'name' field of the NameAttrList. To define a formal TF op for this function implements, try the experimental [composite TF](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/tfr) project. |
| `experimental_autograph_options` | Optional tuple of [`tf.autograph.experimental.Feature`](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/Feature) values. |
| `experimental_attributes` | Optional dictionary of attributes to include in the generated FunctionDefs. |
| `experimental_relax_shapes` | Deprecated. Use `reduce_retracing` instead. |
| `experimental_compile` | Deprecated alias to 'jit\_compile'. |
| `experimental_follow_type_hints` | Deprecated. Please use input\_signature or reduce\_retracing instead. |

| Returns | |
| If `func` is not None, returns a [`tf.types.experimental.PolymorphicFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction). If `func` is None, returns a decorator that, when invoked with a single `func` argument, returns a [`tf.types.experimental.PolymorphicFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction). | |

| Raises | |
| `ValueError` when attempting to use `jit_compile=True`, but XLA support is not available. | |