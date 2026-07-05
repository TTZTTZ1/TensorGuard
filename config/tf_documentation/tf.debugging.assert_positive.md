# tf.debugging.assert_positive

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_positive](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_positive)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L597-L627) |

Assert the condition `x > 0` holds element-wise.

```
tf.debugging.assert_positive(
    x, message=None, summarize=None, name=None
)
```

This Op checks that `x[i] > 0` holds for every element of `x`. If `x` is
empty, this is trivially satisfied.

If `x` is not positive everywhere, `message`, as well as the first `summarize`
entries of `x` are printed, and `InvalidArgumentError` is raised.

| Args | |

|  |  |
| --- | --- |
| `x` | Numeric `Tensor`. |
| `message` | A string to prefix to the default message. |
| `summarize` | Print this many entries of each tensor. |
| `name` | A name for this operation (optional). Defaults to "assert\_positive". |

| Returns | |
| Op raising `InvalidArgumentError` unless `x` is all positive. This can be used with [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) inside of [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s to block followup computation until the check has executed. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if the check can be performed immediately and `x[i] > 0` is False. The check can be performed immediately during eager execution or if `x` is statically known. |

## eager compatibility

returns None