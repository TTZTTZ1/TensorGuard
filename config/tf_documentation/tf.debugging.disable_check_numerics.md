# tf.debugging.disable_check_numerics

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_check_numerics](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_check_numerics)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/debug/lib/check_numerics_callback.py#L445-L469) |

Disable the eager/graph unified numerics checking mechanism.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.disable_check_numerics`](https://tensorflow.google.cn/api_docs/python/tf/debugging/disable_check_numerics)

```
tf.debugging.disable_check_numerics()
```

This method can be used after a call to [`tf.debugging.enable_check_numerics()`](https://tensorflow.google.cn/api_docs/python/tf/debugging/enable_check_numerics)
to disable the numerics-checking mechanism that catches infinity and NaN
values output by ops executed eagerly or in tf.function-compiled graphs.

This method is idempotent. Calling it multiple times has the same effect
as calling it once.

This method takes effect only on the thread in which it is called.