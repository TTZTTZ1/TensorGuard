# tf.saved_model.contains_saved_model

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/contains_saved_model](https://tensorflow.google.cn/api_docs/python/tf/saved_model/contains_saved_model)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/saved_model/loader_impl.py#L252-L270) |

Checks whether the provided export directory could contain a SavedModel.

```
tf.saved_model.contains_saved_model(
    export_dir
)
```

Note that the method does not load any data by itself. If the method returns
`false`, the export directory definitely does not contain a SavedModel. If the
method returns `true`, the export directory may contain a SavedModel but
provides no guarantee that it can be loaded.

| Args | |

|  |  |
| --- | --- |
| `export_dir` | Absolute path to possible export location. For example, '/my/foo/model'. |

| Returns | |
| True if the export directory contains SavedModel files, False otherwise. | |