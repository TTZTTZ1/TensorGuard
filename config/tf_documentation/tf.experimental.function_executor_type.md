# tf.experimental.function_executor_type

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/function_executor_type](https://tensorflow.google.cn/api_docs/python/tf/experimental/function_executor_type)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/context.py#L2658-L2678) |

Context manager for setting the executor of eager defined functions.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.function_executor_type`](https://tensorflow.google.cn/api_docs/python/tf/experimental/function_executor_type)

```
@tf_contextlib.contextmanager
tf.experimental.function_executor_type(
    executor_type
)
```

Eager defined functions are functions decorated by tf.contrib.eager.defun.

| Args | |

|  |  |
| --- | --- |
| `executor_type` | a string for the name of the executor to be used to execute functions defined by tf.contrib.eager.defun. |

| Yields | |
| Context manager for setting the executor of eager defined functions. | |