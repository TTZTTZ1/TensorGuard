# tf.raw_ops.ResourceSparseApplyProximalAdagrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalAdagrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalAdagrad)

---

Sparse update entries in '*var' and '*accum' according to FOBOS algorithm.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceSparseApplyProximalAdagrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceSparseApplyProximalAdagrad)

```
tf.raw_ops.ResourceSparseApplyProximalAdagrad(
    var, accum, lr, l1, l2, grad, indices, use_locking=False, name=None
)
```

That is for rows we have grad for, we update var and accum as follows:
accum += grad \* grad
prox\_v = var
prox\_v -= lr \* grad \* (1 / sqrt(accum))
var = sign(prox\_v)/(1+lr\*l2) \* max{|prox\_v|-lr\*l1,0}

| Args | |

|  |  |
| --- | --- |
| `var` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `accum` | A `Tensor` of type `resource`. Should be from a Variable(). |
| `lr` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Learning rate. Must be a scalar. |
| `l1` | A `Tensor`. Must have the same type as `lr`. L1 regularization. Must be a scalar. |
| `l2` | A `Tensor`. Must have the same type as `lr`. L2 regularization. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `lr`. The gradient. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A vector of indices into the first dimension of var and accum. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, updating of the var and accum tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |