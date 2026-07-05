# tf.debugging.assert_scalar

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_scalar](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_scalar)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L2154-L2174) |

Asserts that the given `tensor` is a scalar.

```
tf.debugging.assert_scalar(
    tensor, message=None, name=None
)
```

This function raises `ValueError` unless it can be certain that the given
`tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
unknown.

This is always checked statically, so this method returns nothing.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation. Defaults to "assert\_scalar" |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the tensor is not scalar (rank 0), or if its shape is unknown. |