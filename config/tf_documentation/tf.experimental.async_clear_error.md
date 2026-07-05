# tf.experimental.async_clear_error

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/async_clear_error](https://tensorflow.google.cn/api_docs/python/tf/experimental/async_clear_error)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/context.py#L2873-L2894) |

Clear pending operations and error statuses in async execution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.async_clear_error`](https://tensorflow.google.cn/api_docs/python/tf/experimental/async_clear_error)

```
tf.experimental.async_clear_error()
```

In async execution mode, an error in op/function execution can lead to errors
in subsequent ops/functions that are scheduled but not yet executed. Calling
this method clears all pending operations and reset the async execution state.

#### Example:

```
while True:
  try:
    # Step function updates the metric `loss` internally
    train_step_fn()
  except tf.errors.OutOfRangeError:
    tf.experimental.async_clear_error()
    break
logging.info('loss = %s', loss.numpy())
```