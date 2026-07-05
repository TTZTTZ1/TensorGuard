# tf.linalg.eigvalsh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/eigvalsh](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigvalsh)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg_ops.py#L465-L486) |

Computes the eigenvalues of one or more self-adjoint matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.eigvalsh`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigvalsh), [`tf.compat.v1.self_adjoint_eigvals`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigvalsh)

```
tf.linalg.eigvalsh(
    tensor, name=None
)
```

**Note:** If your program backpropagates through this function, you should replace
it with a call to tf.linalg.eigh (possibly ignoring the second output) to
avoid computing the eigen decomposition twice. This is because the
eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
\_SelfAdjointEigV2Grad in linalg\_grad.py.

| Args | |

|  |  |
| --- | --- |
| `tensor` | `Tensor` of shape `[..., N, N]`. |
| `name` | string, optional name of the operation. |

| Returns | |

|  |  |
| --- | --- |
| `e` | Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N` eigenvalues of `tensor[..., :, :]`. |