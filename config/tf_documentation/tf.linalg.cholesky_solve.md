# tf.linalg.cholesky_solve

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky_solve](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky_solve)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg_ops.py#L147-L193) |

Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.cholesky_solve`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky_solve), [`tf.compat.v1.linalg.cholesky_solve`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky_solve)

```
tf.linalg.cholesky_solve(
    chol, rhs, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TensorFlow Probability Case Study: Covariance Estimation](https://tensorflow.google.cn/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) |

Specifically, returns `X` from `A X = RHS`, where `A = L L^T`, `L` is the
`chol` arg and `RHS` is the `rhs` arg.

```
# Solve 10 separate 2x2 linear systems:
A = ... # shape 10 x 2 x 2
RHS = ... # shape 10 x 2 x 1
chol = tf.linalg.cholesky(A)  # shape 10 x 2 x 2
X = tf.linalg.cholesky_solve(chol, RHS)  # shape 10 x 2 x 1
# tf.matmul(A, X) ~ RHS
X[3, :, 0]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 0]

# Solve five linear systems (K = 5) for every member of the length 10 batch.
A = ... # shape 10 x 2 x 2
RHS = ... # shape 10 x 2 x 5
...
X[3, :, 2]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 2]
```

| Args | |

|  |  |
| --- | --- |
| `chol` | A `Tensor`. Must be `float32` or `float64`, shape is `[..., M, M]`. Cholesky factorization of `A`, e.g. `chol = tf.linalg.cholesky(A)`. For that reason, only the lower triangular parts (including the diagonal) of the last two dimensions of `chol` are used. The strictly upper part is assumed to be zero and not accessed. |
| `rhs` | A `Tensor`, same type as `chol`, shape is `[..., M, K]`. |
| `name` | A name to give this `Op`. Defaults to `cholesky_solve`. |

| Returns | |
| Solution to `A x = rhs`, shape `[..., M, K]`. | |