# tf.raw_ops.SelfAdjointEig

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SelfAdjointEig](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SelfAdjointEig)

---

Computes the Eigen Decomposition of a batch of square self-adjoint matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SelfAdjointEig`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SelfAdjointEig)

```
tf.raw_ops.SelfAdjointEig(
    input, name=None
)
```

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices, with the same constraints as the single matrix
SelfAdjointEig.

The result is a [..., M+1, M] matrix with [..., 0,:] containing the
eigenvalues, and subsequent [...,1:, :] containing the eigenvectors. The eigenvalues
are sorted in non-decreasing order.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`. Shape is `[..., M, M]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |