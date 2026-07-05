# tf.mlir.experimental.convert_function

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_function](https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_function)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/mlir/mlir.py#L48-L92) |

Import a ConcreteFunction and convert it to a textual MLIR module.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.mlir.experimental.convert_function`](https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_function)

```
tf.mlir.experimental.convert_function(
    concrete_function,
    pass_pipeline='tf-standard-pipeline',
    show_debug_info=False
)
```

This API is only intended for inspecting the internals of TensorFlow and the
string returned is at the moment intended for debugging purposes.

A [tf.function](https://tensorflow.google.cn/api_docs/python/tf/function) can be
imported and converted from TensorFlow to TensorFlow MLIR with this API by
extracting its ConcreteFunction (eagerly-executing wrapper around a
[tf.Graph](https://tensorflow.google.cn/api_docs/python/tf/Graph)).

#### For example:

```
>>> @tf.function
... def add(a, b):
...   return a + b
```

```
>>> concrete_function = add.get_concrete_function(
...     tf.TensorSpec(None, tf.dtypes.float32),
...     tf.TensorSpec(None, tf.dtypes.float32))
>>> tf.mlir.experimental.convert_function(concrete_function)
'...module attributes {...} {...}...'
```

| Args | |

|  |  |
| --- | --- |
| `concrete_function` | An object of type ConcreteFunction. |
| `pass_pipeline` | A textual description of an MLIR Pass Pipeline to run on the module, see MLIR documentation for the [textual pass pipeline syntax](https://mlir.llvm.org/docs/PassManagement/#textual-pass-pipeline-specification). |
| `show_debug_info` | Whether to include locations in the emitted textual form. |

| Returns | |
| A textual representation of the MLIR module corresponding to the ConcreteFunction. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if concrete\_function is invalid or cannot be converted to MLIR. |