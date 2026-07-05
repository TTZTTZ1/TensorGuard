# tf.linalg.expm

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/expm](https://tensorflow.google.cn/api_docs/python/tf/linalg/expm)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L232-L347) |

Computes the matrix exponential of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.expm`](https://tensorflow.google.cn/api_docs/python/tf/linalg/expm)

```
tf.linalg.expm(
    input, name=None
)
```

\[exp(A) = \sum\_{n=0}^\infty A^n/n!\]

The exponential is computed using a combination of the scaling and squaring
method and the Pade approximation. Details can be found in:
Nicholas J. Higham, "The scaling and squaring method for the matrix
exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the exponential for all input submatrices `[..., :, :]`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op` (optional). |

| Returns | |
| the matrix exponential of the input. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | An unsupported type is provided as input. |

## scipy compatibility

Equivalent to scipy.linalg.expm