# tf.debugging.disable_traceback_filtering

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/traceback_utils.py#L76-L96) |

Disable filtering out TensorFlow-internal frames in exception stack traces.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.disable_traceback_filtering`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering)

```
tf.debugging.disable_traceback_filtering()
```

Raw TensorFlow stack traces involve many internal frames, which can be
challenging to read through, while not being actionable for end users.
By default, TensorFlow filters internal frames in most exceptions that it
raises, to keep stack traces short, readable, and focused on what's
actionable for end users (their own code).

Calling [`tf.debugging.disable_traceback_filtering`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering) disables this filtering
mechanism, meaning that TensorFlow exceptions stack traces will include
all frames, in particular TensorFlow-internal ones.

**If you are debugging a TensorFlow-internal issue, you need to call
[`tf.debugging.disable_traceback_filtering`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_traceback_filtering)**.
To re-enable traceback filtering afterwards, you can call
[`tf.debugging.enable_traceback_filtering()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_traceback_filtering).