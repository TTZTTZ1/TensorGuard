# tf.ones_like

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ones_like](https://tensorflow.google.cn/api_docs/python/tf/ones_like)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L2815-L2866) |

Creates a tensor of all ones that has the same shape as the input.

```
tf.ones_like(
    input, dtype=None, name=None, layout=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) | * [CycleGAN](https://tensorflow.google.cn/tutorials/generative/cyclegan) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Multilevel Modeling Primer in TensorFlow Probability](https://tensorflow.google.cn/probability/examples/Multilevel_Modeling_Primer) * [Research tools](https://tensorflow.google.cn/quantum/tutorials/research_tools) |

See also [`tf.ones`](https://tensorflow.google.cn/api_docs/python/tf/ones).

Given a single tensor (`tensor`), this operation returns a tensor of the
same type and shape as `tensor` with all elements set to 1. Optionally,
you can use `dtype` to specify a new type for the returned tensor.

#### For example:

```
>>> tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> tf.ones_like(tensor)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[1, 1, 1],
         [1, 1, 1]], dtype=int32)>
```

Note that the layout of the input tensor is not preserved if the op
is used inside tf.function. To obtain a tensor with the same layout as the
input, chain the returned value to a [`dtensor.relayout_like`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/relayout_like).

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `dtype` | A type for the returned `Tensor`. Must be `float16`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `complex64`, `complex128`, `bool` or `string`. |
| `name` | A name for the operation (optional). |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/Layout). If provided, the result is a [DTensor](https://tensorflow.google.cn/guide/dtensor_overview) with the provided layout. |

| Returns | |
| A `Tensor` with all elements set to one. | |