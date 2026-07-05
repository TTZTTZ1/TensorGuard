# tf.debugging.assert_rank

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_rank](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_rank)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L1064-L1095) |

Assert that `x` has rank equal to `rank`.

#### View aliases

**Main aliases**

[`tf.assert_rank`](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_rank)

```
tf.debugging.assert_rank(
    x, rank, message=None, name=None
)
```

This Op checks that the rank of `x` is equal to `rank`.

If `x` has a different rank, `message`, as well as the shape of `x` are
printed, and `InvalidArgumentError` is raised.

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor`. |
| `rank` | Scalar integer `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_rank". |

| Returns | |
| Op raising `InvalidArgumentError` unless `x` has specified rank. If static checks determine `x` has correct rank, a `no_op` is returned. This can be used with [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) inside of [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s to block followup computation until the check has executed. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if the check can be performed immediately and `x` does not have rank `rank`. The check can be performed immediately during eager execution or if the shape of `x` is statically known. |

## eager compatibility

returns None