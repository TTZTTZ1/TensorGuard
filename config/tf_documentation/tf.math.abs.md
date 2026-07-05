# tf.math.abs

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/abs](https://tensorflow.google.cn/api_docs/python/tf/math/abs)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L359-L403) |

Computes the absolute value of a tensor.

#### View aliases

**Main aliases**

[`tf.abs`](https://tensorflow.google.cn/api_docs/python/tf/math/abs)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.abs`](https://tensorflow.google.cn/api_docs/python/tf/math/abs)

```
tf.math.abs(
    x, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Training checkpoints](https://tensorflow.google.cn/guide/checkpoint) * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) * [Estimators](https://tensorflow.google.cn/guide/estimator) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [TF-NumPy Type Promotion](https://tensorflow.google.cn/guide/tf_numpy_type_promotion) | * [CycleGAN](https://tensorflow.google.cn/tutorials/generative/cyclegan) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) |

Given a tensor of integer or floating-point values, this operation returns a
tensor of the same type, where each element contains the absolute value of the
corresponding element in the input.

Given a tensor `x` of complex numbers, this operation returns a tensor of type
`float32` or `float64` that is the absolute value of each element in `x`. For
a complex number \(a + bj\), its absolute value is computed as
\(\sqrt{a^2 + b^2}\).

#### For example:

```
>>> # real number
>>> x = tf.constant([-2.25, 3.25])
>>> tf.abs(x)
<tf.Tensor: shape=(2,), dtype=float32,
numpy=array([2.25, 3.25], dtype=float32)>
```

```
>>> # complex number
>>> x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])
>>> tf.abs(x)
<tf.Tensor: shape=(2, 1), dtype=float64, numpy=
array([[5.25594901],
       [6.60492241]])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64` or `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor` of the same size, type and sparsity as `x`, with absolute values. Note, for `complex64` or `complex128` input, the returned `Tensor` will be of type `float32` or `float64`, respectively. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.abs(x.values, ...), x.dense_shape)`