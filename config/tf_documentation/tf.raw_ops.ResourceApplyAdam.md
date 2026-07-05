# tf.raw_ops.ResourceApplyAdam

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdam](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdam)

---

Update '\*var' according to the Adam algorithm.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceApplyAdam`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdam)

```
tf.raw_ops.ResourceApplyAdam(
    var,
    m,
    v,
    beta1_power,
    beta2_power,
    lr,
    beta1,
    beta2,
    epsilon,
    grad,
    use_locking=False,
    use_nesterov=False,
    name=None
)
```

\[\text{lr}\_t := \mathrm{lr} \cdot \frac{\sqrt{1 - \beta\_2^t} }{1 - \beta\_1^t}\]

\[m\_t := \beta\_1 \cdot m\_{t-1} + (1 - \beta\_1) \cdot g\]

\[v\_t := \beta\_2 \cdot v\_{t-1} + (1 - \beta\_2) \cdot g^2\]

\[\text{var} := \begin{cases} \text{var} - (m\_t \beta\_1 + g \cdot (1 - \beta\_1))\cdot\text{lr}\_t/(\sqrt{v\_t} + \epsilon), &\text{if use\_nesterov}\\\\ \text{var} - m\_t \cdot \text{lr}\_t /(\sqrt{v\_t} + \epsilon), &\text{otherwise} \end{cases}\]

| Args | |

|  |  |
| --- | --- |
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `m` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `v` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `beta1_power` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Must be a scalar. |
| `beta2_power` | A `Tensor`. Must have the same type as `beta1_power`. Must be a scalar. |
| `lr` | A `Tensor`. Must have the same type as `beta1_power`. Scaling factor. Must be a scalar. |
| `beta1` | A `Tensor`. Must have the same type as `beta1_power`. Momentum factor. Must be a scalar. |
| `beta2` | A `Tensor`. Must have the same type as `beta1_power`. Momentum factor. Must be a scalar. |
| `epsilon` | A `Tensor`. Must have the same type as `beta1_power`. Ridge term. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `beta1_power`. The gradient. |
| `use_locking` | An optional `bool`. Defaults to `False`. If `True`, updating of the var, m, and v tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `use_nesterov` | An optional `bool`. Defaults to `False`. If `True`, uses the nesterov update. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |