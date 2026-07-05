# tf.raw_ops.LogMatrixDeterminant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogMatrixDeterminant](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogMatrixDeterminant)

---

Computes the sign and the log of the absolute value of the determinant of

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LogMatrixDeterminant`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogMatrixDeterminant)

```
tf.raw_ops.LogMatrixDeterminant(
    input, name=None
)
```

one or more square matrices.

The input is a tensor of shape `[N, M, M]` whose inner-most 2 dimensions
form square matrices. The outputs are two tensors containing the signs and
absolute values of the log determinants for all N input submatrices
`[..., :, :]` such that `determinant = sign*exp(log_abs_determinant)`.
The `log_abs_determinant` is computed as `det(P)*sum(log(diag(LU)))` where `LU`
is the `LU` decomposition of the input and `P` is the corresponding
permutation matrix.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`. Shape is `[N, M, M]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (sign, log\_abs\_determinant). | |
| `sign` | A `Tensor`. Has the same type as `input`. |
| `log_abs_determinant` | A `Tensor`. Has the same type as `input`. |