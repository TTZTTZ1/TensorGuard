# tf.linalg.solve

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/solve](https://tensorflow.google.cn/api_docs/python/tf/linalg/solve)

---

Solves systems of linear equations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.solve`](https://tensorflow.google.cn/api_docs/python/tf/linalg/solve), [`tf.compat.v1.matrix_solve`](https://tensorflow.google.cn/api_docs/python/tf/linalg/solve)

```
tf.linalg.solve(
    matrix: Annotated[Any, TV_MatrixSolve_T],
    rhs: Annotated[Any, TV_MatrixSolve_T],
    adjoint: bool = False,
    name=None
) -> Annotated[Any, TV_MatrixSolve_T]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) | * [A Tour of TensorFlow Probability](https://tensorflow.google.cn/probability/examples/A_Tour_of_TensorFlow_Probability) |

`Matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. `Rhs` is a tensor of shape `[..., M, K]`. The `output` is
a tensor shape `[..., M, K]`. If `adjoint` is `False` then each output matrix
satisfies `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`.
If `adjoint` is `True` then each output matrix satisfies
`adjoint(matrix[..., :, :]) * output[..., :, :] = rhs[..., :, :]`.

| Args | |

|  |  |
| --- | --- |
| `matrix` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `rhs` | A `Tensor`. Must have the same type as `matrix`. Shape is `[..., M, K]`. |
| `adjoint` | An optional `bool`. Defaults to `False`. Boolean indicating whether to solve with `matrix` or its (block-wise) adjoint. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `matrix`. | |