# tf.data.experimental.enable_debug_mode

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enable_debug_mode](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enable_debug_mode)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/debug_mode.py#L24-L72) |

Enables debug mode for tf.data.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.enable_debug_mode`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enable_debug_mode)

```
tf.data.experimental.enable_debug_mode()
```

Example usage with pdb module:

```
import tensorflow as tf
import pdb

tf.data.experimental.enable_debug_mode()

def func(x):
  # Python 3.7 and older requires `pdb.Pdb(nosigint=True).set_trace()`
  pdb.set_trace()
  x = x + 1
  return x

dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset = dataset.map(func)

for item in dataset:
  print(item)
```

The effect of debug mode is two-fold:

1) Any transformations that would introduce asynchrony, parallelism, or
non-determinism to the input pipeline execution will be forced to execute
synchronously, sequentially, and deterministically.

2) Any user-defined functions passed into tf.data transformations such as
`map` will be wrapped in [`tf.py_function`](https://tensorflow.google.cn/api_docs/python/tf/py_function) so that their body is executed
"eagerly" as a Python function as opposed to a traced TensorFlow graph, which
is the default behavior. Note that even when debug mode is enabled, the
user-defined function is still traced to infer the shape and type of its
outputs; as a consequence, any `print` statements or breakpoints will be
triggered once during the tracing before the actual execution of the input
pipeline.

**Note:** As the debug mode setting affects the construction of the tf.data input
pipeline, it should be enabled before any tf.data definitions.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | When invoked from graph mode. |