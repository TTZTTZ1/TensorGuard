# tf.raw_ops.ResourceSparseApplyProximalGradientDescent

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalGradientDescent](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalGradientDescent)

---

Sparse update '\*var' as FOBOS algorithm with fixed learning rate.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceSparseApplyProximalGradientDescent`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalGradientDescent)

```
tf.raw_ops.ResourceSparseApplyProximalGradientDescent(
    var, alpha, l1, l2, grad, indices, use_locking=False, name=None
)
```

That is for rows we have grad for, we update var as follows:
prox\_v = var - alpha \* grad
var = sign(prox\_v)/(1+alpha\*l2) \* max{|prox\_v|-alpha\*l1,0}

| Args | |

|  |  |
| --- | --- |
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `alpha` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Scaling factor. Must be a scalar. |
| `l1` | A `Tensor`. Must have the same type as `alpha`. L1 regularization. Must be a scalar. |
| `l2` | A `Tensor`. Must have the same type as `alpha`. L2 regularization. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `alpha`. The gradient. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A vector of indices into the first dimension of var and accum. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, the subtraction will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |