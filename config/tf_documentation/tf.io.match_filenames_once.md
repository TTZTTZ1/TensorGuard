# tf.io.match_filenames_once

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/match_filenames_once](https://tensorflow.google.cn/api_docs/python/tf/io/match_filenames_once)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/training/input.py#L56-L76) |

Save the list of files matching pattern, so it is only computed once.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.io.match_filenames_once`](https://tensorflow.google.cn/api_docs/python/tf/io/match_filenames_once), [`tf.compat.v1.train.match_filenames_once`](https://tensorflow.google.cn/api_docs/python/tf/io/match_filenames_once)

```
tf.io.match_filenames_once(
    pattern, name=None
)
```

**Note:** The order of the files returned is deterministic.

| Args | |

|  |  |
| --- | --- |
| `pattern` | A file pattern (glob), or 1D tensor of file patterns. |
| `name` | A name for the operations (optional). |

| Returns | |
| A variable that is initialized to the list of files matching the pattern(s). | |