# tf.linalg.cholesky

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky)

---

Computes the Cholesky decomposition of one or more square matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.cholesky`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky), [`tf.compat.v1.linalg.cholesky`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cholesky)

```
tf.linalg.cholesky(
    input: Annotated[Any, TV_Cholesky_T], name=None
) -> Annotated[Any, TV_Cholesky_T]
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TensorFlow Probability Case Study: Covariance Estimation](https://tensorflow.google.cn/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) * [TensorFlow Distributions: A Gentle Introduction](https://tensorflow.google.cn/probability/examples/TensorFlow_Distributions_Tutorial) * [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://tensorflow.google.cn/probability/examples/Bayesian_Gaussian_Mixture_Model) * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) |

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices.

The input has to be symmetric and positive definite. Only the lower-triangular
part of the input will be used for this operation. The upper-triangular part
will not be read.

The output is a tensor of the same shape as the input
containing the Cholesky decompositions for all input submatrices `[..., :, :]`.

**Note:** The gradient computation on GPU is faster for large matrices but
not for large batch dimensions when the submatrices are small. In this
case it might be faster to use the CPU.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |