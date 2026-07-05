# tf.debugging.experimental.disable_dump_debug_info

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/experimental/disable_dump_debug_info](https://tensorflow.google.cn/api_docs/python/tf/debugging/experimental/disable_dump_debug_info)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/debug/lib/dumping_callback.py#L863-L886) |

Disable the currently-enabled debugging dumping.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.experimental.disable_dump_debug_info`](https://tensorflow.google.cn/api_docs/python/tf/debugging/experimental/disable_dump_debug_info)

```
tf.debugging.experimental.disable_dump_debug_info()
```

If the `enable_dump_debug_info()` method under the same Python namespace
has been invoked before, calling this method disables it. If no call to
`enable_dump_debug_info()` has been made, calling this method is a no-op.
Calling this method more than once is idempotent.