# tf.debugging.assert_integer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_integer](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_integer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L1427-L1445) |

Assert that `x` is of integer dtype.

```
tf.debugging.assert_integer(
    x, message=None, name=None
)
```

If `x` has a non-integer type, `message`, as well as the dtype of `x` are
printed, and `InvalidArgumentError` is raised.

This can always be checked statically, so this method returns nothing.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_integer". |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `x.dtype` is not a non-quantized integer type. |