# tf.nn.l2_loss

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/l2_loss](https://tensorflow.google.cn/api_docs/python/tf/nn/l2_loss)

---

L2 Loss.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.l2_loss`](https://tensorflow.google.cn/api_docs/python/tf/nn/l2_loss)

```
tf.nn.l2_loss(
    t: Annotated[Any, TV_L2Loss_T], name=None
) -> Annotated[Any, TV_L2Loss_T]
```

Computes half the L2 norm of a tensor without the `sqrt`:

```
output = sum(t ** 2) / 2
```

| Args | |

|  |  |
| --- | --- |
| `t` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. Typically 2-D, but may have any dimensions. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `t`. | |