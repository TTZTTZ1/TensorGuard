# tf.no_gradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/no_gradient](https://tensorflow.google.cn/api_docs/python/tf/no_gradient)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L1703-L1735) |

Specifies that ops of type `op_type` is not differentiable.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.NoGradient`](https://tensorflow.google.cn/api_docs/python/tf/no_gradient), [`tf.compat.v1.NotDifferentiable`](https://tensorflow.google.cn/api_docs/python/tf/no_gradient), [`tf.compat.v1.no_gradient`](https://tensorflow.google.cn/api_docs/python/tf/no_gradient)

```
tf.no_gradient(
    op_type: str
) -> None
```

This function should *not* be used for operations that have a
well-defined gradient that is not yet implemented.

This function is only used when defining a new op type. It may be
used for ops such as [`tf.size()`](https://tensorflow.google.cn/api_docs/python/tf/size) that are not differentiable. For
example:

```
tf.no_gradient("Size")
```

The gradient computed for 'op\_type' will then propagate zeros.

For ops that have a well-defined gradient but are not yet implemented,
no declaration should be made, and an error *must* be thrown if
an attempt to request its gradient is made.

| Args | |

|  |  |
| --- | --- |
| `op_type` | The string type of an operation. This corresponds to the `OpDef.name` field for the proto that defines the operation. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `op_type` is not a string. |