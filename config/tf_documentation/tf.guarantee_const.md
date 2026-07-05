# tf.guarantee_const

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/guarantee_const](https://tensorflow.google.cn/api_docs/python/tf/guarantee_const)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L6646-L6662) |

Promise to the TF runtime that the input tensor is a constant. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.guarantee_const`](https://tensorflow.google.cn/api_docs/python/tf/guarantee_const)

```
tf.guarantee_const(
    input, name=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Not for public use.

The runtime is then free to make optimizations based on this.

Returns the input tensor without modification.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `name` | A name for this operation. |

| Returns | |
| A `Tensor`. Has the same dtype as `input`. | |