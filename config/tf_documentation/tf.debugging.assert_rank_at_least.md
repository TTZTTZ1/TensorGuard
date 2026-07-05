# tf.debugging.assert_rank_at_least

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_rank_at_least](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_rank_at_least)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L1162-L1193) |

Assert that `x` has rank of at least `rank`.

```
tf.debugging.assert_rank_at_least(
    x, rank, message=None, name=None
)
```

This Op checks that the rank of `x` is greater or equal to `rank`.

If `x` has a rank lower than `rank`, `message`, as well as the shape of `x`
are printed, and `InvalidArgumentError` is raised.

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor`. |
| `rank` | Scalar integer `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_rank\_at\_least". |

| Returns | |
| Op raising `InvalidArgumentError` unless `x` has specified rank or higher. If static checks determine `x` has correct rank, a `no_op` is returned. This can be used with [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) inside of [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s to block followup computation until the check has executed. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | `x` does not have rank at least `rank`, but the rank cannot be statically determined. |
| `ValueError` | If static checks determine `x` has mismatched rank. |

## eager compatibility

returns None