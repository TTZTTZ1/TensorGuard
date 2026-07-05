# tf.linalg.eigh_tridiagonal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh_tridiagonal](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh_tridiagonal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L1232-L1588) |

Computes the eigenvalues of a Hermitian tridiagonal matrix.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.eigh_tridiagonal`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh_tridiagonal)

```
tf.linalg.eigh_tridiagonal(
    alpha,
    beta,
    eigvals_only=True,
    select='a',
    select_range=None,
    tol=None,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `alpha` | A real or complex tensor of shape (n), the diagonal elements of the matrix. NOTE: If alpha is complex, the imaginary part is ignored (assumed zero) to satisfy the requirement that the matrix be Hermitian. |
| `beta` | A real or complex tensor of shape (n-1), containing the elements of the first super-diagonal of the matrix. If beta is complex, the first sub-diagonal of the matrix is assumed to be the conjugate of beta to satisfy the requirement that the matrix be Hermitian |
| `eigvals_only` | If False, both eigenvalues and corresponding eigenvectors are computed. If True, only eigenvalues are computed. Default is True. |
| `select` | Optional string with values in {‘a’, ‘v’, ‘i’} (default is 'a') that determines which eigenvalues to calculate: 'a': all eigenvalues. ‘v’: eigenvalues in the interval (min, max] given by `select_range`. 'i’: eigenvalues with indices min <= i <= max. |
| `select_range` | Size 2 tuple or list or tensor specifying the range of eigenvalues to compute together with select. If select is 'a', select\_range is ignored. |
| `tol` | Optional scalar. The absolute tolerance to which each eigenvalue is required. An eigenvalue (or cluster) is considered to have converged if it lies in an interval of this width. If tol is None (default), the value eps\*|T|\_2 is used where eps is the machine precision, and |T|\_2 is the 2-norm of the matrix T. |
| `name` | Optional name of the op. |

| Returns | |

|  |  |
| --- | --- |
| `eig_vals` | The eigenvalues of the matrix in non-decreasing order. |
| `eig_vectors` | If `eigvals_only` is False the eigenvectors are returned in the second output argument. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If input values are invalid. |
| `NotImplemented` | Computing eigenvectors for `eigvals_only` = False is not implemented yet. |

This op implements a subset of the functionality of
scipy.linalg.eigh\_tridiagonal.

**Note:** The result is undefined if the input contains +/-inf or NaN, or if
any value in beta has a magnitude greater than
`numpy.sqrt(numpy.finfo(beta.dtype.as_numpy_dtype).max)`.

Add support for outer batch dimensions.

#### Examples

```
import numpy
eigvals = tf.linalg.eigh_tridiagonal([0.0, 0.0, 0.0], [1.0, 1.0])
eigvals_expected = [-numpy.sqrt(2.0), 0.0, numpy.sqrt(2.0)]
tf.assert_near(eigvals_expected, eigvals)
# ==> True
```