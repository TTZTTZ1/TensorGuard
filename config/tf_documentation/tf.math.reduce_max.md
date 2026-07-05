# tf.math.reduce_max

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reduce_max](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_max)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L2964-L3011) |

Computes [`tf.math.maximum`](https://tensorflow.google.cn/api_docs/python/tf/math/maximum) of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_max`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_max)

```
tf.math.reduce_max(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) | * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Preprocess data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/simple) * [Tutorial on Multi Armed Bandits in TF-Agents](https://tensorflow.google.cn/agents/tutorials/bandits_tutorial) |

This is the reduction operation for the elementwise [`tf.math.maximum`](https://tensorflow.google.cn/api_docs/python/tf/math/maximum) op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

| Usage example | |
|  | |

```
>>> x = tf.constant([5, 1, 2, 4])
>>> tf.reduce_max(x)
<tf.Tensor: shape=(), dtype=int32, numpy=5>
>>> x = tf.constant([-5, -1, -2, -4])
>>> tf.reduce_max(x)
<tf.Tensor: shape=(), dtype=int32, numpy=-1>
>>> x = tf.constant([4, float('nan')])
>>> tf.reduce_max(x)
<tf.Tensor: shape=(), dtype=float32, numpy=nan>
>>> x = tf.constant([float('nan'), float('nan')])
>>> tf.reduce_max(x)
<tf.Tensor: shape=(), dtype=float32, numpy=nan>
>>> x = tf.constant([float('-inf'), float('inf')])
>>> tf.reduce_max(x)
<tf.Tensor: shape=(), dtype=float32, numpy=inf>
```

See the numpy docs for `np.amax` and `np.nanmax` behavior.

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The tensor to reduce. Should have real numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The reduced tensor. | |