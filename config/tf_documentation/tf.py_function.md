# tf.py_function

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/py_function](https://tensorflow.google.cn/api_docs/python/tf/py_function)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/script_ops.py#L461-L641) |

Wraps a python function into a TensorFlow op that executes it eagerly.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function)

```
tf.py_function(
    func=None, inp=None, Tout=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with the tf.data API](https://tensorflow.google.cn/guide/data_performance) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) | * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) |

Using [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) allows you to run a python
function using eager execution, inside the [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)'s graph.
This has two main effects:

1. This allows you to use nofunc=None, inp=None, Tout=None tensorflow code
   inside your [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function).
2. It allows you to run python control logic in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) without
   relying on [`tf.autograph`](https://tensorflow.google.cn/api_docs/python/tf/autograph) to convert the code to use tensorflow control logic
   (tf.cond, tf.while\_loop).

Both of these features can be useful for debugging.

Since [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) operates on `Tensor`s it is still
differentiable (once).

There are two ways to use this function:

### As a decorator

Use [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) as a decorator to ensure the function always runs
eagerly.

When using [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) as a decorator:

* you must set `Tout`
* you may set `name`
* you must not set `func` or `inp`

For example, you might use [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) to
implement the log huber function.

```
>>> @tf.py_function(Tout=tf.float32)
... def py_log_huber(x, m):
...   print('Running with eager execution.')
...   if tf.abs(x) <= m:
...     return x**2
...   else:
...     return m**2 * (1 - 2 * tf.math.log(m) + tf.math.log(x**2))
```

Under eager execution the function operates normally:

```
>>> x = tf.constant(1.0)
>>> m = tf.constant(2.0)
>>> 
>>> print(py_log_huber(x,m).numpy())
Running with eager execution.
1.0
```

Inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) the [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) is not converted to a [`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph).:

```
>>> @tf.function
... def tf_wrapper(x):
...   print('Tracing.')
...   m = tf.constant(2.0)
...   return py_log_huber(x,m)
```

The [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) only executes eagerly, and only when the [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)
is called:

```
>>> print(tf_wrapper(x).numpy())
Tracing.
Running with eager execution.
1.0
>>> print(tf_wrapper(x).numpy())
Running with eager execution.
1.0
```

Gradients work as expected:

```
>>> with tf.GradientTape() as t:
...   t.watch(x)
...   y = tf_wrapper(x)
Running with eager execution.
>>> 
>>> t.gradient(y, x).numpy()
2.0
```

### Inplace

You can also skip the decorator and use [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) in-place.
This form is a useful shortcut if you don't control the function's source,
but it is harder to read.

```
>>> # No decorator
>>> def log_huber(x, m):
...   if tf.abs(x) <= m:
...     return x**2
...   else:
...     return m**2 * (1 - 2 * tf.math.log(m) + tf.math.log(x**2))
>>> 
>>> x = tf.constant(1.0)
>>> m = tf.constant(2.0)
>>> 
>>> tf.py_function(func=log_huber, inp=[x, m], Tout=tf.float32).numpy()
1.0
```

### More info

You can also use [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) to debug your models at runtime
using Python tools, i.e., you can isolate portions of your code that
you want to debug, wrap them in Python functions and insert `pdb` tracepoints
or print statements as desired, and wrap those functions in
[`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function).

For more information on eager execution, see the
[Eager guide](https://tensorflow.org/guide/eager).

[`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) is similar in spirit to [`tf.numpy_function`](https://tensorflow.google.cn/api_docs/python/tf/numpy_function), but unlike
the latter, the former lets you use TensorFlow operations in the wrapped
Python function. In particular, while [`tf.compat.v1.py_func`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/py_func) only runs on CPUs
and wraps functions that take NumPy arrays as inputs and return NumPy arrays
as outputs, [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) can be placed on GPUs and wraps functions
that take Tensors as inputs, execute TensorFlow operations in their bodies,
and return Tensors as outputs.

**Note:** We recommend to avoid using [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) outside of prototyping
and experimentation due to the following known limitations:

* Calling [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) will acquire the Python Global Interpreter Lock
  (GIL) that allows only one thread to run at any point in time. This will
  preclude efficient parallelization and distribution of the execution of the
  program.
* The body of the function (i.e. `func`) will not be serialized in a
  `GraphDef`. Therefore, you should not use this function if you need to
  serialize your model and restore it in a different environment.
* The operation must run in the same address space as the Python program
  that calls [`tf.py_function()`](https://tensorflow.google.cn/api_docs/python/tf/py_function). If you are using distributed
  TensorFlow, you must run a [`tf.distribute.Server`](https://tensorflow.google.cn/api_docs/python/tf/distribute/Server) in the same process as the
  program that calls [`tf.py_function()`](https://tensorflow.google.cn/api_docs/python/tf/py_function) and you must pin the created
  operation to a device in that server (e.g. using `with tf.device():`).
* Currently [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) is not compatible with XLA. Calling
  [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) inside [`tf.function(jit_compile=True)`](https://tensorflow.google.cn/api_docs/python/tf/function) will raise an
  error.

| Args | |

|  |  |
| --- | --- |
| `func` | A Python function that accepts `inp` as arguments, and returns a value (or list of values) whose type is described by `Tout`. Do not set `func` when using [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) as a decorator. |
| `inp` | Input arguments for `func`. A list whose elements are `Tensor`s or `CompositeTensors` (such as [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor)); or a single `Tensor` or `CompositeTensor`. Do not set `inp` when using [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) as a decorator. |
| `Tout` | The type(s) of the value(s) returned by `func`. One of the following. |

* If `func` returns a `Tensor` (or a value that can be converted to a
  Tensor): the [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) for that value. \* If `func` returns a
  `CompositeTensor`: The [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) for that value. \* If `func` returns
  `None`: the empty list (`[]`). \* If `func` returns a list of `Tensor` and
  `CompositeTensor` values: a corresponding list of [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType)s and
  [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec)s for each value.| `name` | A name for the operation (optional). |

| Returns | |
|  | |

* If `func` is `None` this returns a decorator that will ensure the
  decorated function will always run with eager execution even if called
  from a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)/[`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph).
* If used `func` is not `None` this executes `func` with eager execution
  and returns the result: a `Tensor`, `CompositeTensor`, or list of
  `Tensor` and `CompositeTensor`; or an empty list if `func` returns `None`.