# tf.experimental.async_scope

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/async_scope](https://tensorflow.google.cn/api_docs/python/tf/experimental/async_scope)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/context.py#L2809-L2854) |

Context manager for grouping async operations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.async_scope`](https://tensorflow.google.cn/api_docs/python/tf/experimental/async_scope)

```
@tf_contextlib.contextmanager
tf.experimental.async_scope()
```

Ops/function calls inside the scope can return before finishing the actual
execution. When exiting the async scope, a synchronization barrier will be
automatically added to ensure the completion of all async op and function
execution, potentially raising exceptions if async execution results in
an error state.

Users may write the following code to asynchronously invoke `train_step_fn`
and log the `loss` metric for every `num_steps` steps in a training loop.
`train_step_fn` internally consumes data using `iterator.get_next()`, and may
throw OutOfRangeError when running out of data. In the case:

```
try:
  with tf.experimental.async_scope():
    for _ in range(num_steps):
      # Step function updates the metric `loss` internally
      train_step_fn()
except tf.errors.OutOfRangeError:
  tf.experimental.async_clear_error()
logging.info('loss = %s', loss.numpy())
```

| Yields | |
| Context manager for grouping async operations. | |