# tf.math.sqrt

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/sqrt](https://tensorflow.google.cn/api_docs/python/tf/math/sqrt)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5420-L5455) |

Computes element-wise square root of the input tensor.

#### View aliases

**Main aliases**

[`tf.sqrt`](https://tensorflow.google.cn/api_docs/python/tf/math/sqrt)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sqrt`](https://tensorflow.google.cn/api_docs/python/tf/math/sqrt)

```
tf.math.sqrt(
    x, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) | * [Uncertainty-aware Deep Learning with SNGP](https://tensorflow.google.cn/tutorials/understanding/sngp) * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) * [Copulas Primer](https://tensorflow.google.cn/probability/examples/Gaussian_Copula) * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) * [Neural machine translation with a Transformer and Keras](https://tensorflow.google.cn/text/tutorials/transformer) |

**Note:** This operation does not support integer types.

```
>>> x = tf.constant([[4.0], [16.0]])
>>> tf.sqrt(x)
<tf.Tensor: shape=(2, 1), dtype=float32, numpy=
  array([[2.],
         [4.]], dtype=float32)>
>>> y = tf.constant([[-4.0], [16.0]])
>>> tf.sqrt(y)
<tf.Tensor: shape=(2, 1), dtype=float32, numpy=
  array([[nan],
         [ 4.]], dtype=float32)>
>>> z = tf.constant([[-1.0], [16.0]], dtype=tf.complex128)
>>> tf.sqrt(z)
<tf.Tensor: shape=(2, 1), dtype=complex128, numpy=
  array([[0.0+1.j],
         [4.0+0.j]])>
```

**Note:** In order to support complex type, please provide an input tensor
of `complex64` or `complex128`.

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128` |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of same size, type and sparsity as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sqrt(x.values, ...), x.dense_shape)`