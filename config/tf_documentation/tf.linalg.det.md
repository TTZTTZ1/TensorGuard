# tf.linalg.det

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/det](https://tensorflow.google.cn/api_docs/python/tf/linalg/det)

---

Computes the determinant of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.det`](https://tensorflow.google.cn/api_docs/python/tf/linalg/det), [`tf.compat.v1.matrix_determinant`](https://tensorflow.google.cn/api_docs/python/tf/linalg/det)

```
tf.linalg.det(
    input: Annotated[Any, TV_MatrixDeterminant_T], name=None
) -> Annotated[Any, TV_MatrixDeterminant_T]
```

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor containing the determinants
for all input submatrices `[..., :, :]`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |