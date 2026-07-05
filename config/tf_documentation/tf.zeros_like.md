# tf.zeros_like

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/zeros_like](https://tensorflow.google.cn/api_docs/python/tf/zeros_like)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L2667-L2719) |

Creates a tensor with all elements set to zero.

```
tf.zeros_like(
    input, dtype=None, name=None, layout=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Automatically rewrite TF 1.x and compat.v1 API symbols](https://tensorflow.google.cn/guide/migrate/upgrade) | * [CycleGAN](https://tensorflow.google.cn/tutorials/generative/cyclegan) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) |

See also [`tf.zeros`](https://tensorflow.google.cn/api_docs/python/tf/zeros).

Given a single tensor or array-like object (`input`), this operation returns
a tensor of the same type and shape as `input` with all elements set to zero.
Optionally, you can use `dtype` to specify a new type for the returned tensor.

Note that the layout of the input tensor is not preserved if the op
is used inside tf.function. To obtain a tensor with the same layout as the
input, chain the returned value to a [`dtensor.relayout_like`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/relayout_like).

| Examples | |
|  | |

```
>>> tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> tf.zeros_like(tensor)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[0, 0, 0],
       [0, 0, 0]], dtype=int32)>
```

```
>>> tf.zeros_like(tensor, dtype=tf.float32)
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
```

```
>>> tf.zeros_like([[1, 2, 3], [4, 5, 6]])
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[0, 0, 0],
       [0, 0, 0]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` or array-like object. |
| `dtype` | A type for the returned `Tensor`. Must be `float16`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `complex64`, `complex128`, `bool` or `string` (optional). |
| `name` | A name for the operation (optional). |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/Layout). If provided, the result is a [DTensor](https://tensorflow.google.cn/guide/dtensor_overview) with the provided layout. |

| Returns | |
| A `Tensor` with all elements set to zero. | |