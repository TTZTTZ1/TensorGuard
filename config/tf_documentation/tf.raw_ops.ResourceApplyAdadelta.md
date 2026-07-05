# tf.raw_ops.ResourceApplyAdadelta

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdadelta](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdadelta)

---

Update '\*var' according to the adadelta scheme.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceApplyAdadelta`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdadelta)

```
tf.raw_ops.ResourceApplyAdadelta(
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
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `accum` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `accum_update` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `lr` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Scaling factor. Must be a scalar. |
| `rho` | A `Tensor`. Must have the same type as `lr`. Decay factor. Must be a scalar. |
| `epsilon` | A `Tensor`. Must have the same type as `lr`. Constant factor. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `lr`. The gradient. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, updating of the var, accum and update\_accum tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |