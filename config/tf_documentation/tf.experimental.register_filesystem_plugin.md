# tf.experimental.register_filesystem_plugin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/register_filesystem_plugin](https://tensorflow.google.cn/api_docs/python/tf/experimental/register_filesystem_plugin)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/load_library.py#L199-L220) |

Loads a TensorFlow FileSystem plugin.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.register_filesystem_plugin`](https://tensorflow.google.cn/api_docs/python/tf/experimental/register_filesystem_plugin)

```
tf.experimental.register_filesystem_plugin(
    plugin_location
)
```

| Args | |

|  |  |
| --- | --- |
| `plugin_location` | Path to the plugin. Relative or absolute filesystem plugin path to a dynamic library file. |

| Returns | |
| None | |

| Raises | |

|  |  |
| --- | --- |
| `OSError` | When the file to be loaded is not found. |
| `RuntimeError` | when unable to load the library. |