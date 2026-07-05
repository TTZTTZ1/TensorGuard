# tf.mlir.experimental.convert_graph_def

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_graph_def](https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_graph_def)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/mlir/mlir.py#L21-L45) |

Import a GraphDef and convert it to a textual MLIR module.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.mlir.experimental.convert_graph_def`](https://tensorflow.google.cn/api_docs/python/tf/mlir/experimental/convert_graph_def)

```
tf.mlir.experimental.convert_graph_def(
    graph_def,
    pass_pipeline='tf-standard-pipeline',
    show_debug_info=False
)
```

This API is only intended for inspecting the internals of TensorFlow and the
string returned is at the moment intended for debugging purposes.

| Args | |

|  |  |
| --- | --- |
| `graph_def` | An object of type graph\_pb2.GraphDef or a textual proto representation of a valid GraphDef. |
| `pass_pipeline` | A textual description of an MLIR Pass Pipeline to run on the module, see MLIR documentation for the [textual pass pipeline syntax](https://mlir.llvm.org/docs/PassManagement/#textual-pass-pipeline-specification). |
| `show_debug_info` | Whether to include locations in the emitted textual form. |

| Returns | |
| A textual representation of the MLIR module corresponding to the graphdef. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if graph\_def is invalid or cannot be converted to MLIR. |