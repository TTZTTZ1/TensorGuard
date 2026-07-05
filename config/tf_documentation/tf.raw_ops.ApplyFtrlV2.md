# tf.raw_ops.ApplyFtrlV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyFtrlV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyFtrlV2)

---

Update '\*var' according to the Ftrl-proximal scheme.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ApplyFtrlV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyFtrlV2)

```
tf.raw_ops.ApplyFtrlV2(
    var,
    accum,
    linear,
    grad,
    lr,
    l1,
    l2,
    l2_shrinkage,
    lr_power,
    use_locking=False,
    multiply_linear_by_lr=False,
    name=None
)
```

grad\_with\_shrinkage = grad + 2 \* l2\_shrinkage \* var
accum\_new = accum + grad \* grad
linear += grad\_with\_shrinkage -
(accum\_new^(-lr\_power) - accum^(-lr\_power)) / lr \* var
quadratic = 1.0 / (accum\_new^(lr\_power) \* lr) + 2 \* l2
var = (sign(linear) \* l1 - linear) / quadratic if |linear| > l1 else 0.0
accum = accum\_new

| Args | |

|  |  |
| --- | --- |
| `var` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Should be from a Variable(). |
| `accum` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `linear` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `grad` | A `Tensor`. Must have the same type as `var`. The gradient. |
| `lr` | A `Tensor`. Must have the same type as `var`. Scaling factor. Must be a scalar. |
| `l1` | A `Tensor`. Must have the same type as `var`. L1 regularization. Must be a scalar. |
| `l2` | A `Tensor`. Must have the same type as `var`. L2 shrinkage regularization. Must be a scalar. |
| `l2_shrinkage` | A `Tensor`. Must have the same type as `var`. |
| `lr_power` | A `Tensor`. Must have the same type as `var`. Scaling factor. Must be a scalar. |
| `use_locking` | An optional `bool`. Defaults to `False`. If `True`, updating of the var and accum tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `multiply_linear_by_lr` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor`. Has the same type as `var`. | |