# tf.identity_n

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/identity_n](https://tensorflow.google.cn/api_docs/python/tf/identity_n)

---

Returns a list of tensors with the same shapes and contents as the input

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.identity_n`](https://tensorflow.google.cn/api_docs/python/tf/identity_n)

```
tf.identity_n(
    input, name=None
)
```

tensors.

This op can be used to override the gradient for complicated functions. For
example, suppose y = f(x) and we wish to apply a custom function g for backprop
such that dx = g(dy). In Python,

```
with tf.get_default_graph().gradient_override_map(
    {'IdentityN': 'OverrideGradientWithG'}):
  y, _ = identity_n([f(x), x])

@tf.RegisterGradient('OverrideGradientWithG')
def ApplyG(op, dy, _):
  return [None, g(dy)]  # Do not backprop to f(x).
```

| Args | |

|  |  |
| --- | --- |
| `input` | A list of `Tensor` objects. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects. Has the same type as `input`. | |