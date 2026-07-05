# tf.raw_ops.ResourceApplyAdagrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdagrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdagrad)

---

Update '\*var' according to the adagrad scheme.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceApplyAdagrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceApplyAdagrad)

```
tf.raw_ops.ResourceApplyAdagrad(
    var, accum, lr, grad, use_locking=False, update_slots=True, name=None
)
```

accum += grad \* grad
var -= lr \* grad \* (1 / sqrt(accum))

| Args | |

|  |  |
| --- | --- |
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `accum` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `lr` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Scaling factor. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `lr`. The gradient. |
| `use_locking` | An optional `bool`. Defaults to `False`. If `True`, updating of the var and accum tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `update_slots` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |