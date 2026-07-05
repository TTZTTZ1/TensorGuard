# tf.raw_ops.ApplyAdadelta

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyAdadelta](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyAdadelta)

---

Update '\*var' according to the adadelta scheme.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ApplyAdadelta`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ApplyAdadelta)

```
tf.raw_ops.ApplyAdadelta(
    var,
    accum,
    accum_update,
    lr,
    rho,
    epsilon,
    grad,
    use_locking=False,
    name=None
)
```

accum = rho() \* accum + (1 - rho()) \* grad.square();
update = (update\_accum + epsilon).sqrt() \* (accum + epsilon()).rsqrt() \* grad;
update\_accum = rho() \* update\_accum + (1 - rho()) \* update.square();
var -= update;

| Args | |

|  |  |
| --- | --- |
| `var` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Should be from a Variable(). |
| `accum` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `accum_update` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `lr` | A `Tensor`. Must have the same type as `var`. Scaling factor. Must be a scalar. |
| `rho` | A `Tensor`. Must have the same type as `var`. Decay factor. Must be a scalar. |
| `epsilon` | A `Tensor`. Must have the same type as `var`. Constant factor. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `var`. The gradient. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, updating of the var, accum and update\_accum tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor`. Has the same type as `var`. | |