# tf.load_library

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/load_library](https://tensorflow.google.cn/api_docs/python/tf/load_library)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/load_library.py#L120-L157) |

Loads a TensorFlow plugin.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.load_library`](https://tensorflow.google.cn/api_docs/python/tf/load_library)

```
tf.load_library(
    library_location
)
```

"library\_location" can be a path to a specific shared object, or a folder.
If it is a folder, all shared objects that are named "libtfkernel\*" will be
loaded. When the library is loaded, kernels registered in the library via the
`REGISTER_*` macros are made available in the TensorFlow process.

| Args | |

|  |  |
| --- | --- |
| `library_location` | Path to the plugin or the folder of plugins. Relative or absolute filesystem path to a dynamic library file or folder. |

| Returns | |
| None | |

| Raises | |

|  |  |
| --- | --- |
| `OSError` | When the file to be loaded is not found. |
| `RuntimeError` | when unable to load the library. |