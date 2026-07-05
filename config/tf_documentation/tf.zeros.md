# tf.zeros

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/zeros](https://tensorflow.google.cn/api_docs/python/tf/zeros)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L2565-L2624) |

Creates a tensor with all elements set to zero.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.zeros`](https://tensorflow.google.cn/api_docs/python/tf/zeros)

```
tf.zeros(
    shape,
    dtype=tf.dtypes.float32,
    name=None,
    layout=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Better performance with the tf.data API](https://tensorflow.google.cn/guide/data_performance) * [Training checkpoints](https://tensorflow.google.cn/guide/checkpoint) * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) | * [Custom layers](https://tensorflow.google.cn/tutorials/customization/custom_layers) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Multilevel Modeling Primer in TensorFlow Probability](https://tensorflow.google.cn/probability/examples/Multilevel_Modeling_Primer) |

See also [`tf.zeros_like`](https://tensorflow.google.cn/api_docs/python/tf/zeros_like), [`tf.ones`](https://tensorflow.google.cn/api_docs/python/tf/ones), [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill), [`tf.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye).

This operation returns a tensor of type `dtype` with shape `shape` and
all elements set to zero.

```
>>> tf.zeros([3, 4], tf.int32)
<tf.Tensor: shape=(3, 4), dtype=int32, numpy=
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `shape` | A `list` of integers, a `tuple` of integers, or a 1-D `Tensor` of type `int32`. |
| `dtype` | The DType of an element in the resulting `Tensor`. |
| `name` | Optional string. A name for the operation. |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/Layout). If provided, the result is a [DTensor](https://tensorflow.google.cn/guide/dtensor_overview) with the provided layout. |

| Returns | |
| A `Tensor` with all elements set to zero. | |