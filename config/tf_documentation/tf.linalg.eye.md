# tf.linalg.eye

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/eye](https://tensorflow.google.cn/api_docs/python/tf/linalg/eye)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg_ops.py#L196-L241) |

Construct an identity matrix, or a batch of matrices.

#### View aliases

**Main aliases**

[`tf.linalg.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye), [`tf.compat.v1.linalg.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye)

```
tf.eye(
    num_rows,
    num_columns=None,
    batch_shape=None,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) | * [TensorFlow Probability Case Study: Covariance Estimation](https://tensorflow.google.cn/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) * [Learnable Distributions Zoo](https://tensorflow.google.cn/probability/examples/Learnable_Distributions_Zoo) * [A Tour of TensorFlow Probability](https://tensorflow.google.cn/probability/examples/A_Tour_of_TensorFlow_Probability) * [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://tensorflow.google.cn/probability/examples/Bayesian_Gaussian_Mixture_Model) * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) |

See also [`tf.ones`](https://tensorflow.google.cn/api_docs/python/tf/ones), [`tf.zeros`](https://tensorflow.google.cn/api_docs/python/tf/zeros), [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill), [`tf.one_hot`](https://tensorflow.google.cn/api_docs/python/tf/one_hot).

```
# Construct one identity matrix.
tf.eye(2)
==> [[1., 0.],
     [0., 1.]]

# Construct a batch of 3 identity matrices, each 2 x 2.
# batch_identity[i, :, :] is a 2 x 2 identity matrix, i = 0, 1, 2.
batch_identity = tf.eye(2, batch_shape=[3])

# Construct one 2 x 3 "identity" matrix
tf.eye(2, num_columns=3)
==> [[ 1.,  0.,  0.],
     [ 0.,  1.,  0.]]
```

| Args | |

|  |  |
| --- | --- |
| `num_rows` | Non-negative `int32` scalar `Tensor` giving the number of rows in each batch matrix. |
| `num_columns` | Optional non-negative `int32` scalar `Tensor` giving the number of columns in each batch matrix. Defaults to `num_rows`. |
| `batch_shape` | A list or tuple of Python integers or a 1-D `int32` `Tensor`. If provided, the returned `Tensor` will have leading batch dimensions of this shape. |
| `dtype` | The type of an element in the resulting `Tensor` |
| `name` | A name for this `Op`. Defaults to "eye". |

| Returns | |
| A `Tensor` of shape `batch_shape + [num_rows, num_columns]` | |