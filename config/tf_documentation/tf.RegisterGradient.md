# tf.RegisterGradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/RegisterGradient](https://tensorflow.google.cn/api_docs/python/tf/RegisterGradient)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L1655-L1700) |

A decorator for registering the gradient function for an op type.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.RegisterGradient`](https://tensorflow.google.cn/api_docs/python/tf/RegisterGradient)

```
tf.RegisterGradient(
    op_type
)
```

This decorator is only used when defining a new op type. For an op
with `m` inputs and `n` outputs, the gradient function is a function
that takes the original `Operation` and `n` `Tensor` objects
(representing the gradients with respect to each output of the op),
and returns `m` `Tensor` objects (representing the partial gradients
with respect to each input of the op).

For example, assuming that operations of type `"Sub"` take two
inputs `x` and `y`, and return a single output `x - y`, the
following gradient function would be registered:

```
@tf.RegisterGradient("Sub")
def _sub_grad(unused_op, grad):
  return grad, tf.negative(grad)
```

The decorator argument `op_type` is the string type of an
operation. This corresponds to the `OpDef.name` field for the proto
that defines the operation.

| Args | |

|  |  |
| --- | --- |
| `op_type` | The string type of an operation. This corresponds to the `OpDef.name` field for the proto that defines the operation. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `op_type` is not string. |

## Methods

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L1697-L1700)

```
__call__(
    f: _T
) -> _T
```

Registers the function `f` as gradient function for `op_type`.