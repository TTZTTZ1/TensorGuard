# tf.debugging.is_traceback_filtering_enabled

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/is_traceback_filtering_enabled](https://tensorflow.google.cn/api_docs/python/tf/debugging/is_traceback_filtering_enabled)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/traceback_utils.py#L32-L48) |

Check whether traceback filtering is currently enabled.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_traceback_filtering_enabled`](https://tensorflow.google.cn/api_docs/python/tf/debugging/is_traceback_filtering_enabled)

```
tf.debugging.is_traceback_filtering_enabled()
```

See also [`tf.debugging.enable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering) and
[`tf.debugging.disable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering). Note that filtering out
internal frames from the tracebacks of exceptions raised by TensorFlow code
is the default behavior.

| Returns | |
| True if traceback filtering is enabled (e.g. if [`tf.debugging.enable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering) was called), and False otherwise (e.g. if [`tf.debugging.disable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering) was called). | |