# tf.reduce_prod

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/reduce_prod](https://tensorflow.google.cn/api_docs/python/tf/reduce_prod)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L2664-L2710) |

Computes [`tf.math.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply) of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_prod`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_prod)

```
tf.math.reduce_prod(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Sparse weights using structural pruning](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) * [TensorFlow Distributions: A Gentle Introduction](https://tensorflow.google.cn/probability/examples/TensorFlow_Distributions_Tutorial) |

This is the reduction operation for the elementwise [`tf.math.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply) op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

| For example | |
|  | |

```
>>> x = tf.constant([[1., 2.], [3., 4.]])
>>> tf.math.reduce_prod(x)
<tf.Tensor: shape=(), dtype=float32, numpy=24.>
>>> tf.math.reduce_prod(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)>
>>> tf.math.reduce_prod(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],
dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The tensor to reduce. Should have numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The reduced tensor. | |

## numpy compatibility

Equivalent to np.prod