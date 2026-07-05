# tf.linalg.matrix_rank

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/matrix_rank](https://tensorflow.google.cn/api_docs/python/tf/linalg/matrix_rank)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L768-L804) |

Compute the matrix rank of one or more matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.matrix_rank`](https://tensorflow.google.cn/api_docs/python/tf/linalg/matrix_rank)

```
tf.linalg.matrix_rank(
    a, tol=None, validate_args=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `a` | (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be pseudo-inverted. |
| `tol` | Threshold below which the singular value is counted as 'zero'. Default value: `None` (i.e., `eps * max(rows, cols) * max(singular_val)`). |
| `validate_args` | When `True`, additional assertions might be embedded in the graph. Default value: `False` (i.e., no graph assertions are added). |
| `name` | Python `str` prefixed to ops created by this function. Default value: 'matrix\_rank'. |

| Returns | |

|  |  |
| --- | --- |
| `matrix_rank` | (Batch of) `int32` scalars representing the number of non-zero singular values. |