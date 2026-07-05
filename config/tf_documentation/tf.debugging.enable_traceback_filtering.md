# tf.debugging.enable_traceback_filtering

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/traceback_utils.py#L51-L73) |

Enable filtering out TensorFlow-internal frames in exception stack traces.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.enable_traceback_filtering`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering)

```
tf.debugging.enable_traceback_filtering()
```

Raw TensorFlow stack traces involve many internal frames, which can be
challenging to read through, while not being actionable for end users.
By default, TensorFlow filters internal frames in most exceptions that it
raises, to keep stack traces short, readable, and focused on what's
actionable for end users (their own code).

If you have previously disabled traceback filtering via
[`tf.debugging.disable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering), you can re-enable it via
[`tf.debugging.enable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering).

| Raises | |

|  |  |
| --- | --- |
| `RuntimeError` | If Python version is not at least 3.7. |