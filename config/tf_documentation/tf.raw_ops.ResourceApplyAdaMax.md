# tf.raw_ops.ResourceApplyAdaMax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdaMax](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdaMax)

---

Update '\*var' according to the AdaMax algorithm.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceApplyAdaMax`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdaMax)

```
tf.raw_ops.ResourceApplyAdaMax(
    var,
    m,
    v,
    beta1_power,
    lr,
    beta1,
    beta2,
    epsilon,
    grad,
    use_locking=False,
    name=None
)
```

m*t <- beta1 \* m*{t-1} + (1 - beta1) \* g
v*t <- max(beta2 \* v*{t-1}, abs(g))
variable <- variable - learning\_rate / (1 - beta1^t) \* m\_t / (v\_t + epsilon)

| Args | |

|  |  |
| --- | --- |
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `m` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `v` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `beta1_power` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Must be a scalar. |
| `lr` | A `Tensor`. Must have the same type as `beta1_power`. Scaling factor. Must be a scalar. |
| `beta1` | A `Tensor`. Must have the same type as `beta1_power`. Momentum factor. Must be a scalar. |
| `beta2` | A `Tensor`. Must have the same type as `beta1_power`. Momentum factor. Must be a scalar. |
| `epsilon` | A `Tensor`. Must have the same type as `beta1_power`. Ridge term. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `beta1_power`. The gradient. |
| `use_locking` | An optional `bool`. Defaults to `False`. If `True`, updating of the var, m, and v tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |