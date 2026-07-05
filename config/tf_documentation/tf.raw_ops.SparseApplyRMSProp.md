# tf.raw_ops.SparseApplyRMSProp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseApplyRMSProp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseApplyRMSProp)

---

Update '\*var' according to the RMSProp algorithm.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseApplyRMSProp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseApplyRMSProp)

```
tf.raw_ops.SparseApplyRMSProp(
    var,
    ms,
    mom,
    lr,
    rho,
    momentum,
    epsilon,
    grad,
    indices,
    use_locking=False,
    name=None
)
```

Note that in dense implementation of this algorithm, ms and mom will
update even if the grad is zero, but in this sparse implementation, ms
and mom will not update in iterations during which the grad is zero.

mean\_square = decay \* mean\_square + (1-decay) \* gradient \*\* 2
Delta = learning\_rate \* gradient / sqrt(mean\_square + epsilon)

\[ms <- rho \* ms\_{t-1} + (1-rho) \* grad \* grad\]

\[mom <- momentum \* mom\_{t-1} + lr \* grad / sqrt(ms + epsilon)\]

\[var <- var - mom\]

| Args | |

|  |  |
| --- | --- |
| `var` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Should be from a Variable(). |
| `ms` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `mom` | A mutable `Tensor`. Must have the same type as `var`. Should be from a Variable(). |
| `lr` | A `Tensor`. Must have the same type as `var`. Scaling factor. Must be a scalar. |
| `rho` | A `Tensor`. Must have the same type as `var`. Decay rate. Must be a scalar. |
| `momentum` | A `Tensor`. Must have the same type as `var`. |
| `epsilon` | A `Tensor`. Must have the same type as `var`. Ridge term. Must be a scalar. |
| `grad` | A `Tensor`. Must have the same type as `var`. The gradient. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A vector of indices into the first dimension of var, ms and mom. |
| `use_locking` | An optional `bool`. Defaults to `False`. If `True`, updating of the var, ms, and mom tensors is protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor`. Has the same type as `var`. | |