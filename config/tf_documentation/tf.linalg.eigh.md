# tf.linalg.eigh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg_ops.py#L441-L462) |

Computes the eigen decomposition of a batch of self-adjoint matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.eigh`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh), [`tf.compat.v1.self_adjoint_eig`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigh)

```
tf.linalg.eigh(
    tensor, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Quantum data](https://tensorflow.google.cn/quantum/tutorials/quantum_data) * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) |

Computes the eigenvalues and eigenvectors of the innermost N-by-N matrices
in `tensor` such that
`tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

| Args | |

|  |  |
| --- | --- |
| `tensor` | `Tensor` of shape `[..., N, N]`. Only the lower triangular part of each inner inner matrix is referenced. |
| `name` | string, optional name of the operation. |

| Returns | |

|  |  |
| --- | --- |
| `e` | Eigenvalues. Shape is `[..., N]`. Sorted in non-decreasing order. |
| `v` | Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most matrices contain eigenvectors of the corresponding matrices in `tensor` |