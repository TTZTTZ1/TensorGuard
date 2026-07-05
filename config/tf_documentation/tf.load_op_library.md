# tf.load_op_library

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/load_op_library](https://tensorflow.google.cn/api_docs/python/tf/load_op_library)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/load_library.py#L31-L74) |

Loads a TensorFlow plugin, containing custom ops and kernels.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.load_op_library`](https://tensorflow.google.cn/api_docs/python/tf/load_op_library)

```
tf.load_op_library(
    library_filename
)
```

Pass "library\_filename" to a platform-specific mechanism for dynamically
loading a library. The rules for determining the exact location of the
library are platform-specific and are not documented here. When the
library is loaded, ops and kernels registered in the library via the
`REGISTER_*` macros are made available in the TensorFlow process. Note
that ops with the same name as an existing op are rejected and not
registered with the process.

| Args | |

|  |  |
| --- | --- |
| `library_filename` | Path to the plugin. Relative or absolute filesystem path to a dynamic library file. |

| Returns | |
| A python module containing the Python wrappers for Ops defined in the plugin. | |

| Raises | |

|  |  |
| --- | --- |
| `RuntimeError` | when unable to load the library or get the python wrappers. |