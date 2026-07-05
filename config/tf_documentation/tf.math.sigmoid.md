# tf.math.sigmoid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/sigmoid](https://tensorflow.google.cn/api_docs/python/tf/math/sigmoid)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L4069-L4119) |

Computes sigmoid of `x` element-wise.

#### View aliases

**Main aliases**

[`tf.nn.sigmoid`](https://tensorflow.google.cn/api_docs/python/tf/math/sigmoid), [`tf.sigmoid`](https://tensorflow.google.cn/api_docs/python/tf/math/sigmoid)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sigmoid`](https://tensorflow.google.cn/api_docs/python/tf/math/sigmoid)

```
tf.math.sigmoid(
    x, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) | * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Classify structured data using Keras preprocessing layers](https://tensorflow.google.cn/tutorials/structured_data/preprocessing_layers) * [Classify text with BERT](https://tensorflow.google.cn/text/tutorials/classify_text_with_bert) * [Shape Constraints for Ethics with Tensorflow Lattice](https://tensorflow.google.cn/lattice/tutorials/shape_constraints_for_ethics) |

Formula for calculating \(\mathrm{sigmoid}(x) = y = 1 / (1 + \exp(-x))\).

For \(x \in (-\infty, \infty)\), \(\mathrm{sigmoid}(x) \in (0, 1)\).

#### Example Usage:

If a positive number is large, then its sigmoid will approach to 1 since the
formula will be `y = <large_num> / (1 + <large_num>)`

```
>>> x = tf.constant([0.0, 1.0, 50.0, 100.0])
>>> tf.math.sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32,
numpy=array([0.5, 0.7310586, 1.0, 1.0], dtype=float32)>
```

If a negative number is large, its sigmoid will approach to 0 since the
formula will be `y = 1 / (1 + <large_num>)`

```
>>> x = tf.constant([-100.0, -50.0, -1.0, 0.0])
>>> tf.math.sigmoid(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=
array([0.0000000e+00, 1.9287499e-22, 2.6894143e-01, 0.5],
      dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A Tensor with type `float16`, `float32`, `float64`, `complex64`, or `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A Tensor with the same type as `x`. | |

#### Usage Example:

```
>>> x = tf.constant([-128.0, 0.0, 128.0], dtype=tf.float32)
>>> tf.sigmoid(x)
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([0. , 0.5, 1. ], dtype=float32)>
```

## scipy compatibility

Equivalent to scipy.special.expit