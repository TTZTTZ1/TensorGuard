# tf.eigvals

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/eigvals](https://tensorflow.google.cn/api_docs/python/tf/eigvals)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg_ops.py#L414-L438) |

Computes the eigenvalues of one or more matrices.

#### View aliases

**Main aliases**

[`tf.eigvals`](https://tensorflow.google.cn/api_docs/python/tf/linalg/eigvals)

```
tf.linalg.eigvals(
    tensor, name=None
)
```

**Note:** If your program backpropagates through this function, you should replace
it with a call to tf.linalg.eig (possibly ignoring the second output) to
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