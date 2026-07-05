# tf.linalg.adjoint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/adjoint](https://tensorflow.google.cn/api_docs/python/tf/linalg/adjoint)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L102-L128) |

Transposes the last two dimensions of and conjugates tensor `matrix`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.adjoint`](https://tensorflow.google.cn/api_docs/python/tf/linalg/adjoint)

```
tf.linalg.adjoint(
    matrix, name=None
)
```

#### For example:

```
x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],
                      #  [2 - 2j, 5 - 5j],
                      #  [3 - 3j, 6 - 6j]]
```

| Args | |

|  |  |
| --- | --- |
| `matrix` | A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or `complex128` with shape `[..., M, M]`. |
| `name` | A name to give this `Op` (optional). |

| Returns | |
| The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of matrix. | |